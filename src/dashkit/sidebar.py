from typing import Any

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

# Track registered callbacks to prevent duplicates
_registered_callbacks = set()


def _register_sidebar_collapse_callback():
    """Register a clientside callback for sidebar collapse functionality."""
    if "sidebar-collapse" in _registered_callbacks:
        return

    try:
        # Register callback for sidebar toggle
        clientside_callback(
            """
            function(n_clicks) {
                if (!n_clicks) return window.dash_clientside.no_update;

                const sidebar = document.querySelector('.sidebar-container');
                const mainContent = document.querySelector('.main-content-area');
                const headerToggle = document.getElementById('header-sidebar-toggle');
                const sidebarToggle = document.getElementById('sidebar-collapse-toggle');

                if (sidebar) {
                    const isCollapsed = sidebar.classList.contains('!hidden');

                    if (isCollapsed) {
                        // Show sidebar
                        sidebar.classList.remove('!hidden');
                        if (mainContent) {
                            mainContent.classList.remove('!ml-0');
                        }
                        if (headerToggle) {
                            headerToggle.classList.add('hidden');
                        }
                        if (sidebarToggle) {
                            sidebarToggle.classList.remove('hidden');
                        }
                    } else {
                        // Hide sidebar
                        sidebar.classList.add('!hidden');
                        if (mainContent) {
                            mainContent.classList.add('!ml-0');
                        }
                        if (headerToggle) {
                            headerToggle.classList.remove('hidden');
                        }
                        if (sidebarToggle) {
                            sidebarToggle.classList.add('hidden');
                        }
                    }
                }

                return window.dash_clientside.no_update;
            }
            """,
            Output("sidebar-collapse-toggle", "n_clicks", allow_duplicate=True),
            Input("sidebar-collapse-toggle", "n_clicks"),
            prevent_initial_call=True,
        )

        _registered_callbacks.add("sidebar-collapse")
    except Exception:
        # Callback might already be registered, skip silently
        pass


def _register_header_toggle_callback():
    """Register a clientside callback for header sidebar toggle functionality."""
    if "header-toggle" in _registered_callbacks:
        return

    try:
        # Register callback for header toggle
        clientside_callback(
            """
            function(n_clicks) {
                if (!n_clicks) return window.dash_clientside.no_update;

                const sidebar = document.querySelector('.sidebar-container');
                const mainContent = document.querySelector('.main-content-area');
                const headerToggle = document.getElementById('header-sidebar-toggle');
                const sidebarToggle = document.getElementById('sidebar-collapse-toggle');

                if (sidebar) {
                    // When header toggle is clicked, always show sidebar (it's only visible when collapsed)
                    sidebar.classList.remove('!hidden');
                    if (mainContent) {
                        mainContent.classList.remove('!ml-0');
                    }
                    if (headerToggle) {
                        headerToggle.classList.add('hidden');
                    }
                    if (sidebarToggle) {
                        sidebarToggle.classList.remove('hidden');
                    }
                }

                return window.dash_clientside.no_update;
            }
            """,
            Output("header-sidebar-toggle", "n_clicks", allow_duplicate=True),
            Input("header-sidebar-toggle", "n_clicks"),
            prevent_initial_call=True,
        )

        _registered_callbacks.add("header-toggle")
    except Exception:
        # Callback might already be registered, skip silently
        pass


def _register_section_callback(section_id: str):
    """Register a clientside callback for section toggle functionality."""
    # Skip if already registered
    if section_id in _registered_callbacks:
        return

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
        # Mark as registered
        _registered_callbacks.add(section_id)
    except Exception:
        # Callback might already be registered, skip silently
        pass


