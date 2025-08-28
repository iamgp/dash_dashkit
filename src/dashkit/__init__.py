"""
Dashkit - Reusable UI components for Dash applications.

This package provides production-ready components with modern dashboard styling.
All components are configurable and can be used across different projects.
"""

from pathlib import Path

from flask import send_from_directory

from .buttons import PrimaryButton, SecondaryButton
from .callout import (
    Callout,
    CautionCallout,
    ImportantCallout,
    NoteCallout,
    TipCallout,
    WarningCallout,
)
from .card import Card, ChartCard, MetricCard
from .header import create_header
from .layout import create_layout
from .markdown_report import MarkdownReport
from .sidebar import create_sidebar
from .table import Table, TableWithStats

# Charts are optional; only import if available
try:
    from .charts import AreaChart, BarChart, ChartContainer  # type: ignore
except Exception:  # pragma: no cover - optional dependency may be missing
    AreaChart = None  # type: ignore[assignment]
    BarChart = None  # type: ignore[assignment]
    ChartContainer = None  # type: ignore[assignment]


def setup_app(app, assets_folder=None, include_dashkit_css: bool = True):
    """
    Configure a Dash app with dashkit styling and theme management.

    Args:
        app: Dash app instance
        assets_folder: Optional path to assets folder for your app (defaults to
            Dash's own ./assets). We do NOT override your assets by default.
        include_dashkit_css: When True, serve dashkit's packaged CSS via a
            dedicated route and include a <link> in the index.
    """
    # Preserve the app's own assets folder unless explicitly overridden
    if assets_folder:
        app.assets_folder = assets_folder

    # Serve dashkit's packaged assets from a namespaced route so app assets still work
    pkg_assets = Path(__file__).parent / "assets"
    if include_dashkit_css and pkg_assets.exists():
        route_attr = "_dashkit_assets_route_registered"
        if not getattr(app.server, route_attr, False):

            @app.server.route("/dashkit-assets/<path:filename>")
            def _dashkit_assets(filename: str):  # type: ignore
                return send_from_directory(str(pkg_assets), filename)

            setattr(app.server, route_attr, True)

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
        {dashkit_css}
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
""".replace(
        "{dashkit_css}",
        '<link href="/dashkit-assets/style.css" rel="stylesheet">'
        if include_dashkit_css and pkg_assets.exists()
        else "",
    )


# Resolve version dynamically from installed package metadata
try:
    from importlib.metadata import version as _pkg_version

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
    "Callout",
    "NoteCallout",
    "TipCallout",
    "ImportantCallout",
    "WarningCallout",
    "CautionCallout",
    "setup_app",
]

# Expose charts if available
if AreaChart is not None and BarChart is not None and ChartContainer is not None:
    __all__ += ["AreaChart", "BarChart", "ChartContainer"]
