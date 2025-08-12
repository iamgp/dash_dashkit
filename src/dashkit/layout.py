from typing import Any

from dash import html

from .header import create_header
from .sidebar import create_sidebar


def create_layout(
    content: html.Div | None = None,
    sidebar_config: dict[str, Any] | None = None,
    header_config: dict[str, Any] | None = None,
) -> html.Div:
    """Create the main layout with configurable sidebar and header.

    Args:
        content: Main content to display
        sidebar_config: Configuration for sidebar with brand, nav_items, and sections
        header_config: Configuration for header with page_title, actions, etc.
    """
    if content is None:
        content = html.Div(
            [
                html.H2(
                    "Welcome to Dashkit-style Dashboard",
                    className="text-2xl font-semibold text-[#242529] dark:text-[#EEEFF1] mb-4",
                ),
                html.P("This is the main content area.", className="text-gray-600"),
            ],
            className="p-6",
        )

    # Default sidebar config
    if sidebar_config is None:
        sidebar_config = {
            "brand_name": "App",
            "brand_initial": "A",
            "nav_items": [],
            "sections": [],
        }

    # Default header config
    if header_config is None:
        header_config = {
            "page_title": "Dashboard",
            "page_icon": "📊",
            "search_placeholder": "Search...",
            "actions": None,
            "filter_items": None,
        }

    return html.Div(
        [
            # Sidebar
            create_sidebar(
                brand_name=sidebar_config["brand_name"],
                brand_initial=sidebar_config["brand_initial"],
                nav_items=sidebar_config["nav_items"],
                sections=sidebar_config["sections"],
            ),
            # Right side: navbar + content (full width minus sidebar)
            html.Div(
                [
                    # Header/navbar - spans full width of content area
                    create_header(
                        page_title=header_config["page_title"],
                        page_icon=header_config["page_icon"],
                        search_placeholder=header_config.get(
                            "search_placeholder", "Search..."
                        ),
                        actions=header_config.get("actions"),
                        filter_items=header_config.get("filter_items"),
                    ),
                    # Content with max-width constraint
                    html.Main(
                        [
                            html.Div(
                                [content],
                                style={
                                    "maxWidth": "calc(100vw - 16rem)",
                                    "width": "100%",
                                },
                                className="",
                            )
                        ],
                        className="flex-1 overflow-auto dark:bg-[#1B1D21]",
                    ),
                ],
                className="flex-1 flex flex-col",
            ),
        ],
        className="flex h-screen bg-white dark:bg-[#1B1D21] font-sans",
    )
