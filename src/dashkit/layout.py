from typing import Any

import dash
import dash_mantine_components as dmc
from dash import Input, Output, callback, clientside_callback, dcc, html

from .header import create_header
from .sidebar import create_sidebar
from .theme_manager import ThemeManager


def create_layout(
    content: html.Div | None = None,
    sidebar_config: dict[str, Any] | None = None,
    header_config: dict[str, Any] | None = None,
    content_padding: str = "p-8",
    include_theme_manager: bool = True,
) -> html.Div:
    """Create the main layout with configurable sidebar and header.

    Args:
        content: Main content to display
        sidebar_config: Configuration for sidebar with brand name and initial
        header_config: Configuration for header with page_title, actions, etc.
        content_padding: CSS class for content padding (default: "p-8")
        include_theme_manager: When True, injects ThemeManager (Location + theme stores/callbacks)
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
                # Theme and location management
                ThemeManager() if include_theme_manager else None,
                # Global page stores for header + page config
                dcc.Store(id="page_header_config", data={}),
                dcc.Store(id="page_config", data={}),
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


# Register page state callbacks at import time so apps don't need to define them
@callback(
    [
        Output("page_header_config", "data"),
        Output("page_config", "data"),
    ],
    Input("url", "pathname", allow_optional=True),
)
def _update_page_config(pathname: str | None):
    """Update header + page config stores from Dash page registry.

    This runs whenever the URL changes. If `url` isn't present, it will be
    skipped due to allow_optional.
    """
    header_config = {"title": "Dashboard", "icon": ""}
    page_config = {"content_padding": "p-8"}

    if pathname:
        for page in dash.page_registry.values():
            if page.get("path") == pathname:
                header_config = {
                    "title": page.get("title", ""),
                    "icon": page.get("icon", ""),
                }
                page_config = {"content_padding": page.get("content_padding", "p-8")}
                break

    return header_config, page_config


# Clientside callback to apply content padding class to main content container
clientside_callback(
    r"""
    function(page_config) {
        if (page_config && page_config.content_padding) {
            const element = document.getElementById('main-content-container');
            if (element) {
                element.className = element.className.replace(/p-\d+|p-0/g, '');
                element.className = element.className + ' ' + page_config.content_padding;
            }
        }
        return window.dash_clientside.no_update;
    }
    """,
    Output("main-content-container", "className"),
    Input("page_config", "data"),
    prevent_initial_call=False,
)
