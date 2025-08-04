import sys
from pathlib import Path

# Add the src directory to the path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))

from dash import Dash

from dash_attio_components import AttioTable, create_layout
from dash_attio_components.table import create_company_columns, format_company_data

# External stylesheets including Font Awesome for icons
external_stylesheets = [
    "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css",
]

app = Dash(__name__, external_stylesheets=external_stylesheets)

# Serve custom CSS by embedding it in the index string
app.index_string = (
    """
<!DOCTYPE html>
<html>
    <head>
        {%metas%}
        <title>{%title%}</title>
        {%favicon%}
        {%css%}
        <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css" rel="stylesheet">
        <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
        <style>
            """
    + open(Path(__file__).parent.parent / "assets/style.css").read()
    + """
        </style>
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
)

# Sample company data with proper Attio-style formatting
companies_data = [
    {
        "name": "United Airlines",
        "icon": "🛫",
        "categories": [
            {"name": "Airlines", "color": "#FEF3C7"},
            {"name": "B2C", "color": "#DBEAFE"},
            {"name": "E-commerce", "color": "#FED7C3"},
            {"name": "Transport", "color": "#FEF3C7"},
        ],
        "linkedin": "united-airlines",
        "last_interaction": "No communication",
        "connection_strength": "",
        "twitter_followers": 1174209,
        "twitter_handle": "united",
    },
    {
        "name": "Airbnb",
        "icon": "🏠",
        "categories": [
            {"name": "B2C", "color": "#DBEAFE"},
            {"name": "Information", "color": "#FEF3C7"},
            {"name": "Internet", "color": "#FED7C3"},
            {"name": "Marketplace", "color": "#D1FAE5"},
        ],
        "linkedin": "airbnb",
        "last_interaction": "No communication",
        "connection_strength": "",
        "twitter_followers": 883549,
        "twitter_handle": "Airbnb",
    },
    {
        "name": "Attio",
        "icon": "⚡",
        "categories": [
            {"name": "Automation", "color": "#FEE2E2"},
            {"name": "B2B", "color": "#DBEAFE"},
            {"name": "Enterprise", "color": "#E0E7FF"},
            {"name": "Information", "color": "#FEF3C7"},
        ],
        "linkedin": "attio",
        "last_interaction": "No communication",
        "connection_strength": "",
        "twitter_followers": 1340,
        "twitter_handle": "attio",
    },
    {
        "name": "Google",
        "icon": "🌐",
        "categories": [
            {"name": "B2B", "color": "#DBEAFE"},
            {"name": "B2C", "color": "#DBEAFE"},
            {"name": "Broadcasting", "color": "#E0E7FF"},
            {"name": "Information", "color": "#FEF3C7"},
        ],
        "linkedin": "google",
        "last_interaction": "No communication",
        "connection_strength": "",
        "twitter_followers": 28946065,
        "twitter_handle": "Google",
    },
    {
        "name": "Microsoft",
        "icon": "🖥️",
        "categories": [
            {"name": "B2B", "color": "#DBEAFE"},
            {"name": "Enterprise", "color": "#E0E7FF"},
            {"name": "Information", "color": "#FEF3C7"},
            {"name": "Publishing", "color": "#FCE7F3"},
        ],
        "linkedin": "microsoft",
        "last_interaction": "No communication",
        "connection_strength": "",
        "twitter_followers": 12814907,
        "twitter_handle": "Microsoft",
    },
    {
        "name": "PayPal",
        "icon": "💳",
        "categories": [
            {"name": "B2C", "color": "#DBEAFE"},
            {"name": "Finance", "color": "#FED7C3"},
            {"name": "Financial services", "color": "#FEF3C7"},
            {"name": "Information", "color": "#FEF3C7"},
        ],
        "linkedin": "paypal",
        "last_interaction": "No communication",
        "connection_strength": "",
        "twitter_followers": 1800000,
        "twitter_handle": "PayPal",
    },
    {
        "name": "Disney",
        "icon": "🏰",
        "categories": [
            {"name": "B2C", "color": "#DBEAFE"},
            {"name": "Entertainment & Recreation", "color": "#FCE7F3"},
        ],
        "linkedin": "the-walt-disney-company",
        "last_interaction": "No communication",
        "connection_strength": "",
        "twitter_followers": 14500000,
        "twitter_handle": "Disney",
    },
    {
        "name": "Intercom",
        "icon": "💬",
        "categories": [
            {"name": "B2B", "color": "#DBEAFE"},
            {"name": "Information", "color": "#FEF3C7"},
            {"name": "Publishing", "color": "#FCE7F3"},
            {"name": "SAAS", "color": "#D1FAE5"},
        ],
        "linkedin": "intercom",
        "last_interaction": "No communication",
        "connection_strength": "",
        "twitter_followers": 82000,
        "twitter_handle": "intercom",
    },
    {
        "name": "Apple",
        "icon": "🍎",
        "categories": [
            {"name": "B2C", "color": "#DBEAFE"},
            {"name": "Computer Hardware", "color": "#FEF3C7"},
            {"name": "Consumer Electronics", "color": "#FED7C3"},
            {"name": "Consumer Goods", "color": "#FED7C3"},
        ],
        "linkedin": "apple",
        "last_interaction": "No communication",
        "connection_strength": "",
        "twitter_followers": 9000000,
        "twitter_handle": "Apple",
    },
    {
        "name": "LVMH",
        "icon": "👜",
        "categories": [
            {"name": "B2C", "color": "#DBEAFE"},
            {"name": "Consumer Discretionary", "color": "#E0E7FF"},
            {"name": "E-commerce", "color": "#FED7C3"},
        ],
        "linkedin": "lvmh",
        "last_interaction": "No communication",
        "connection_strength": "",
        "twitter_followers": 420000,
        "twitter_handle": "LVMH",
    },
]

# Format data and create table
table_data = format_company_data(companies_data)
columns = create_company_columns()

# Create the content using just the table component without stats header
example_content = AttioTable(data=table_data, columns=columns, height=600)

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
            ]
        },
        {
            "title": "Favorites",
            "items": ["No favorites"],
            "expanded": True
        },
        {
            "title": "Records",
            "items": [
                {"type": "nav_item", "icon": "fas fa-building", "label": "Companies", "active": True},
                {"type": "nav_item", "icon": "fas fa-users", "label": "People"},
            ]
        },
        {
            "title": "Lists",
            "items": [
                {"type": "button", "icon": "fas fa-plus", "label": "New list"}
            ]
        }
    ]
}

header_config = {
    "page_title": "Companies",
    "page_icon": "📊",
    "search_placeholder": "Search...",
    "actions": [
        {"type": "secondary", "label": "Import / Export", "icon": "fas fa-download", "dropdown": True, "className": "mr-3"},
        {"type": "primary", "label": "New Company", "icon": "fas fa-plus"},
    ],
    "filter_items": [
        {"label": "All Companies", "icon": "fas fa-building", "dropdown": True, "className": "mr-3"},
        {"label": "View settings", "icon": "fas fa-eye", "dropdown": True, "className": "mr-3"},
        {"label": "Sort", "icon": "fas fa-sort", "className": "mr-3"},
        {"label": "Filter", "icon": "fas fa-filter"},
    ]
}

app.layout = create_layout(
    content=example_content,
    sidebar_config=sidebar_config,
    header_config=header_config
)

if __name__ == "__main__":
    app.run(debug=True)
