from dash import dcc, html
from .logo import BrandHeader
from .navigation import TopNavigationBar, FilterBar
from .buttons import PrimaryButton, SecondaryButton


def create_header():
    """Create the main header with two-tier structure using modular components."""
    # Create navigation instances
    top_nav = TopNavigationBar()
    filter_bar = FilterBar()
    
    # Top tier content
    left_content = BrandHeader("Companies", "📊")
    
    center_content = html.Div([
        html.I(className="fas fa-search absolute left-3 top-1/2 transform -translate-y-1/2 text-gray-400"),
        dcc.Input(
            placeholder="Search...",
            className="pl-10 pr-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent w-64",
        ),
    ], className="relative")
    
    right_content = [
        SecondaryButton("Import / Export", icon="fas fa-download", dropdown=True, className="mr-3"),
        PrimaryButton("New Company", icon="fas fa-plus"),
    ]
    
    # Filter tier content
    filter_content = [
        SecondaryButton("All Companies", icon="fas fa-building", dropdown=True, className="mr-3"),
        SecondaryButton("View settings", icon="fas fa-eye", dropdown=True, className="mr-3"),
        SecondaryButton("Sort", icon="fas fa-sort", className="mr-3"),
        SecondaryButton("Filter", icon="fas fa-filter"),
    ]
    
    return html.Div([
        # Top tier
        top_nav.render(left_content, center_content, right_content),
        
        # Bottom tier  
        filter_bar.render(filter_content),
    ])
