# Quick Start Guide

Get up and running with Dashkit in minutes! This guide shows you how to create your first Dashkit dashboard.

## Installation

### Basic Installation

```bash
pip install dash-dashkit
```

### With Additional Components

```bash
# With table support (recommended)
pip install dash-dashkit[table]

# With charts
pip install dash-dashkit[charts]  

# With contribution graphs
pip install dash-dashkit[kiboui]

# Everything included
pip install dash-dashkit[all]
```

## Your First Dashboard

### 1. Basic Setup

Create a new file called `app.py`:

```python
from dash import Dash, html
import dashkit

# Create Dash app
app = Dash(__name__)

# Configure with Dashkit styling
dashkit.setup_app(app)

# Create a simple layout
app.layout = dashkit.create_layout(
    content=html.Div([
        html.H1("My First Dashboard", className="text-2xl font-bold mb-4"),
        html.P("Welcome to Dashkit!", className="text-gray-600"),
    ])
)

if __name__ == "__main__":
    app.run(debug=True)
```

Run your app:
```bash
python app.py
```

Visit `http://localhost:8050` to see your dashboard!

### 2. Add Data and Components

Let's add some real components with data:

```python
from dash import Dash, html
import dashkit

app = Dash(__name__)
dashkit.setup_app(app)

# Sample data
sales_data = [
    {"product": "Laptops", "sales": 1250, "revenue": 125000},
    {"product": "Phones", "sales": 2100, "revenue": 84000}, 
    {"product": "Tablets", "sales": 800, "revenue": 32000},
    {"product": "Accessories", "sales": 3200, "revenue": 16000}
]

columns = [
    {"data": "product", "title": "Product"},
    {"data": "sales", "title": "Units Sold", "type": "numeric"},
    {"data": "revenue", "title": "Revenue", "type": "numeric", "format": "$0,0"}
]

app.layout = dashkit.create_layout(
    content=html.Div([
        html.H1("Sales Dashboard", className="text-2xl font-bold mb-6"),
        
        # Metrics cards
        html.Div([
            dashkit.MetricCard(
                title="Total Revenue",
                value="$257,000",
                change="+12.5%",
                change_type="positive",
                icon="dollar-sign"
            ),
            dashkit.MetricCard(
                title="Units Sold", 
                value="7,350",
                change="+8.2%",
                change_type="positive",
                icon="shopping-cart"
            ),
            dashkit.MetricCard(
                title="Avg Order Value",
                value="$35",
                change="-2.1%", 
                change_type="negative",
                icon="trending-up"
            )
        ], className="grid grid-cols-1 md:grid-cols-3 gap-4 mb-6"),
        
        # Data table
        html.Div([
            html.H2("Product Performance", className="text-lg font-semibold mb-4"),
            dashkit.Table(
                id="sales-table",
                data=sales_data,
                columns=columns,
                height=300
            )
        ]),
        
        # Action buttons
        html.Div([
            dashkit.PrimaryButton("Export Data", icon="download"),
            dashkit.SecondaryButton("Refresh", icon="refresh")
        ], className="flex space-x-3 mt-6")
    ])
)

if __name__ == "__main__":
    app.run(debug=True)
```

### 3. Add Navigation

Now let's add sidebar navigation and a proper header:

```python
from dash import Dash, html
import dashkit

app = Dash(__name__)
dashkit.setup_app(app)

# Your data and components from step 2...
# (keeping the same sales_data, columns, and content)

# Configuration for sidebar
sidebar_config = {
    "brand_name": "Sales Dashboard",
    "brand_initial": "S",
    "nav_items": [
        {"icon": "fas fa-home", "label": "Dashboard", "href": "/"},
        {"icon": "fas fa-chart-bar", "label": "Analytics", "href": "/analytics"},
        {"icon": "fas fa-users", "label": "Customers", "href": "/customers"}
    ],
    "sections": [
        {
            "title": "Reports",
            "items": [
                {"type": "nav_item", "icon": "fas fa-file-alt", "label": "Sales Report"},
                {"type": "nav_item", "icon": "fas fa-chart-line", "label": "Trends"}
            ]
        }
    ]
}

# Configuration for header  
header_config = {
    "page_title": "Sales Overview",
    "page_icon": "📊",
    "actions": [
        {"type": "secondary", "label": "Export", "icon": "download"},
        {"type": "primary", "label": "New Sale", "icon": "plus"}
    ]
}

app.layout = dashkit.create_layout(
    content=your_content_from_step_2,  # The content we built above
    sidebar_config=sidebar_config,
    header_config=header_config
)

if __name__ == "__main__":
    app.run(debug=True)
```

