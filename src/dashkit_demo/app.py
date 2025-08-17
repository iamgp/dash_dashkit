import sys
from pathlib import Path

# Add the src directory to the path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))

import dash
from dash import Dash, html

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
        ThemeManager(),
        create_layout(
            content=dash.page_container,
            sidebar_config=sidebar_config,
            header_config={
                "page_title": "",  # Will be set by individual pages
                "page_icon": "",
                "search_placeholder": "Search...",
                "actions": [],
                "filter_items": [],
            },
            use_pages=True,
        ),
    ]
)


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Run the Dash app")
    _ = parser.add_argument(
        "--port", type=int, default=8050, help="Port to run the app on"
    )
    args = parser.parse_args()

    app.run(debug=True, port=args.port)
