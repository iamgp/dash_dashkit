import sys
from pathlib import Path

# Add the src directory to the path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))

import dash
from dash import Dash, html

from dashkit import create_layout
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

# Serve custom CSS by embedding it in the index string
app.index_string = """
<!DOCTYPE html>
<html class="">
    <head>
        {%metas%}
        <title>{%title%}</title>
        {%favicon%}
        {%css%}
        <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css" rel="stylesheet">
        <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
        <link href="/assets/style.css" rel="stylesheet">
        <script>
            (function() {
                const storedTheme = localStorage.getItem('theme');
                if (storedTheme === 'dark') {
                    document.documentElement.classList.add('dark');
                } else {
                    document.documentElement.classList.remove('dark');
                }
            })();
        </script>
    </head>
    <body>
        {%app_entry%}
        <footer>
            {%config%}
            {%scripts%}
            {%renderer%}
        </footer>
    </body>
</html>
"""


# Configuration for the demo app
sidebar_config = {
    "brand_name": "Rhinoe",
    "brand_initial": "R",
    "nav_items": [
        {"icon": "fas fa-bolt", "label": "Quick actions"},
        {"icon": "fas fa-bell", "label": "Notifications"},
        {"icon": "fas fa-tasks", "label": "Tasks"},
        {"icon": "fas fa-sticky-note", "label": "Notes"},
        {"icon": "fas fa-envelope", "label": "Emails"},
        {"icon": "fas fa-phone", "label": "Calls"},
        {"icon": "fas fa-chart-bar", "label": "Reports"},
    ],
    "sections": [
        {
            "title": "Automations",
            "items": [
                {"type": "nav_item", "icon": "fas fa-list", "label": "Sequences"},
                {"type": "nav_item", "icon": "fas fa-cogs", "label": "Workflows"},
            ],
        },
        {"title": "Favorites", "items": ["No favorites"], "expanded": True},
        {
            "title": "Records",
            "items": [
                {
                    "type": "nav_item",
                    "icon": "fas fa-building",
                    "label": "Companies",
                    "href": "/",
                },
                {"type": "nav_item", "icon": "fas fa-users", "label": "People"},
            ],
        },
        {
            "title": "Lists",
            "items": [{"type": "button", "icon": "fas fa-plus", "label": "New list"}],
        },
    ],
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