## Adding Interactivity

### Basic Callback

Add interactivity with Dash callbacks:

```python
from dash import Dash, html, Input, Output, callback
import dashkit

app = Dash(__name__)
dashkit.setup_app(app)

app.layout = dashkit.create_layout(
    content=html.Div([
        html.H2("Interactive Dashboard"),
        
        dashkit.PrimaryButton("Click Me!", id="click-btn"),
        html.Div(id="output", className="mt-4 p-4 bg-gray-100 rounded"),
        
        dashkit.Table(
            id="data-table",
            data=[{"name": "Item 1", "value": 100}],
            columns=[
                {"data": "name", "title": "Name"},
                {"data": "value", "title": "Value", "type": "numeric"}
            ]
        )
    ])
)

@callback(
    Output("output", "children"),
    Input("click-btn", "n_clicks"),
    prevent_initial_call=True
)
def update_output(n_clicks):
    return f"Button clicked {n_clicks} times!"

if __name__ == "__main__":
    app.run(debug=True)
```

## Dark Mode Support

Dashkit includes automatic dark mode! Your users can toggle between light and dark themes, and their preference is saved automatically.

The dark mode toggle is built into the layout - no extra configuration needed.

## Next Steps

### Explore More Components

```python
# Try different components
app.layout = dashkit.create_layout(
    content=html.Div([
        # Card components
        dashkit.Card(
            header=html.H3("Recent Activity"),
            children=html.P("Your recent dashboard activity will appear here")
        ),
        
        # Chart card (if you installed charts)
        dashkit.ChartCard(
            title="Performance Metrics",
            children=your_plotly_chart,
            height=400
        ),
        
        # Different button styles
        html.Div([
            dashkit.PrimaryButton("Primary", icon="check"),
            dashkit.SecondaryButton("Secondary", icon="cog")
        ], className="space-x-2")
    ])
)
```

### Learn More

- **[Complete API Reference](../api/README.md)** - Detailed documentation for all components
- **[Component Gallery](components.md)** - Visual examples of all components  
- **[Configuration Guide](configuration.md)** - Advanced customization options
- **[GitHub Repository](https://github.com/iamgp/dash_dashkit)** - Source code and examples

### Common Patterns

**Dashboard with Tabs**
```python
from dash import dcc

app.layout = dashkit.create_layout(
    content=html.Div([
        dcc.Tabs([
            dcc.Tab(label="Overview", children=overview_content),
            dcc.Tab(label="Details", children=details_content)
        ])
    ])
)
```

**Multi-page App**
```python
from dash import page_registry, page_container

# Register pages
dash.register_page(__name__, path="/", name="Home")

app.layout = dashkit.create_layout(
    content=page_container,
    sidebar_config={"nav_items": [
        {"label": "Home", "href": "/"},
        {"label": "Analytics", "href": "/analytics"}
    ]}
)
```

**Responsive Layout**
```python
# Use Tailwind classes for responsive design
content = html.Div([
    html.Div([
        dashkit.MetricCard("Mobile", "1st"),
        dashkit.MetricCard("Tablet", "2nd"), 
        dashkit.MetricCard("Desktop", "3rd")
    ], className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4")
])
```

## Troubleshooting

**Components not styled correctly?**
- Make sure you called `dashkit.setup_app(app)` before defining your layout

**Dark mode not working?** 
- Check that JavaScript is enabled in your browser
- Verify the theme toggle appears in the sidebar

**Table not displaying?**
- Install table support: `pip install dash-dashkit[table]`
- Check that your data format matches the expected structure

**Need help?**
- Check the [API documentation](../api/README.md)
- Look at the [GitHub issues](https://github.com/iamgp/dash_dashkit/issues)
- Create a minimal reproduction case for debugging

Happy dashboard building! 🚀