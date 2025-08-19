from pathlib import Path

import dash
from dash import Dash, html, dcc, callback, Input, Output

from dashkit import create_layout, setup_app
from dashkit.theme_manager import ThemeManager

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
    Output("page_header_config", "data"),
    Input("url", "pathname")
)
def update_header(pathname):
    """Update header based on current page."""
    for page in dash.page_registry.values():
        if page["path"] == pathname:
            return {
                "title": page.get("title", ""),
                "icon": page.get("icon", "")
            }
    return {"title": "Dashboard", "icon": ""}


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Run the Dash app")
    _ = parser.add_argument(
        "--port", type=int, default=8050, help="Port to run the app on"
    )
    args = parser.parse_args()

    app.run(debug=True, port=args.port)
