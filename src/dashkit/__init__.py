"""
Dashkit - Reusable UI components for Dash applications.

This package provides production-ready components with modern dashboard styling.
All components are configurable and can be used across different projects.
"""

from .table import Table
from .buttons import PrimaryButton, SecondaryButton
from .header import create_header
from .layout import create_layout
from .markdown_report import MarkdownReport
from .sidebar import create_sidebar
from .table import TableWithStats

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
]
