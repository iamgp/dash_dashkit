from pathlib import Path

import dash
from dash import Dash, Input, Output, callback, clientside_callback, dcc, html

from dashkit import create_layout, setup_app
from dashkit.theme_manager import ThemeManager

# Import dashkit_shadcn components to register them with Dash
from dashkit_shadcn import AreaChart, BarChart, ChartContainer, ChartLegend, ChartTooltip  # Force registration

# Create dummy components to force Dash to register the library
_dummy_components = [
    AreaChart(id="dummy-area", data=[]),
    BarChart(id="dummy-bar", data=[]),
]

# External stylesheets including Font Awesome for icons
external_stylesheets = [
    "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css",
]

app = Dash(
    __name__,
    external_stylesheets=external_stylesheets,
    suppress_callback_exceptions=True,
    assets_folder=str(Path(__file__).parent.parent / "assets"),
    use_pages=True,
    pages_folder=str(Path(__file__).parent / "pages"),
)

# Configure the app with dashkit styling
setup_app(app)


# Configuration for the demo app
sidebar_config = {
    "brand_name": "Rhinoe",
    "brand_initial": "R",
}


app.layout = html.Div(
    [
        dcc.Store(id="page_header_config", data={}),
        dcc.Store(id="page_config", data={}),
        ThemeManager(),
        create_layout(
            content=dash.page_container,
            sidebar_config=sidebar_config,
            header_config={
                "page_title": "",
                "page_icon": "",
                "search_placeholder": "Search...",
                "actions": [],
                "filter_items": [],
            },
        ),
    ]
)


@callback(
    [
        Output("page_header_config", "data"),
        Output("page_config", "data"),
    ],
    Input("url", "pathname"),
)
def update_page_config(pathname):
    """Update page configuration based on current page."""
    header_config = {"title": "Dashboard", "icon": ""}
    page_config = {"content_padding": "p-8"}  # default padding
    
    for page in dash.page_registry.values():
        if page["path"] == pathname:
            header_config = {"title": page.get("title", ""), "icon": page.get("icon", "")}
            page_config = {
                "content_padding": page.get("content_padding", "p-8")
            }
            break
    
    return header_config, page_config


# Clientside callback to update content padding
clientside_callback(
    """
    function(page_config) {
        if (page_config && page_config.content_padding) {
            const element = document.getElementById('main-content-container');
            if (element) {
                // Remove existing padding classes
                element.className = element.className.replace(/p-\\d+|p-0/g, '');
                // Add new padding class
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


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Run the Dash app")
    _ = parser.add_argument(
        "--port", type=int, default=8050, help="Port to run the app on"
    )
    args = parser.parse_args()

    app.run(debug=True, port=args.port)
