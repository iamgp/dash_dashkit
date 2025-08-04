from dash import html

from .header import create_header
from .sidebar import create_sidebar


def create_layout(content=None):
    """Create the main layout with sidebar and header."""
    if content is None:
        content = html.Div([
            html.H2("Welcome to Attio-style Dashboard", className="text-2xl font-semibold text-gray-900 mb-4"),
            html.P("This is the main content area.", className="text-gray-600"),
        ], className="p-6")

    return html.Div([
        # Sidebar
        create_sidebar(),

        # Right side: navbar + content (full width minus sidebar)
        html.Div([
            # Header/navbar - spans full width of content area
            create_header(),

            # Content with max-width constraint
            html.Main([
                html.Div([
                    content
                ], style={"maxWidth": "calc(100vw - 16rem)", "width": "100%"}, className="")
            ], className="flex-1 overflow-auto bg-gray-50"),

        ], className="flex-1 flex flex-col"),

    ], className="flex h-screen bg-white font-sans")
