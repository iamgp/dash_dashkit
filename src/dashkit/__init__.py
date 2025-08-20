"""
Dashkit - Reusable UI components for Dash applications.

This package provides production-ready components with modern dashboard styling.
All components are configurable and can be used across different projects.
"""

from pathlib import Path

from .buttons import PrimaryButton, SecondaryButton
from .card import Card, ChartCard, MetricCard
from .header import create_header
from .layout import create_layout
from .markdown_report import MarkdownReport
from .sidebar import create_sidebar
from .table import Table, TableWithStats

# Import charts module to register dashkit_shadcn components with Dash
# This must happen even for selective imports to ensure component registration
from . import charts  # noqa: F401
from .charts import AreaChart, BarChart, ChartContainer


def setup_app(app, assets_folder=None):
    """
    Configure a Dash app with dashkit styling and theme management.

    Args:
        app: Dash app instance
        assets_folder: Optional path to assets folder. If not provided, uses the
            package's built-in assets directory.
    """
    # If no assets folder was provided, default to the package's bundled assets
    if assets_folder:
        app.assets_folder = assets_folder
    else:
        pkg_assets = Path(__file__).parent / "assets"
        if pkg_assets.exists():
            app.assets_folder = str(pkg_assets)

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


# Resolve version dynamically from installed package metadata
try:
    from importlib.metadata import PackageNotFoundError, version as _pkg_version
    __version__ = _pkg_version("dash-dashkit")
except Exception:
    __version__ = "0.0.0"

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
    "AreaChart",
    "BarChart", 
    "ChartContainer",
    "setup_app",
]
