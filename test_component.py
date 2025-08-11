#!/usr/bin/env python3
"""Test script to verify our custom component works."""

import sys
from pathlib import Path

# Add the src directory to the path for imports
sys.path.insert(0, str(Path(__file__).parent / "src"))

import dash
from dash import html
from dash_attio_table import AttioTable

# Create a minimal test app
app = dash.Dash(__name__)

app.layout = html.Div(
    [
        html.H1("Testing Custom AttioTable Component"),
        AttioTable(
            id="test-table",
            data=[["A", "B", "C"], [1, 2, 3], [4, 5, 6]],
            height=300,
            themeName="ht-theme-main",
            colHeaders=True,
            licenseKey="non-commercial-and-evaluation",
        ),
    ]
)

if __name__ == "__main__":
    print("Starting test app...")
    print("Component available:", AttioTable)
    app.run(debug=True, port=8051)
