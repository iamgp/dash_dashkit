# Import parent directory for components
import sys
from pathlib import Path

import dash

sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from dashkit import Table
from dashkit_demo.demo_utils import create_company_columns, format_company_data

# Sample company data (moved from app.py)
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
]

table_data = format_company_data(companies_data)
columns = create_company_columns()

dash.register_page(__name__, path="/", title="Companies")

layout = Table(
    id="companies-table",
    data=table_data,
    columns=columns,
    height=600,
    theme_name="ht-theme-horizon",
)
