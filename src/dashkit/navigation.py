import dash_iconify
from dash import html

from .buttons import IconButton


class BaseNavigationBar:
    """Base class for navigation bars with common styling."""

    def __init__(self, className="", style=None):
        self.className = className
        self.style = style or {}

    def render_item(self, item):
        """Override in subclasses to customize item rendering."""
        return item

    def render(self, items):
        """Render the navigation bar with items."""
        return html.Nav(
            [
                html.Ul(
                    [html.Li(self.render_item(item)) for item in items],
                    className="space-y-1 px-2",
                )
            ],
            className=f"flex-1 py-4 {self.className}",
            style=self.style,
        )


class SidebarNavigation(BaseNavigationBar):
    """Sidebar navigation with collapsible sections."""

    def __init__(self):
        super().__init__()

    def create_nav_item(self, icon, label, href="#", active=False):
        """Create a sidebar navigation item."""
        return html.Li(
            IconButton(icon, label, active=active, href=href), className="mb-px"
        )

    def create_collapsible_nav_item(
        self, icon, label, children, expanded=False, nav_item_id=None, href=None
    ):
        """Create a collapsible navigation item with children."""
        if nav_item_id is None:
            nav_item_id = f"nav-item-{label.lower().replace(' ', '-')}"

        chevron_id = f"{nav_item_id}-chevron"
        content_id = f"{nav_item_id}-content"
        toggle_id = f"{nav_item_id}-toggle"

        chevron = "chevron-down" if expanded else "chevron-right"

        # Main nav item with toggle functionality
        main_item = html.Div(
            [
                html.Div(
                    [
                        dash_iconify.DashIconify(
                            icon=icon if ":" in icon else f"mynaui:{icon}",
                            width=16,
                            className="mr-2 text-dashkit-icon-light dark:text-dashkit-icon-dark align-middle inline-block w-4 h-4 shrink-0",
                        ),
                        html.Span(
                            label,
                            className="opacity-100 transition-all duration-200 flex-1",
                        ),
                        dash_iconify.DashIconify(
                            icon=f"mynaui:{chevron}",
                            width=16,
                            className="ml-auto text-dashkit-icon-light dark:text-dashkit-icon-dark transition-transform duration-200 align-middle inline-block w-4 h-4 shrink-0",
                            id=chevron_id,
                        ),
                    ],
                    className="sidebar-item flex items-center px-2 py-1 text-sm font-medium rounded-lg hover:bg-dashkit-hover-light transition-colors duration-150 dark:hover:bg-dashkit-hover-dark text-dashkit-text dark:text-dashkit-text-invert cursor-pointer break-words truncate mb-px tracking-sidebar",
                    id=toggle_id,
                )
            ],
            className="mb-px",
        )

        # Children container with proper indentation and connecting lines
        children_items = []
        for i, child in enumerate(children):
            if isinstance(child, dict):
                is_last = i == len(children) - 1

                # Create the connecting line structure
                line_container = html.Div(
                    [
                        # Vertical line - show for all items with adequate height
                        html.Div(
                            className=f"absolute left-2 top-0 w-px bg-dashkit-connector-light dark:bg-dashkit-connector-dark {'h-full' if is_last else 'h-full'}"
                        ),
                        # The actual nav item
                        html.Div(
                            IconButton(
                                child["icon"],
                                child["label"],
                                href=child.get("href", "#"),
                                active=child.get("active", False),
                            ),
                            className="ml-4",
                        ),
                    ],
                    className="relative",
                )

                children_items.append(line_container)

        children_container = html.Ul(
            children_items,
            id=content_id,
            className=f"ml-2 space-y-0 {'block' if expanded else 'hidden'}",
        )

        return html.Li([main_item, children_container], className="", id=nav_item_id)

    def create_section(self, title, items, expanded=True, section_id=None):
        """Create a collapsible navigation section."""
        if section_id is None:
            section_id = f"sidebar-section-{title.lower().replace(' ', '-')}"

        chevron_id = f"{section_id}-chevron"
        content_id = f"{section_id}-content"
        toggle_id = f"{section_id}-toggle"

        chevron = "chevron-down" if expanded else "chevron-right"

        # Header with toggle functionality
        header = html.Div(
            [
                dash_iconify.DashIconify(
                    icon=f"mynaui:{chevron}",
                    width=16,
                    className="mr-2 text-dashkit-icon-light dark:text-dashkit-icon-dark transition-transform duration-200 align-middle inline-block w-4 h-4 shrink-0",
                    id=chevron_id,
                ),
                html.Span(
                    title,
                    className="opacity-100 transition-all duration-200 text-sm font-medium text-gray-600 dark:text-gray-300",
                ),
            ],
            id=toggle_id,
            className="flex items-center pr-3 pl-2 py-2 cursor-pointer hover:bg-dashkit-hover-light dark:hover:bg-dashkit-hover-dark rounded-lg",
        )

        # Content container that will be shown/hidden
        content_items = []
        if items:
            if isinstance(items[0], str):  # Simple text items
                content_items = [
                    html.Div(
                        item,
                        className="text-sm text-gray-400 dark:text-gray-500 pr-3 pl-1 py-1",
                    )
                    for item in items
                ]
            else:  # Navigation items
                content_items = items

        content = html.Ul(
            content_items if content_items else [],
            id=content_id,
            className=f"mt-px space-y-px {'block' if expanded else 'hidden'}",
        )

        return html.Li([header, content], className="", id=section_id)

    def render(self, nav_items, sections=None):
        """Render sidebar navigation with items and sections."""
        all_items = []

        # Add main navigation items
        for item in nav_items:
            all_items.append(html.Li(item, className="mb-px"))

        # Add sections
        if sections:
            for section in sections:
                all_items.append(section)

        return html.Nav(
            [html.Ul(all_items, className="space-y-px px-1")], className="flex-1 py-2"
        )


class TopNavigationBar(BaseNavigationBar):
    """Top navigation bar for main header."""

    def __init__(self, height="h-12"):
        self.height = height
        super().__init__()

    def render(self, left_content, center_content=None, right_content=None):
        """Render top navigation with left, center, right sections."""
        return html.Div(
            [
                # Left content
                html.Div(left_content, className="flex items-center"),
                # Center content
                html.Div(
                    center_content or [],
                    className="flex items-center flex-1 justify-center",
                ),
                # Right content
                html.Div(right_content or [], className="flex items-center"),
            ],
            className=f"bg-white dark:bg-dashkit-surface border-b border-gray-200 dark:border-dashkit-border-dark px-8 py-4 flex items-center justify-between {self.height}",
        )


class FilterBar(BaseNavigationBar):
    """Filter/action bar for secondary navigation."""

    def __init__(self, height="h-14"):
        self.height = height
        super().__init__()

    def render(self, left_content, right_content=None):
        """Render filter bar with left and right sections."""
        return html.Div(
            [
                # Left content
                html.Div(left_content, className="flex items-center"),
                # Right content
                html.Div(right_content or [], className="flex items-center"),
            ],
            className=f"bg-white dark:bg-dashkit-surface border-b border-gray-200 dark:border-dashkit-border-dark px-8 py-3 flex items-center justify-between {self.height}",
        )
