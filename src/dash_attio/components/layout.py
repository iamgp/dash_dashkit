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
        
        # Main content area
        html.Div([
            # Header
            create_header(),
            
            # Content
            html.Main([
                content
            ], className="flex-1 overflow-auto bg-gray-50"),
            
        ], className="flex-1 flex flex-col min-h-screen"),
        
    ], className="flex h-screen bg-white font-sans")
