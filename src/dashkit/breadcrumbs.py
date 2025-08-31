"""Breadcrumb navigation component."""

from dataclasses import dataclass
from typing import Any

import dash_iconify
from dash import Input, Output, callback, dcc, html, page_registry


@dataclass
class Crumb:
    """Data for a single breadcrumb."""

    label: str
    icon: str | None = None
    href: str | None = None


def Breadcrumbs(id: str = "breadcrumbs") -> html.Nav:
    """Render the breadcrumb container.

    This returns an empty ``Nav`` element that will be populated via a
    callback whenever the URL changes.

    Pages can override labels, icons, or hide specific crumbs by passing a
    ``breadcrumbs`` list to :func:`dash.register_page`. Each item should have
    a ``path`` key and optional ``label``, ``icon``, or ``hide`` keys.
    """

    return html.Nav(
        id=id,
        className="flex items-center gap-1 text-sm px-4 py-2 text-dashkit-text dark:text-dashkit-text-invert",
    )


@callback(Output("breadcrumbs", "children"), Input("url", "pathname"))
def _update_breadcrumbs(pathname: str | None) -> list[Any]:
    """Update breadcrumb trail based on current pathname."""

    if pathname is None:
        return []

    # Locate current page entry
    current_page: dict[str, Any] | None = None
    for page in page_registry.values():
        if page.get("path") == pathname:
            current_page = page
            break

    # Map overrides by path for quick lookup
    override_map: dict[str, dict[str, Any]] = {}
    if current_page and current_page.get("breadcrumbs"):
        for override in current_page.get("breadcrumbs", []):
            path = override.get("path")
            if path:
                override_map[path] = override

    crumbs: list[Crumb] = [Crumb(label="Home", icon="home", href="/")]

    parts = [p for p in pathname.strip("/").split("/") if p]
    path_accum = ""
    for part in parts:
        path_accum += "/" + part
        page = next(
            (p for p in page_registry.values() if p.get("path") == path_accum), None
        )
        label = (
            page.get("name") or page.get("title")
            if page
            else part.replace("-", " ").title()
        )
        icon = page.get("icon") if page else None

        if override := override_map.get(path_accum):
            label = override.get("label", label)
            icon = override.get("icon", icon)
            if override.get("hide"):
                continue

        crumbs.append(Crumb(label=label, icon=icon, href=path_accum))

    # Current page should not be a link
    if crumbs:
        crumbs[-1].href = None

    elements: list[Any] = []
    for idx, crumb in enumerate(crumbs):
        icon_elem = (
            dash_iconify.DashIconify(
                icon=crumb.icon if ":" in crumb.icon else f"mynaui:{crumb.icon}",
                width=14,
                className="mr-1",
            )
            if crumb.icon
            else None
        )
        label_elem = html.Span(crumb.label)

        if crumb.href:
            link = dcc.Link(
                [icon_elem, label_elem] if icon_elem else label_elem,
                href=crumb.href,
                className="flex items-center hover:underline",
            )
            elements.append(link)
        else:
            elements.append(
                html.Span(
                    [icon_elem, label_elem] if icon_elem else label_elem,
                    className="flex items-center",
                )
            )

        if idx < len(crumbs) - 1:
            elements.append(
                dash_iconify.DashIconify(
                    icon="mynaui:chevron-right",
                    width=12,
                    className="mx-1 text-dashkit-icon-light dark:text-dashkit-icon-dark",
                )
            )

    return elements
