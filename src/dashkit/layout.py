from typing import Any

import dash_mantine_components as dmc
from dash import html

from .header import create_header
from .sidebar import create_sidebar


def create_layout(
    content: html.Div | None = None,
    sidebar_config: dict[str, Any] | None = None,
    header_config: dict[str, Any] | None = None,
    content_padding: str = "p-8",
) -> html.Div:
    """Create the main layout with configurable sidebar and header.

    Args:
        content: Main content to display
        sidebar_config: Configuration for sidebar with brand name and initial
        header_config: Configuration for header with page_title, actions, etc.
        content_padding: CSS class for content padding (default: "p-8")
    """
    if content is None:
        content = html.Div(
            [
                html.H2(
                    "Welcome to Dashkit-style Dashboard",
                    className="text-2xl font-semibold text-dashkit-text dark:text-dashkit-text-invert mb-4",
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

    return dmc.MantineProvider(
        html.Div(
            [
                # Sidebar
                create_sidebar(
                    brand_name=sidebar_config["brand_name"],
                    brand_initial=sidebar_config["brand_initial"],
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
                                    id="main-content-container",
                                    style={
                                        "maxWidth": "calc(100vw - var(--dashkit-sidebar-width))",
                                        "width": "100%",
                                    },
                                    className=f"dark:text-white {content_padding} prose prose-sm dark:prose-invert",
                                )
                            ],
                            className="flex-1 overflow-auto dark:bg-dashkit-surface ",
                        ),
                    ],
                    className="main-content-area flex-1 flex flex-col",
                ),
            ],
            className="flex h-screen bg-white dark:bg-dashkit-surface font-sans",
        )
    )
