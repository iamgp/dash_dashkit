# Application Setup

Configuration functions for setting up Dash applications with Dashkit.

## setup_app

Configures a Dash app with Dashkit styling, theme management, and asset handling.

### Signature

```python
def setup_app(
    app,
    assets_folder=None,
    include_dashkit_css: bool = True
) -> None
```

### Parameters

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `app` | `Dash` | Required | Dash application instance |
| `assets_folder` | `str \| None` | `None` | Custom assets folder path (preserves app default if None) |
| `include_dashkit_css` | `bool` | `True` | Whether to serve Dashkit's CSS via dedicated route |

### What setup_app Does

1. **Preserves your existing assets** - Doesn't override your `./assets` folder by default
2. **Serves Dashkit CSS** - Creates `/dashkit-assets/` route for packaged styles
3. **Injects HTML template** - Adds FontAwesome, Inter font, and theme switching script
4. **Enables dark mode** - Automatic theme persistence via localStorage

### Examples

#### Basic Setup

```python
from dash import Dash
import dashkit

app = Dash(__name__)
dashkit.setup_app(app)

# Your app now has Dashkit styling and theme support
app.layout = dashkit.create_layout(
    content=html.H1("My Dashboard")
)
```

#### Custom Assets Folder

```python
import dashkit

app = Dash(__name__)
dashkit.setup_app(
    app, 
    assets_folder="my_custom_assets"  # Use custom assets directory
)
```

#### Without Dashkit CSS

```python
import dashkit

app = Dash(__name__)
dashkit.setup_app(
    app,
    include_dashkit_css=False  # Don't serve Dashkit CSS (use your own)
)

# You'll need to include Dashkit styles manually in your assets
```

## What Gets Injected

### HTML Template

The `setup_app` function replaces the default Dash HTML template with:

```html
<!DOCTYPE html>
<html class="">
    <head>
        {%metas%}
        <title>{%title%}</title>
        {%favicon%}
        {%css%}
        
        <!-- FontAwesome Icons -->
        <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css" rel="stylesheet">
        
        <!-- Inter Font -->
        <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
        
        <!-- Dashkit CSS (if included) -->
        <link href="/dashkit-assets/style.css" rel="stylesheet">
        
        <!-- Theme Switching Script -->
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
```

### Asset Route

Creates a Flask route at `/dashkit-assets/<filename>` that serves:
- `style.css` - Compiled Tailwind CSS with Dashkit components
- Any other assets from the Dashkit package

### Theme Management

Injects JavaScript that:
- Checks localStorage for saved theme preference
- Applies `dark` class to `<html>` element if needed
- Runs before page render to prevent flash

## Complete Setup Example

```python
from dash import Dash, html, dcc, Input, Output, callback
import dashkit

# Initialize Dash app
app = Dash(
    __name__,
    title="My Dashboard App",
    suppress_callback_exceptions=True
)

# Configure with Dashkit
dashkit.setup_app(app)

# Sample data
sales_data = [
    {"month": "Jan", "sales": 1000, "profit": 200},
    {"month": "Feb", "sales": 1200, "profit": 250},
    {"month": "Mar", "sales": 950, "profit": 180}
]

table_columns = [
    {"data": "month", "title": "Month"},
    {"data": "sales", "title": "Sales", "type": "numeric"},
    {"data": "profit", "title": "Profit", "type": "numeric"}
]

# Create layout
app.layout = dashkit.create_layout(
    content=html.Div([
        html.H2("Sales Dashboard", className="mb-6"),
        
        # Metrics row
        html.Div([
            dashkit.MetricCard("Total Sales", "$3,150", "+8%", "positive", "dollar-sign"),
            dashkit.MetricCard("Avg Profit", "$210", "+5%", "positive", "trending-up"),
        ], className="grid grid-cols-2 gap-4 mb-6"),
        
        # Data table
        dashkit.Table(
            id="sales-table",
            data=sales_data,
            columns=table_columns,
            height=300
        )
    ]),
    
    sidebar_config={
        "brand_name": "Sales App",
        "brand_initial": "S",
        "nav_items": [
            {"icon": "fas fa-chart-line", "label": "Dashboard", "href": "/"},
            {"icon": "fas fa-table", "label": "Data", "href": "/data"}
        ]
    },
    
    header_config={
        "page_title": "Sales Dashboard",
        "page_icon": "📊",
        "actions": [
            {"type": "secondary", "label": "Export", "icon": "download"},
            {"type": "primary", "label": "Add Record", "icon": "plus"}
        ]
    }
)

# Optional: Add interactivity with callbacks
@callback(
    Output("sales-table", "data"),
    Input("add-record-btn", "n_clicks"),
    prevent_initial_call=True
)
def add_record(n_clicks):
    # Add new record logic
    return updated_data

if __name__ == "__main__":
    app.run(debug=True)
```

## Advanced Configuration

### Multiple Dash Apps

```python
# Primary app
app1 = Dash(__name__, url_base_pathname="/app1/")
dashkit.setup_app(app1)

# Secondary app
app2 = Dash(__name__, url_base_pathname="/app2/") 
dashkit.setup_app(app2)

# Each app gets independent Dashkit configuration
```

### Custom CSS Integration

```python
# Setup Dashkit with your own CSS
app = Dash(__name__)
dashkit.setup_app(app, include_dashkit_css=False)

# Place your CSS files in assets/ folder:
# assets/
# ├── custom-styles.css      # Your custom styles
# ├── dashkit-overrides.css  # Dashkit customizations
# └── app.css                # Application-specific styles
```

### Production Considerations

```python
# Production setup
app = Dash(__name__)

# Configure for production
if not app.config.get("DEBUG", False):
    # Production-specific setup
    dashkit.setup_app(
        app,
        assets_folder="production_assets"
    )
else:
    # Development setup
    dashkit.setup_app(app)
```

## Troubleshooting

### Common Issues

**CSS not loading**
- Check that `include_dashkit_css=True` (default)
- Verify `/dashkit-assets/style.css` is accessible
- Check browser dev tools for 404 errors

**Theme not switching**
- Ensure JavaScript is enabled
- Check browser localStorage for `theme` key
- Verify `<html>` element gets `dark` class

**Assets conflicts**
- Dashkit preserves your existing `assets/` folder
- Use `assets_folder` parameter to specify custom location
- Check for CSS rule conflicts in browser dev tools

**Font or icon issues**
- Verify internet connection for CDN resources
- Check Content Security Policy if using one
- Consider self-hosting fonts for offline applications

### Performance Optimization

```python
# Minimize external requests in production
app = Dash(__name__)
dashkit.setup_app(app)

# Add CSP headers for security
app.server.config.update({
    'CSP_FONT_SRC': 'https://fonts.googleapis.com https://cdnjs.cloudflare.com',
    'CSP_STYLE_SRC': 'https://fonts.googleapis.com https://cdnjs.cloudflare.com'
})
```

## Next Steps

After setting up your app:

1. **Create your layout** using `create_layout()`
2. **Add components** like Tables, Cards, and Buttons
3. **Configure sidebar and header** for navigation
4. **Add interactivity** with Dash callbacks
5. **Customize styling** with additional CSS if needed