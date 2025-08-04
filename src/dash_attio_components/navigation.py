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
        return IconButton(icon, label, active=active, href=href)

    def create_section(self, title, items, expanded=True):
        """Create a collapsible navigation section."""
        chevron = "fas fa-chevron-down" if expanded else "fas fa-chevron-right"

        section_items = [
            html.Div(
                [
                    html.I(className=f"{chevron} mr-2 text-xs text-gray-400"),
                    html.Span(title, className="text-sm font-medium text-gray-600"),
                ],
                className="flex items-center px-3 py-2 cursor-pointer hover:bg-gray-50 rounded-lg",
            )
        ]

        if expanded and items:
            if isinstance(items[0], str):  # Simple text items
                section_items.append(
                    html.Div(
                        [
                            html.Span(item, className="text-sm text-gray-400 px-3 py-2")
                            for item in items
                        ],
                        className="ml-4",
                    )
                )
            else:  # Navigation items
                section_items.append(html.Ul(items, className="ml-4 mt-1 space-y-1"))

        return html.Li(section_items, className="mb-2 ")

    def render(self, nav_items, sections=None):
        """Render sidebar navigation with items and sections."""
        all_items = []

        # Add main navigation items
        for item in nav_items:
            all_items.append(html.Li(item, className="mb-1"))

        # Add separator
        if sections:
            all_items.append(html.Li(html.Hr(className="my-3 border-gray-200")))

        # Add sections
        if sections:
            for section in sections:
                all_items.append(section)

        return html.Nav(
            [html.Ul(all_items, className="space-y-1 px-2")], className="flex-1 py-4"
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
            className=f"bg-white dark:bg-[#1E1E1E] border-b border-gray-200 dark:border-[#27282B] px-6 py-4 flex items-center justify-between {self.height}",
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
            className=f"bg-white dark:bg-[#1E1E1E] border-b border-gray-200 dark:border-[#27282B] px-6 py-3 flex items-center justify-between {self.height}",
        )