def _register_nav_item_callback(nav_item_id: str):
    """Register a clientside callback for nav item toggle functionality."""
    # Skip if already registered
    if nav_item_id in _registered_callbacks:
        return

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
        # Mark as registered
        _registered_callbacks.add(nav_item_id)
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
    include_location: bool = False,
) -> html.Div:
    """Create a reusable sidebar component.

    The sidebar is built dynamically from Dash's page registry using folder structure.
    Navigation hierarchy is automatically inferred from the file path:

    - pages/section/page.py → section="SECTION"
    - pages/section/container/page.py → section="SECTION", parent="Container"

    Supported register_page parameters:
    - ``sidebar_visible``: bool include page in sidebar (default: True)
    - ``sidebar_expanded``: bool expand containers by default (default: True)
    - ``sidebar_order``: int order within section (fallback to ``order`` or 0)
    - ``icon``: string icon name for MynaUI icons (e.g., "chart-line")

    Args:
        brand_name: The brand/company name for the logo
        brand_initial: Initial letter for the logo
        include_location: When True, include dcc.Location component (set to False if you have one already)
    """

    # Create navigation instance
    nav = SidebarNavigation()

    # Generate navigation from page registry using folder structure
    # First pass: collect all pages and organize by section and parent
    pages_by_section: dict[str, list[dict[str, Any]]] = {}
    all_pages: dict[str, dict[str, Any]] = {}

    for _page in page_registry.values():
        # visibility
        if _page.get("sidebar_visible", True) is False:
            continue

        # Extract hierarchy from module path if not explicitly set
        module_path = _page.get("module", "")
        path_parts = module_path.split(".")

        # Auto-infer section and parent from folder structure
        # Example: "dashkit_demo.pages.pcr.duplex.analysis" -> section="PCR", parent="Duplex"
        if "pages" in path_parts:
            pages_index = path_parts.index("pages")
            folder_parts = path_parts[pages_index + 1 :]  # Get parts after "pages"

            # Default values
            auto_section = "Main"
            auto_parent = None

            if len(folder_parts) >= 2:  # e.g., ["pcr", "analysis"]
                auto_section = folder_parts[0].upper()  # "pcr" -> "PCR"

            if len(folder_parts) >= 3:  # e.g., ["pcr", "duplex", "analysis"]
                auto_parent = folder_parts[-2].title()  # "duplex" -> "Duplex"

            # Use auto-inferred values if not explicitly set
            section_name = _page.get("sidebar_section", auto_section)
            parent_name = _page.get("sidebar_parent", auto_parent)
        else:
            # Fallback to explicit or default values
            section_name = _page.get("sidebar_section", "Main")
            parent_name = _page.get("sidebar_parent")

        expanded: bool = _page.get("sidebar_expanded", True)
        order = _page.get("sidebar_order", _page.get("order", 0))
        is_collapsible = _page.get("sidebar_collapsible", False)
        is_container_only = _page.get("sidebar_container_only", False)

        # Compose page info
        icon_value = _page.get("icon", "circle")

        page_type = "virtual_container" if is_container_only else "nav_item"
        page_href = None if is_container_only else _page.get("path")

        # Create unique label for dictionary key to avoid conflicts
        base_label = _page.get("name") or _page.get("title") or _page.get("path")
        unique_key = f"{section_name}::{parent_name or 'root'}::{base_label}"

        page_info = {
            "type": page_type,
            "icon": icon_value,
            "label": base_label,  # Keep original label for display
            "href": page_href,
            "order": order,
            "section": section_name,
            "parent": parent_name,
            "expanded": expanded,
            "collapsible": is_collapsible
            or is_container_only,  # Containers are always collapsible
            "children": [],
        }

        all_pages[unique_key] = page_info

        # Group by section
        if section_name not in pages_by_section:
            pages_by_section[section_name] = []
        pages_by_section[section_name].append(page_info)

    # Auto-create missing parent containers based on folder structure
    missing_containers = set()
    for page_info in all_pages.values():
        if page_info["parent"]:
            # Check if parent container exists as a virtual container in same section
            parent_exists = False
            for _existing_key, existing_page in all_pages.items():
                if (
                    existing_page["label"] == page_info["parent"]
                    and existing_page["section"] == page_info["section"]
                ):
                    parent_exists = True
                    break

            if not parent_exists:
                missing_containers.add((page_info["parent"], page_info["section"]))

    for container_name, section_name in missing_containers:
        # Try to load container config from __init__.py file
        container_config = {}

        # Look for container config in registered pages' modules
        for _page in page_registry.values():
            module_path = _page.get("module", "")
            path_parts = module_path.split(".")

            # Check if this page is in the container folder
            if "pages" in path_parts:
                pages_index = path_parts.index("pages")
                folder_parts = path_parts[pages_index + 1 :]

                # If this page is in the container we're looking for
                if (
                    len(folder_parts) >= 3
                    and folder_parts[-2].title() == container_name
                ):
                    # Try to import the container's __init__.py
                    try:
                        container_module_path = ".".join(
                            path_parts[:-1]
                        )  # Remove the page file name
                        container_module = __import__(
                            container_module_path, fromlist=["CONTAINER_CONFIG"]
                        )
                        if hasattr(container_module, "CONTAINER_CONFIG"):
                            container_config = container_module.CONTAINER_CONFIG
                            break
                    except (ImportError, AttributeError):
                        pass

        # Use config values or defaults
        container_icon = container_config.get("icon", "folder")
        container_expanded = container_config.get("expanded", True)
        container_order = container_config.get("order", 0)

        container_info = {
            "type": "virtual_container",
            "icon": container_icon,
            "label": container_name,
            "href": None,
            "order": container_order,
            "section": section_name,
            "parent": None,  # Auto-created containers are top-level in their section
            "expanded": container_expanded,
            "collapsible": True,
            "children": [],
        }

        all_pages[container_name] = container_info

        if section_name not in pages_by_section:
            pages_by_section[section_name] = []
        pages_by_section[section_name].append(container_info)

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

    # Get section order by looking for CONTAINER_CONFIG in section folders
    section_orders = {}
    for section_title in pages_by_section.keys():
        section_order = 999  # Default high order

        # Handle Main section specially (pages directly in pages/ folder)
        if section_title == "Main":
            try:
                # Try to load config from pages/__init__.py
                for _page in page_registry.values():
                    module_path = _page.get("module", "")
                    path_parts = module_path.split(".")

                    if "pages" in path_parts:
                        pages_index = path_parts.index("pages")
                        folder_parts = path_parts[pages_index + 1 :]

                        # If this is a page directly in pages/ (main section)
                        if (
                            len(folder_parts) == 1
                        ):  # e.g. ["companies"] not ["pcr", "analysis"]
                            main_module_path = ".".join(
                                path_parts[: pages_index + 1]
                            )  # Just "pages"
                            main_module = __import__(
                                main_module_path, fromlist=["CONTAINER_CONFIG"]
                            )
                            if hasattr(main_module, "CONTAINER_CONFIG"):
                                main_config = main_module.CONTAINER_CONFIG
                                section_order = main_config.get("order", 999)
                                break
            except (ImportError, AttributeError):
                pass
        else:
            # Try to find a page in this section to get the section folder path
            for _page in page_registry.values():
                module_path = _page.get("module", "")
                path_parts = module_path.split(".")

                if "pages" in path_parts:
                    pages_index = path_parts.index("pages")
                    folder_parts = path_parts[pages_index + 1 :]

                    # If this page is in the current section
                    if len(folder_parts) >= 1:
                        auto_section = folder_parts[0].upper()
                        if auto_section == section_title:
                            # Try to load section config from folder's __init__.py
                            try:
                                section_module_path = ".".join(
                                    path_parts[: pages_index + 2]
                                )  # Include pages.section
                                section_module = __import__(
                                    section_module_path, fromlist=["CONTAINER_CONFIG"]
                                )
                                if hasattr(section_module, "CONTAINER_CONFIG"):
                                    section_config = section_module.CONTAINER_CONFIG
                                    section_order = section_config.get("order", 999)
                                    break
                            except (ImportError, AttributeError):
                                pass

        section_orders[section_title] = section_order

    # Sort sections by order, then alphabetically
    def _section_sort_key(item):
        section_title, pages = item
        return (section_orders.get(section_title, 999), section_title)

    for section_title, pages in sorted(pages_by_section.items(), key=_section_sort_key):
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
        def _sort_key(it: dict[str, Any]) -> tuple[int, str]:
            return (_safe_order(it.get("order")), str(it.get("label", "")))

        top_level_items.sort(key=_sort_key)

        section_items = []
        for item in top_level_items:
            if item["children"] or item.get("type") == "virtual_container":
                # Create collapsible nav item (for both regular items with children and virtual containers)
                children_data = []

                def _child_sort_key(c: dict[str, Any]) -> tuple[int, str]:
                    return (_safe_order(c.get("order")), str(c.get("label", "")))

                for child in sorted(item["children"], key=_child_sort_key):
                    children_data.append(
                        {
                            "icon": child["icon"],
                            "label": child["label"],
                            "href": child["href"],
                            "active": False,
                        }
                    )

                nav_item_id = f"nav-item-{item['label'].lower().replace(' ', '-')}"

                # For virtual containers, we don't provide an href (non-clickable)
                if item.get("type") == "virtual_container":
                    collapsible_item = nav.create_collapsible_nav_item(
                        item["icon"],
                        item["label"],
                        children_data,
                        expanded=item["expanded"],
                        nav_item_id=nav_item_id,
                        href=None,  # Virtual containers are not clickable
                    )
                else:
                    collapsible_item = nav.create_collapsible_nav_item(
                        item["icon"],
                        item["label"],
                        children_data,
                        expanded=item["expanded"],
                        nav_item_id=nav_item_id,
                        href=item.get("href"),
                    )

                section_items.append(collapsible_item)
                _register_nav_item_callback(nav_item_id)
            else:
                # Regular nav item
                regular_item = nav.create_nav_item(
                    item["icon"],
                    item["label"],
                    href=item.get("href", "#"),
                    active=False,
                )
                section_items.append(regular_item)

        section_id = f"sidebar-section-{section_title.lower().replace(' ', '-')}"

        # Check if any top-level item has expanded=True to determine section expansion
        section_expanded = any(item.get("expanded", True) for item in top_level_items)

        # For "Main" section, add items directly without section header
        if section_title.lower() == "main":
            rendered_sections.extend(section_items)
            # Add spacer after main section items
            if section_items:
                rendered_sections.append(html.Li(html.Div(className="h-3")))
        else:
            rendered_section = nav.create_section(
                section_title,
                section_items,
                expanded=section_expanded,
                section_id=section_id,
            )
            rendered_sections.append(rendered_section)
            # Add spacer after each section
            rendered_sections.append(html.Li(html.Div(className="h-3")))
            _register_section_callback(section_id)

    sidebar_content = html.Div(
        [
            LogoSection(brand_name, brand_initial),
            # Navigation sections from folder structure
            SidebarNavigation().render([], rendered_sections),
            # Resize handle
            html.Div(
                id="sidebar-resize-handle",
                className="absolute top-0 right-0 h-full cursor-col-resize hover:bg-blue-400 transition-all duration-150 bg-transparent z-50",
                style={"right": "-1px", "width": "2px"},
            ),
        ],
        id="sidebar-container",
        className="sidebar-container relative bg-dashkit-panel-light dark:bg-dashkit-panel-dark w-[var(--dashkit-sidebar-width)] h-screen border-r border-dashkit-border-light dark:border-dashkit-border-dark flex flex-col shrink-0 select-none",
        style={"position": "relative"},
    )

    # Register the sidebar collapse callbacks
    _register_sidebar_collapse_callback()
    _register_header_toggle_callback()

    # Register resize callback using URL as trigger
    try:
        url_id = "sidebar-url" if include_location else "url"
        clientside_callback(
            """
            function(pathname) {
                // Load saved width immediately and add transition class after
                const sidebar = document.getElementById('sidebar-container');
                if (sidebar) {
                    const savedWidth = localStorage.getItem('dashkit-sidebar-width');
                    if (savedWidth) {
                        document.documentElement.style.setProperty('--dashkit-sidebar-width', savedWidth);
                    }
                    // Add transition class after width is set
                    setTimeout(function() {
                        sidebar.classList.add('transition-all', 'duration-200');
                    }, 50);
                }

                // Only setup resize on first load to avoid duplicate setup
                if (window.sidebarResizeSetup) {
                    return window.dash_clientside.no_update;
                }

                setTimeout(function() {
                    const resizeHandle = document.getElementById('sidebar-resize-handle');
                    const sidebar = document.querySelector('.sidebar-container');

                    if (!resizeHandle || !sidebar) {
                        console.log('Resize elements not found, retrying...');
                        setTimeout(arguments.callee, 100);
                        return;
                    }

                    window.sidebarResizeSetup = true;
                    console.log('Setting up sidebar resize functionality');

                    let isResizing = false;
                    let startX = 0;
                    let startWidth = 0;

                    resizeHandle.onmousedown = function(e) {
                        console.log('Sidebar resize started');
                        isResizing = true;
                        startX = e.clientX;
                        startWidth = sidebar.offsetWidth;
                        document.body.style.cursor = 'col-resize';
                        document.body.style.userSelect = 'none';
                        e.preventDefault();
                        return false;
                    };

                    document.onmousemove = function(e) {
                        if (!isResizing) return;

                        const deltaX = e.clientX - startX;
                        const newWidth = Math.max(120, Math.min(600, startWidth + deltaX));
                        const newWidthRem = newWidth / 16;

                        document.documentElement.style.setProperty('--dashkit-sidebar-width', newWidthRem + 'rem');
                        return false;
                    };

                    document.onmouseup = function() {
                        if (isResizing) {
                            console.log('Sidebar resize completed');
                            isResizing = false;
                            document.body.style.cursor = '';
                            document.body.style.userSelect = '';

                            const currentWidth = getComputedStyle(document.documentElement).getPropertyValue('--dashkit-sidebar-width');
                            localStorage.setItem('dashkit-sidebar-width', currentWidth);
                        }
                    };

                    console.log('Sidebar resize ready');
                }, 200);

                return window.dash_clientside.no_update;
            }
            """,
            Output("sidebar-resize-handle", "n_clicks", allow_duplicate=True),
            Input(url_id, "pathname"),
            prevent_initial_call=True,
        )
    except Exception as e:
        print(f"Error setting up resize: {e}")

    # Register callback to handle active states
    if include_location:
        url_id = "sidebar-url"
        _register_active_state_callback(url_id)
        return html.Div([dcc.Location(id=url_id, refresh=False), sidebar_content])
    else:
        _register_active_state_callback("url")
        return sidebar_content
