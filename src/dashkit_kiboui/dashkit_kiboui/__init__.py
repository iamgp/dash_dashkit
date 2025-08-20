from pathlib import Path

try:
    from importlib.metadata import version as _pkg_version
    __version__ = _pkg_version("dashkit_kiboui")
except Exception:
    __version__ = "0.0.0"

# Get the directory of this package
_current_dir = Path(__file__).parent

# Define the JavaScript distribution files for Dash
_js_dist = [
    {"relative_package_path": "dashkit_kiboui.js", "namespace": "dashkit_kiboui"}
]

_js_dist.append(
    {
        "dev_package_path": "proptypes.js",
        "dev_only": True,
        "namespace": "dashkit_kiboui",
    }
)

# Import generated components after build
try:
    from ._imports_ import *  # noqa: F401,F403
    from .ContributionGraph import ContributionGraph  # noqa: F401
    from .ContributionGraphBlock import ContributionGraphBlock  # noqa: F401
    from .ContributionGraphCalendar import ContributionGraphCalendar  # noqa: F401

    # Set the _js_dist attribute on all components so Dash can find them
    ContributionGraph._js_dist = _js_dist
    ContributionGraphCalendar._js_dist = _js_dist
    ContributionGraphBlock._js_dist = _js_dist
except ImportError:
    # Components not yet generated - will be created during build
    pass
