"""
Dash Attio Components - Reusable UI components for Dash applications.

This package provides production-ready components styled to match Attio's design system.
All components are configurable and can be used across different projects.
"""

from .attio_table import AttioTable
from .buttons import PrimaryButton, SecondaryButton
from .header import create_header
from .layout import create_layout
from .sidebar import create_sidebar
from .table import AttioTableWithStats

__version__ = "1.0.0"
__all__ = [
    "create_layout",
    "create_sidebar",
    "create_header",
    "AttioTable",
    "AttioTableWithStats",
    "PrimaryButton",
    "SecondaryButton",
]
