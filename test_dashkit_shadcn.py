"""Test script to verify dashkit_shadcn registration with Dash"""

import dash
from dash import Dash, html

# Import the package first to trigger __init__.py
import dashkit_shadcn
from dashkit_shadcn.AreaChart import AreaChart

print("Creating test Dash app...")
app = Dash(__name__)

print("Testing AreaChart component...")
test_chart = AreaChart(
    id="test-chart",
    data=[{"name": "A", "value": 10}, {"name": "B", "value": 20}]
)

print("Setting up app layout...")
app.layout = html.Div([
    html.H1("Test dashkit_shadcn"),
    test_chart
])

print("Starting app on port 8051...")
if __name__ == "__main__":
    app.run(debug=True, port=8051)