# API Reference

Complete reference for all Dashkit components and functions.

## Core Components

### Layout Components
- **[create_layout](components/layout.md)** - Main application layout with sidebar and header
- **[create_sidebar](components/sidebar.md)** - Configurable sidebar navigation  
- **[create_header](components/header.md)** - Two-tier header with actions and search

### UI Components  
- **[Table](components/table.md)** - Modern data tables with Handsontable integration
- **[Buttons](components/buttons.md)** - Primary and secondary button components
- **[Cards](components/cards.md)** - Card containers for content organization
- **[MarkdownReport](components/markdown.md)** - Markdown content rendering

### Chart Components (Optional)
- **[AreaChart](components/charts.md#areachart)** - Area chart visualization
- **[BarChart](components/charts.md#barchart)** - Bar chart visualization  
- **[ChartContainer](components/charts.md#chartcontainer)** - Chart wrapper component

## Setup & Configuration

### Application Setup
- **[setup_app](setup.md#setup_app)** - Configure Dash app with Dashkit styling

### Theme Management
- **[ThemeManager](theming.md)** - Theme switching and persistence

## Installation Options

```bash
# Core components only
pip install dash-dashkit

# With table support  
pip install dash-dashkit[table]

# With chart support
pip install dash-dashkit[charts]

# With contribution graphs
pip install dash-dashkit[kiboui]

# Everything included
pip install dash-dashkit[all]
```

## Import Structure

```python
# Core imports
from dashkit import create_layout, setup_app
from dashkit import Table, PrimaryButton, SecondaryButton
from dashkit import Card, MetricCard, ChartCard, MarkdownReport

# Optional chart imports (requires dashkit_shadcn)
from dashkit import AreaChart, BarChart, ChartContainer

# Direct component imports
from dashkit_table import DashkitTable
from dashkit_kiboui import ContributionGraph
from dashkit_shadcn import AreaChart as ShadcnAreaChart
```

## Quick Example

```python
from dash import Dash, html
import dashkit

app = Dash(__name__)
dashkit.setup_app(app)

data = [{"name": "Alice", "score": 10}, {"name": "Bob", "score": 20}]
columns = [{"data": "name", "title": "Name"}, {"data": "score", "title": "Score"}]

app.layout = dashkit.create_layout(
    content=html.Div([
        html.H3("Dashboard"),
        dashkit.Table(id="table", data=data, columns=columns, height=300),
        dashkit.PrimaryButton("Add Row", icon="plus")
    ]),
    sidebar_config={"brand_name": "My App"},
    header_config={"page_title": "Dashboard"}
)

if __name__ == "__main__":
    app.run(debug=True)
```