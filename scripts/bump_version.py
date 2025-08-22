#!/usr/bin/env python3
import argparse
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

REPOS = {
    "dashkit": ROOT / "pyproject.toml",
    "table": ROOT / "src" / "dashkit_table" / "pyproject.toml",
    "kiboui": ROOT / "src" / "dashkit_kiboui" / "pyproject.toml",
    "shadcn": ROOT / "src" / "dashkit_shadcn" / "pyproject.toml",
}

VERSION_RE = re.compile(
    r'^(\s*version\s*=\s*")(?P<ver>\d+\.\d+\.\d+)("\s*)$', re.MULTILINE
)
PKG_CONSTRAINTS = {
    "table": "dashkit_table",
    "kiboui": "dashkit_kiboui",
    "shadcn": "dashkit_shadcn",
}


def parse_args():
    p = argparse.ArgumentParser(description="Bump versions for selected repos")
    p.add_argument(
        "--repos",
        default="dashkit,table,kiboui,shadcn",
        help="Comma-separated list of repos to bump: dashkit,table,kiboui,shadcn or 'all'",
    )
    p.add_argument(
        "--type",
        choices=["major", "minor", "patch"],
        default="patch",
        help="Which part of the version to bump",
    )
    p.add_argument(
        "--interactive",
        action="store_true",
        help="Prompt to select repos and bump type (default when no args)",
    )
    # Release/VC options
    p.add_argument(
        "--commit", action="store_true", help="Create a Git commit with the changes"
    )
    p.add_argument("--tag", action="store_true", help="Create a Git tag after commit")
    p.add_argument(
        "--tag-name",
        default=None,
        help="Explicit tag name to create (overrides prefix+version)",
    )
    p.add_argument(
        "--tag-prefix",
        default="v",
        help="Prefix for tag when --tag-name not provided (default: v)",
    )
    p.add_argument("--push", action="store_true", help="Push commit and tag to remote")
    p.add_argument(
        "--remote", default="origin", help="Remote name for push (default: origin)"
    )
    return p.parse_args()


def bump_semver(ver: str, kind: str) -> str:
    major, minor, patch = [int(x) for x in ver.split(".")]
    if kind == "major":
        return f"{major + 1}.0.0"
    if kind == "minor":
        return f"{major}.{minor + 1}.0"
    return f"{major}.{minor}.{patch + 1}"


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def write_text(path: Path, content: str) -> None:
    path.write_text(content, encoding="utf-8")


def bump_file(path: Path, kind: str) -> tuple[str, str]:
    content = read_text(path)
    m = VERSION_RE.search(content)
    if not m:
        raise RuntimeError(f"No version line found in {path}")
    old = m.group("ver")
    new = bump_semver(old, kind)

    def repl(mm: re.Match) -> str:
        return f"{mm.group(1)}{new}{mm.group(3)}"

    new_content = VERSION_RE.sub(repl, content, count=1)
    write_text(path, new_content)
    return old, new


def update_root_constraints(root_path: Path, new_versions: dict[str, str]) -> bool:
    """Update >= constraints in root optional-dependencies to match bumped subpackages.

    Returns True if file was modified.
    """
    if not new_versions:
        return False
    content = read_text(root_path)
    modified = False
    for repo_key, new_ver in new_versions.items():
        if repo_key not in PKG_CONSTRAINTS:
            continue
        pkg = PKG_CONSTRAINTS[repo_key]
        # Replace entries like "dashkit_table>=1.1.2"
        pattern = re.compile(rf'("{re.escape(pkg)}>=)(\d+\.\d+\.\d+)(")')

        def repl(mm: re.Match) -> str:
            return f"{mm.group(1)}{new_ver}{mm.group(3)}"  # noqa: B023

        new_content, n = pattern.subn(repl, content)
        if n:
            content = new_content
            modified = True
    if modified:
        write_text(root_path, content)
    return modified


# ---------------- Git helpers -----------------


def _run_git(*args: str) -> subprocess.CompletedProcess:
    return subprocess.run(
        ["git", *args],
        cwd=str(ROOT),
        capture_output=True,
        text=True,
    )


def _ensure_git_repo() -> bool:
    cp = _run_git("rev-parse", "--is-inside-work-tree")
    return cp.returncode == 0 and cp.stdout.strip() == "true"


def _git_add(paths: list[Path]) -> None:
    rels = [str(p.relative_to(ROOT)) for p in paths]
    _run_git("add", "--", *rels)


def _git_commit(message: str) -> bool:
    cp = _run_git("commit", "-m", message)
    return cp.returncode == 0


def _git_tag(tag_name: str, message: str) -> bool:
    cp = _run_git("tag", "-a", tag_name, "-m", message)
    return cp.returncode == 0


def _git_push(remote: str, push_tags: bool) -> None:
    _run_git("push", remote, "HEAD")
    if push_tags:
        _run_git("push", remote, "--tags")


# ---------------- Interactive helpers -----------------


def _prompt_select_repos() -> list[str]:
    keys = list(REPOS.keys())
    print(
        "Select repos to bump (comma-separated numbers or names; 'all' for all; blank to cancel):"
    )
    for i, k in enumerate(keys, 1):
        print(f"  {i}) {k}")
    sel = input("> ").strip()
    if not sel:
        raise SystemExit("Cancelled.")
    if sel.lower() == "all":
        return keys
    chosen: list[str] = []
    for token in [t.strip() for t in sel.split(",") if t.strip()]:
        if token.isdigit():
            idx = int(token)
            if 1 <= idx <= len(keys):
                chosen.append(keys[idx - 1])
            else:
                print(f"Ignoring out-of-range index: {token}")
        elif token in REPOS:
            chosen.append(token)
        else:
            print(f"Ignoring unknown repo: {token}")
    if not chosen:
        raise SystemExit("No valid repos selected. Cancelled.")
    return chosen


