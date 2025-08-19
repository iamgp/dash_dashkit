"""
Dashkit - Reusable UI components for Dash applications.

This package provides production-ready components with modern dashboard styling.
All components are configurable and can be used across different projects.
"""

from .buttons import PrimaryButton, SecondaryButton
from .card import Card, ChartCard, MetricCard
from .header import create_header
from .layout import create_layout
from .markdown_report import MarkdownReport
from .sidebar import create_sidebar
from .table import Table, TableWithStats


def setup_app(app, assets_folder=None):
    """
    Configure a Dash app with dashkit styling and theme management.

    Args:
        app: Dash app instance
        assets_folder: Optional path to assets folder (defaults to app's assets_folder)
    """
    if assets_folder:
        app.assets_folder = assets_folder

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


__version__ = "1.0.0"
__all__ = [
    "create_layout",
    "create_sidebar",
    "create_header",
    "Table",
    "TableWithStats",
    "PrimaryButton",
    "SecondaryButton",
    "MarkdownReport",
    "Card",
    "MetricCard",
    "ChartCard",
    "setup_app",
]
