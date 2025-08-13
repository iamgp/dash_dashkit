from typing import Any

import dash_iconify
from dash import (
    Input,
    Output,
    clientside_callback,
    dcc,
    html,
    page_registry,
)

from .logo import LogoSection
from .navigation import SidebarNavigation


def _register_section_callback(section_id: str):
    """Register a clientside callback for section toggle functionality."""
    toggle_id = f"{section_id}-toggle"
    content_id = f"{section_id}-content"
    chevron_id = f"{section_id}-chevron"

    try:
        clientside_callback(
            """
            function(n_clicks) {
                if (!n_clicks) return window.dash_clientside.no_update;

                const content = document.getElementById('"""
            + content_id
            + """');
                const chevron = document.getElementById('"""
            + chevron_id
            + """');

                if (content && chevron) {
                    const isHidden = content.classList.contains('hidden');

                    if (isHidden) {
                        content.classList.remove('hidden');
                        content.classList.add('block');
                        // Update iconify icon
                        chevron.setAttribute('icon', 'mynaui:chevron-down');
                    } else {
                        content.classList.remove('block');
                        content.classList.add('hidden');
                        // Update iconify icon
                        chevron.setAttribute('icon', 'mynaui:chevron-right');
                    }
                }

                return window.dash_clientside.no_update;
            }
            """,
            Output(toggle_id, "n_clicks", allow_duplicate=True),
            Input(toggle_id, "n_clicks"),
            prevent_initial_call=True,
        )
    except Exception:
        # Callback might already be registered, skip silently
        pass


def _register_active_state_callback(url_id: str = "url"):
    """Register callback to handle active states based on current URL."""
    try:
        clientside_callback(
            """
            function(pathname) {
                console.log('Pathname changed to:', pathname);

                // Remove active class from all sidebar items
                document.querySelectorAll('.sidebar-item').forEach(function(item) {
                    item.classList.remove('active');
                    console.log('Removed active from:', item.getAttribute('href'));
                });

                // Find and activate the current page item
                document.querySelectorAll('.sidebar-item').forEach(function(item) {
                    var href = item.getAttribute('href');
                    console.log('Checking href:', href, 'against pathname:', pathname);
                    if (href === pathname) {
                        item.classList.add('active');
                        console.log('Added active to:', href);
                    }
                });

                return window.dash_clientside.no_update;
            }
            """,
            Output(url_id, "pathname", allow_duplicate=True),
            Input(url_id, "pathname"),
            prevent_initial_call="initial_duplicate",
        )
    except Exception as e:
        print(f"Error registering active state callback: {e}")
        # Callback might already be registered, skip silently
        pass


