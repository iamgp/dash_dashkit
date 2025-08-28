# Dashkit

**Modern dashboard components for Dash applications**

Dashkit provides production-ready UI components with modern dashboard styling. All components are configurable and can be used across different projects with consistent theming and responsive design.

## Key Features

- ✅ **Fully configurable components** - Customize every aspect through configuration dictionaries
- ✅ **Modern dashboard design** - Beautiful, consistent styling with dark mode support
- ✅ **TypeScript support** - Advanced table components with modern Handsontable integration
- ✅ **Responsive layout** - Works seamlessly across desktop, tablet, and mobile
- ✅ **Rich theming** - Automatic dark/light mode with user preference persistence
- ✅ **Icon integration** - Built-in support for Font Awesome and MyNaUI icons
- ✅ **Clean, typed code** - Full type hints and linted codebase

## Quick Example

```python
from dash import Dash, html
import dashkit

app = Dash(__name__)
dashkit.setup_app(app)

# Sample data
data = [
    {"product": "Laptops", "sales": 1250, "revenue": 125000},
    {"product": "Phones", "sales": 2100, "revenue": 84000}
]

columns = [
    {"data": "product", "title": "Product"},
    {"data": "sales", "title": "Units Sold", "type": "numeric"},
    {"data": "revenue", "title": "Revenue", "type": "numeric", "format": "$0,0"}
]

app.layout = dashkit.create_layout(
    content=html.Div([
        html.H1("Sales Dashboard", className="mb-6"),
        
        # Metrics
        html.Div([
            dashkit.MetricCard("Revenue", "$209K", "+15%", "positive", "dollar-sign"),
            dashkit.MetricCard("Units", "3,350", "+12%", "positive", "shopping-cart")
        ], className="grid grid-cols-2 gap-4 mb-6"),
        
        # Data table
        dashkit.Table(id="sales-table", data=data, columns=columns, height=300)
    ]),
    
    # Sidebar configuration
    sidebar_config={
        "brand_name": "Sales App",
        "nav_items": [
            {"icon": "fas fa-chart-line", "label": "Dashboard"},
            {"icon": "fas fa-table", "label": "Data"}
        ]
    },
    
    # Header configuration  
    header_config={
        "page_title": "Sales Dashboard",
        "page_icon": "📊",
        "actions": [
            {"type": "primary", "label": "Add Sale", "icon": "fas fa-plus"}
        ]
    }
)

if __name__ == "__main__":
    app.run(debug=True)
```

## Installation

=== "Basic Installation"

    ```bash
    pip install dash-dashkit
    ```

=== "With Tables"

    ```bash
    pip install dash-dashkit[table]
    ```

=== "With Charts"

    ```bash
    pip install dash-dashkit[charts]
    ```

=== "Everything"

    ```bash
    pip install dash-dashkit[all]
    ```

## Component Overview

### Layout System
- **[create_layout](api/components/layout.md)** - Complete dashboard layout with sidebar and header
- **[create_sidebar](api/components/sidebar.md)** - Configurable navigation sidebar
- **[create_header](api/components/header.md)** - Header with title, breadcrumbs, and actions

### Data Components
- **[Table](api/components/table.md)** - Modern data tables with Handsontable integration
- **[MarkdownReport](api/components/markdown.md)** - Rich markdown content rendering

### UI Elements
- **[Buttons](api/components/buttons.md)** - Primary and secondary styled buttons
- **[Cards](api/components/cards.md)** - Content containers and metric displays

### Visualizations *(Optional)*
- **[Charts](api/components/charts.md)** - Area charts, bar charts, and containers

## Architecture

Dashkit follows a **multi-package architecture** for modularity:

- **`dashkit`** - Core layout and UI components
- **`dashkit_table`** - Advanced table components (React + Python)  
- **`dashkit_shadcn`** - Chart components with shadcn/ui styling
- **`dashkit_kiboui`** - Contribution graph components

Each package can be installed independently based on your needs.

## Next Steps

<div class="grid cards" markdown>

- :material-rocket-launch: **[Quick Start Guide](guides/quickstart.md)**

    Get up and running with your first dashboard in minutes

- :material-api: **[API Reference](api/README.md)**

    Complete documentation for all components and configuration options

- :material-palette: **Component Examples**

    Visual examples and code snippets for every component

- :material-github: **[GitHub Repository](https://github.com/iamgp/dash_dashkit)**

    Source code, issues, and latest releases

</div>

## Support

- **Documentation**: Complete API reference and guides available
- **Issues**: Report bugs and request features on [GitHub](https://github.com/iamgp/dash_dashkit/issues)
- **PyPI Package**: [dash-dashkit](https://pypi.org/project/dash-dashkit/) for latest releases

---

*Built with ❤️ for the Dash community*