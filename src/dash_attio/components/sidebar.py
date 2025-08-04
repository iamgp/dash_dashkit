from dash import html
from .logo import LogoSection
from .navigation import SidebarNavigation
from .buttons import PrimaryButton


def create_sidebar():
    """Create the main sidebar component using modular components."""
    # Create navigation instance
    nav = SidebarNavigation()
    
    # Main navigation items
    nav_items = [
        nav.create_nav_item("fas fa-bolt", "Quick actions"),
        nav.create_nav_item("fas fa-bell", "Notifications"),
        nav.create_nav_item("fas fa-tasks", "Tasks"),
        nav.create_nav_item("fas fa-sticky-note", "Notes"),
        nav.create_nav_item("fas fa-envelope", "Emails"),
        nav.create_nav_item("fas fa-phone", "Calls"),
        nav.create_nav_item("fas fa-chart-bar", "Reports"),
    ]
    
    # Create sections
    automations_section = nav.create_section("Automations", [
        html.Li(nav.create_nav_item("fas fa-list", "Sequences")),
        html.Li(nav.create_nav_item("fas fa-cogs", "Workflows")),
    ])
    
    favorites_section = nav.create_section("Favorites", ["No favorites"], expanded=True)
    
    records_section = nav.create_section("Records", [
        html.Li(nav.create_nav_item("fas fa-building", "Companies", active=True)),
        html.Li(nav.create_nav_item("fas fa-users", "People")),
    ])
    
    lists_section = nav.create_section("Lists", [
        html.Button([
            html.I(className="fas fa-plus mr-2"),
            "New list"
        ], className="text-sm text-blue-600 hover:text-blue-700 px-3 py-2 w-full text-left"),
    ])
    
    sections = [automations_section, favorites_section, records_section, lists_section]
    
    return html.Div([
        # Logo section
        LogoSection("Rhinoe", "R"),
        
        # Navigation
        nav.render(nav_items, sections),
        
    ], className="bg-white w-64 h-screen border-r border-gray-200 flex flex-col shrink-0")