def create_sidebar(
    brand_name: str,
    brand_initial: str,
    nav_items: list[dict[str, Any]] | None = None,
    sections: list[dict[str, Any]] | None = None,
    use_pages: bool = True,
    include_location: bool = False,
) -> html.Div:
    """Create a reusable sidebar component.

    If ``use_pages`` is True, the sidebar is built dynamically from Dash's
    page registry. You can control sidebar behaviour per page by passing
    extra keyword arguments to ``dash.register_page``. Supported keys:

    - ``sidebar_section``: str section name (default: "Main")
    - ``sidebar_visible``: bool include page in sidebar (default: True)
    - ``sidebar_expanded``: bool expand the section by default (default: True)
    - ``sidebar_order``: int order within section (fallback to ``order`` or title)
    - ``icon``: string icon class (e.g., "fas fa-home") for the nav item

    Args:
        brand_name: The brand/company name for the logo
        brand_initial: Initial letter for the logo
        nav_items: Explicit navigation items (ignored if ``use_pages`` is True)
        sections: Explicit sections config (ignored if ``use_pages`` is True)
        use_pages: When True, generate items from ``dash.page_registry``
        include_location: When True, include dcc.Location component (set to False if you have one already)
    """

    # Create navigation instance
    nav = SidebarNavigation()

    # If using pages, generate nav_items/sections from page_registry
    if use_pages:
        generated_sections: dict[str, dict[str, Any]] = {}

        for _page in page_registry.values():
            supplied: dict[str, Any] = _page.get("supplied", {}) or {}

            # visibility
            if supplied.get("sidebar_visible", True) is False:
                continue

            section_name: str = supplied.get("sidebar_section", "Main")
            expanded: bool = supplied.get("sidebar_expanded", True)

            section_bucket = generated_sections.setdefault(
                section_name,
                {"expanded": expanded, "items": []},
            )

            # Prefer sidebar-specific order; fallback to page order
            order = supplied.get("sidebar_order", _page.get("order", 0))

            # Compose item
            item = {
                "type": "nav_item",
                "icon": supplied.get("icon", _page.get("icon", "circle")),
                "label": _page.get("name") or _page.get("title") or _page.get("path"),
                "href": _page.get("path"),
                "order": order,
            }

            section_bucket["items"].append(item)

        # Sort items within sections and build rendered structures
        nav_items = []  # type: ignore[assignment]
        rendered_sections = []
        for section_title, meta in sorted(
            generated_sections.items(), key=lambda kv: kv[0] or ""
        ):

            def _safe_order(value: Any) -> int:
                try:
                    return int(value)
                except Exception:
                    return 0

            items_sorted = sorted(
                meta["items"],
                key=lambda it: (_safe_order(it.get("order")), str(it.get("label", ""))),
            )

            section_items = [
                nav.create_nav_item(
                    it["icon"], it["label"], href=it.get("href", "#"), active=False
                )
                for it in items_sorted
            ]

            section_id = f"sidebar-section-{section_title.lower().replace(' ', '-')}"
            rendered_section = nav.create_section(
                section_title,
                section_items,
                expanded=meta.get("expanded", True),
                section_id=section_id,
            )
            rendered_sections.append(rendered_section)
            _register_section_callback(section_id)

    else:
        # Manual mode: Convert provided configs
        nav_items = nav_items or []
        sections = sections or []

        # Convert nav_items config to actual nav items
        rendered_nav_items = []
        for item in nav_items:
            rendered_nav_items.append(
                nav.create_nav_item(
                    item["icon"],
                    item["label"],
                    active=False,
                    href=item.get("href", "#"),
                )
            )

        # Convert sections config to actual sections
        rendered_sections = []
        for section in sections:
            section_items = []
            section_id = f"sidebar-section-{section['title'].lower().replace(' ', '-')}"

            for item in section["items"]:
                if isinstance(item, str):
                    section_items.append(item)
                elif item.get("type") == "nav_item":
                    section_items.append(
                        nav.create_nav_item(
                            item["icon"],
                            item["label"],
                            active=False,
                            href=item.get("href", "#"),
                        )
                    )
                elif item.get("type") == "button":
                    section_items.append(
                        html.Button(
                            [
                                dash_iconify.DashIconify(
                                    icon=f"mynaui:{item['icon']}",
                                    width=16,
                                    className="mr-2",
                                ),
                                item["label"],
                            ],
                            className="text-sm text-blue-600 hover:text-blue-700 px-3 py-2 w-full text-left",
                        )
                    )

            rendered_sections.append(
                nav.create_section(
                    section["title"],
                    section_items,
                    expanded=section.get("expanded", False),
                    section_id=section_id,
                )
            )
            _register_section_callback(section_id)

        # In manual mode, also expose the items list
        rendered_nav_items = [
            html.Li(it, className="mb-px") for it in rendered_nav_items
        ]

    sidebar_content = html.Div(
        [
            LogoSection(brand_name, brand_initial),
            # Navigation (in pages mode, nav items go into sections; we still render any standalone items if present)
            SidebarNavigation().render(
                [] if use_pages else rendered_nav_items, rendered_sections
            ),
        ],
        className="bg-dashkit-panel-light dark:bg-dashkit-panel-dark w-64 h-screen border-r border-dashkit-border-light dark:border-dashkit-border-dark flex flex-col shrink-0",
    )

    # Register callback to handle active states
    if include_location:
        url_id = "sidebar-url"
        _register_active_state_callback(url_id)
        return html.Div([dcc.Location(id=url_id, refresh=False), sidebar_content])
    else:
        _register_active_state_callback("url")
        return sidebar_content