def _prompt_bump_type() -> str:
    print("Select bump type [1] patch  [2] minor  [3] major (default: 1):")
    sel = input("> ").strip()
    mapping = {
        "1": "patch",
        "2": "minor",
        "3": "major",
        "patch": "patch",
        "minor": "minor",
        "major": "major",
    }
    if not sel:
        return "patch"
    kind = mapping.get(sel.lower())
    if not kind:
        print("Invalid selection; defaulting to patch")
        return "patch"
    return kind


def _yesno(prompt: str, default: bool = False) -> bool:
    suffix = " [Y/n]: " if default else " [y/N]: "
    ans = input(prompt + suffix).strip().lower()
    if not ans:
        return default
    return ans in {"y", "yes"}


def main():
    args = parse_args()
    interactive = args.interactive or (len(sys.argv) == 1)

    # Defaults from args (non-interactive)
    commit_flag = args.commit
    tag_flag = args.tag
    push_flag = args.push
    remote = args.remote
    tag_name = args.tag_name
    tag_prefix = args.tag_prefix

    if interactive:
        targets = _prompt_select_repos()
        bump_type = _prompt_bump_type()
        print(f"You selected repos: {', '.join(targets)}; bump type: {bump_type}")
        confirm = _yesno("Proceed?", default=False)
        if not confirm:
            raise SystemExit("Cancelled.")
        # Ask for VC actions
        commit_flag = _yesno("Create a Git commit?", default=True)
        tag_flag = _yesno("Create an annotated tag?", default=False)
        if tag_flag and not tag_name:
            custom = input("Tag name (blank to auto-generate): ").strip()
            tag_name = custom or None
        push_flag = _yesno("Push to remote?", default=False)
        if push_flag:
            r = input(f"Remote name [{remote}]: ").strip()
            if r:
                remote = r
    else:
        repos_arg = args.repos.strip()
        if repos_arg == "all":
            targets = list(REPOS.keys())
        else:
            targets = [r.strip() for r in repos_arg.split(",") if r.strip()]
        bump_type = args.type
        unknown = [r for r in targets if r not in REPOS]
        if unknown:
            raise SystemExit(
                f"Unknown repos: {', '.join(unknown)}. Valid: {', '.join(REPOS)}"
            )

    bumped: dict[str, str] = {}
    changed_paths: list[Path] = []

    for repo in targets:
        path = REPOS[repo]
        if not path.exists():
            raise SystemExit(f"Path not found for {repo}: {path}")
        old, new = bump_file(path, bump_type)
        bumped[repo] = new
        changed_paths.append(path)
        print(f"Bumped {repo}: {old} -> {new} ({path})")

    # If any subpackages were bumped, update root constraints
    subs = {k: v for k, v in bumped.items() if k in PKG_CONSTRAINTS}
    if subs:
        if update_root_constraints(REPOS["dashkit"], subs):
            print("Updated root optional-dependencies constraints.")
            if REPOS["dashkit"] not in changed_paths:
                changed_paths.append(REPOS["dashkit"])

    # Optionally commit, tag, and push
    if commit_flag or tag_flag or push_flag:
        if not _ensure_git_repo():
            raise SystemExit(
                "Not a Git repo (or Git not available); cannot commit/tag/push."
            )
        if changed_paths:
            _git_add(changed_paths)
        commit_msg_parts = [f"{name} {ver}" for name, ver in bumped.items()]
        commit_msg = f"chore(release): bump versions: {'; '.join(commit_msg_parts)}"
        if commit_flag or tag_flag:
            did_commit = _git_commit(commit_msg)
            if did_commit:
                print("Created commit:", commit_msg)
            else:
                print("No changes to commit or commit failed.")
        # Determine tag names per repo (use GitHub Actions conventions in .github/workflows/release.yml)
        if tag_flag:
            TAG_PREFIXES = {
                "dashkit": "dashkit-v",
                "table": "dashkit_table-v",
                "kiboui": "dashkit_kiboui-v",
                "shadcn": "dashkit_shadcn-v",
            }
            tags_to_create: list[tuple[str, str]] = []  # (tag_name, message)
            if tag_name and len(bumped) == 1:
                # Single repo: respect explicit tag name
                next(iter(bumped.keys()))
                tn = tag_name
                msg = f"Release {tn} ({'; '.join(commit_msg_parts)})"
                tags_to_create.append((tn, msg))
            else:
                if tag_name and len(bumped) > 1:
                    print(
                        "Note: --tag-name ignored when tagging multiple repos; using per-repo conventions."
                    )
                for repo_key, ver in bumped.items():
                    prefix = TAG_PREFIXES.get(repo_key, tag_prefix)
                    tn = f"{prefix}{ver}"
                    msg = f"Release {tn} ({'; '.join(commit_msg_parts)})"
                    tags_to_create.append((tn, msg))
            for tn, tag_msg in tags_to_create:
                if _git_tag(tn, tag_msg):
                    print(f"Created tag {tn}")
                else:
                    print(f"Failed to create tag {tn}")
        if push_flag:
            _git_push(remote, push_tags=tag_flag)
            print(f"Pushed to {remote}")


if __name__ == "__main__":
    main()
