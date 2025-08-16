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


def _register_nav_item_callback(nav_item_id: str):
    """Register a clientside callback for nav item toggle functionality."""
    toggle_id = f"{nav_item_id}-toggle"
    content_id = f"{nav_item_id}-content"
    chevron_id = f"{nav_item_id}-chevron"

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
        # First pass: collect all pages and organize by section and parent
        pages_by_section: dict[str, list[dict[str, Any]]] = {}
        all_pages: dict[str, dict[str, Any]] = {}
        
        for _page in page_registry.values():
            supplied: dict[str, Any] = _page.get("supplied", {}) or {}

            # visibility
            if _page.get("sidebar_visible", True) is False:
                continue

            section_name: str = _page.get("sidebar_section", "Main")
            parent_name: str | None = _page.get("sidebar_parent")
            expanded: bool = _page.get("sidebar_expanded", True)
            order = _page.get("sidebar_order", _page.get("order", 0))
            is_collapsible = _page.get("sidebar_collapsible", False)
            

            # Compose page info  
            icon_value = _page.get("icon", "circle")
            print(f"Page {_page.get('title')}: icon = '{icon_value}'")
            page_info = {
                "type": "nav_item", 
                "icon": icon_value,
                "label": _page.get("name") or _page.get("title") or _page.get("path"),
                "href": _page.get("path"),
                "order": order,
                "section": section_name,
                "parent": parent_name,
                "expanded": expanded,
                "collapsible": is_collapsible,
                "children": []
            }
            
            all_pages[page_info["label"]] = page_info
            
            # Group by section
            if section_name not in pages_by_section:
                pages_by_section[section_name] = []
            pages_by_section[section_name].append(page_info)

        # Second pass: build hierarchy by connecting children to parents
        for section_name, pages in pages_by_section.items():
            for page in pages:
                if page["parent"]:
                    # Find parent in the same section - could be another page or the section itself
                    parent_found = False
                    for potential_parent in pages:
                        if potential_parent["label"] == page["parent"]:
                            potential_parent["children"].append(page)
                            potential_parent["collapsible"] = True
                            parent_found = True
                            break
                    
                    # If parent not found in pages, might be referencing the section itself
                    if not parent_found and page["parent"] == section_name:
                        # This page's parent is the section itself, treat as top-level
                        page["parent"] = None

        def _safe_order(value: Any) -> int:
            try:
                return int(value)
            except Exception:
                return 0

        # Third pass: render sections with hierarchy
        rendered_sections = []
        for section_title, pages in sorted(pages_by_section.items()):
            # Only include top-level items (those without parents)
            # But exclude items that are just section containers (same name as section)
            top_level_items = []
            for p in pages:
                if not p["parent"]:
                    # Skip pages that are just section containers (same name as section)
                    if p["label"].lower() == section_title.lower():
                        continue
                    else:
                        # Regular top-level page
                        top_level_items.append(p)
            
            # Sort top-level items
            top_level_items.sort(key=lambda it: (_safe_order(it.get("order")), str(it.get("label", ""))))
            
            section_items = []
            for item in top_level_items:
                if item["children"]:
                    # Create collapsible nav item
                    children_data = []
                    for child in sorted(item["children"], key=lambda c: (_safe_order(c.get("order")), str(c.get("label", "")))):
                        children_data.append({
                            "icon": child["icon"],
                            "label": child["label"],
                            "href": child["href"],
                            "active": False
                        })
                    
                    nav_item_id = f"nav-item-{item['label'].lower().replace(' ', '-')}"
                    collapsible_item = nav.create_collapsible_nav_item(
                        item["icon"],
                        item["label"],
                        children_data,
                        expanded=item["expanded"],
                        nav_item_id=nav_item_id
                    )
                    section_items.append(collapsible_item)
                    _register_nav_item_callback(nav_item_id)
                else:
                    # Regular nav item
                    regular_item = nav.create_nav_item(
                        item["icon"], item["label"], href=item.get("href", "#"), active=False
                    )
                    section_items.append(regular_item)

            section_id = f"sidebar-section-{section_title.lower().replace(' ', '-')}"
            
            # Check if any top-level item has expanded=True to determine section expansion
            section_expanded = any(item.get("expanded", True) for item in top_level_items)
            
            rendered_section = nav.create_section(
                section_title,
                section_items,
                expanded=section_expanded,
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
            if item.get("type") == "collapsible":
                # Create collapsible nav item with children
                nav_item_id = f"nav-item-{item['label'].lower().replace(' ', '-')}"
                collapsible_item = nav.create_collapsible_nav_item(
                    item["icon"],
                    item["label"],
                    item.get("children", []),
                    expanded=item.get("expanded", False),
                    nav_item_id=nav_item_id,
                )
                rendered_nav_items.append(collapsible_item)
                _register_nav_item_callback(nav_item_id)
            else:
                # Regular nav item
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

        # In manual mode, wrap items that aren't already Li elements
        wrapped_nav_items = []
        for item in rendered_nav_items:
            if hasattr(item, 'type') and item.type == 'Li':
                # Already wrapped (collapsible items)
                wrapped_nav_items.append(item)
            else:
                # Regular items need wrapping
                wrapped_nav_items.append(html.Li(item, className="mb-px"))
        rendered_nav_items = wrapped_nav_items

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
