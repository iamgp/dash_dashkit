# Architecture Overview

Understanding the structure and design patterns of the Dashkit project.

## Project Architecture

### Multi-Package Structure

Dashkit is organized as a monorepo with multiple packages:

```
dash-dashkit/
├── src/
│   ├── dashkit/           # Core Python package
│   ├── dashkit_table/     # Table components (React + Python)
│   ├── dashkit_shadcn/    # Chart components (React + Python)  
│   └── dashkit_kiboui/    # Contribution graphs (React + Python)
├── docs/                  # Documentation
├── scripts/               # Build and release scripts
└── pyproject.toml        # Main package configuration
```

### Package Responsibilities

**Core Package (`src/dashkit/`)**
- Layout components (sidebar, header, main layout)
- Basic UI components (buttons, cards)
- Theme management and CSS integration
- Application setup and configuration

**Component Packages**
- React/TypeScript components compiled to JavaScript
- Python wrapper classes for Dash integration
- Specialized functionality (tables, charts, graphs)
- Independent versioning and releases

## Core Components Design

### Layout System

The layout system follows a hierarchical structure:

```
create_layout()
├── Sidebar (create_sidebar)
│   ├── Logo Section
│   ├── Navigation Items
│   ├── Grouped Sections
│   └── Theme Toggle
├── Header (create_header)
│   ├── Page Title/Breadcrumbs
│   ├── Search (optional)
│   └── Action Buttons
└── Main Content Area
    └── User-provided content
```

### Component Architecture

Components follow consistent patterns:

```python
def Component(
    # Required parameters first
    id: str,
    # Main content parameters
    content: Any,
    # Configuration dictionaries
    config: dict[str, Any] | None = None,
    # Styling parameters
    className: str = "",
    # Extensibility
    **kwargs: Any
) -> html.Div:
    """Component docstring with examples."""
```

## JavaScript Integration

### React Component Structure

Component packages use this structure:

```
src/dashkit_table/
├── src/ts/
│   ├── components/
│   │   ├── DashkitTable.tsx    # Main React component
│   │   ├── index.ts            # Exports
│   │   └── lib/
│   │       ├── types.ts        # TypeScript definitions
│   │       └── utils.ts        # Utility functions
│   ├── package.json           # npm configuration
│   ├── tsconfig.json         # TypeScript config
│   └── webpack.config.js     # Build configuration
├── dashkit_table/
│   ├── DashkitTable.py       # Python wrapper
│   └── __init__.py           # Package exports
└── pyproject.toml           # Python package config
```

### Build Process

1. **TypeScript → JavaScript**: Components compiled with webpack
2. **JavaScript → Python**: Dash components generated automatically
3. **Python Package**: Wrapped with convenience functions
4. **Distribution**: Published as separate PyPI packages

### Python-JavaScript Bridge

```python
# Python wrapper example
from dash import html
try:
    from dashkit_table import DashkitTable as JSComponent
except ImportError:
    JSComponent = None

def Table(id: str, data: list, **kwargs) -> html.Div:
    """Python wrapper around JavaScript component."""
    if JSComponent is None:
        return html.Div("Table component not installed")
    
    # Data processing and validation
    processed_data = process_table_data(data)
    
    # Component instantiation
    return JSComponent(
        id=id,
        data=processed_data,
        **kwargs
    )
```

## CSS and Styling

### Tailwind CSS Integration

Dashkit uses Tailwind CSS v4 for styling:

```
src/
├── input.css              # Tailwind source
└── dashkit/assets/
    └── style.css          # Compiled output
```

**Build Process:**
```bash
npx tailwindcss -i src/input.css -o src/dashkit/assets/style.css --minify
```

### Theme System

**CSS Custom Properties:**
```css
:root {
  --dashkit-primary: rgb(59 130 246);
  --dashkit-background: rgb(255 255 255);
}

.dark {
  --dashkit-primary: rgb(96 165 250);
  --dashkit-background: rgb(17 24 39);
}
```

**JavaScript Theme Switching:**
```javascript
// Injected in HTML template
const storedTheme = localStorage.getItem('theme');
if (storedTheme === 'dark') {
    document.documentElement.classList.add('dark');
}
```

## Configuration Patterns

### Dictionary-Based Configuration

Components use dictionaries for complex configuration:

```python
sidebar_config = {
    "brand_name": "App",
    "nav_items": [
        {"icon": "home", "label": "Dashboard", "href": "/"}
    ],
    "sections": [
        {
            "title": "Analytics",
            "items": [
                {"type": "nav_item", "icon": "chart", "label": "Reports"}
            ]
        }
    ]
}
```

### Configuration Validation

```python
def validate_sidebar_config(config: dict) -> dict:
    """Validate and normalize sidebar configuration."""
    defaults = {
        "brand_name": "App",
        "brand_initial": "A",
        "nav_items": [],
        "sections": []
    }
    
    # Merge with defaults
    validated = {**defaults, **config}
    
    # Validate structure
    for item in validated["nav_items"]:
        if "label" not in item:
            raise ValueError("nav_items must have 'label' field")
    
    return validated
```

## Asset Management

### Static Assets

```python
# Asset serving in setup_app()
from pathlib import Path
from flask import send_from_directory

pkg_assets = Path(__file__).parent / "assets"

@app.server.route("/dashkit-assets/<path:filename>")
def _dashkit_assets(filename: str):
    return send_from_directory(str(pkg_assets), filename)
```

### HTML Template Injection

```python
app.index_string = """
<!DOCTYPE html>
<html>
    <head>
        {%metas%}
        <title>{%title%}</title>
        {%css%}
        <link href="/dashkit-assets/style.css" rel="stylesheet">
        <script>/* theme switching */</script>
    </head>
    <body>{%app_entry%}</body>
</html>
"""
```

## Error Handling

### Graceful Degradation

```python
# Optional imports with fallbacks
try:
    from dashkit_table import DashkitTable
except ImportError as e:
    DashkitTable = None
    _import_error = e

def Table(*args, **kwargs):
    if DashkitTable is None:
        return html.Div([
            html.P("Table component not available"),
            html.P(f"Install with: pip install dash-dashkit[table]"),
            html.Details([
                html.Summary("Error details"),
                html.Pre(str(_import_error))
            ])
        ])
    return DashkitTable(*args, **kwargs)
```

### Configuration Validation

```python
def create_layout(
    content=None,
    sidebar_config=None,
    header_config=None
):
    # Provide defaults
    if content is None:
        content = html.Div("Welcome to Dashkit")
    
    if sidebar_config is None:
        sidebar_config = {"brand_name": "App"}
    
    # Validate configuration
    try:
        sidebar_config = validate_sidebar_config(sidebar_config)
    except ValueError as e:
        # Log error and use defaults
        print(f"Invalid sidebar config: {e}")
        sidebar_config = {"brand_name": "App"}
```

## Release Process

### Multi-Package Releases

Each package has independent versioning:

```bash
# Component package release
cd src/dashkit_table
# Bump version in pyproject.toml
git tag dashkit_table-v1.2.3

# Main package release  
# Bump version in pyproject.toml
git tag dashkit-v1.3.0
```

### CI/CD Pipeline

```yaml
# .github/workflows/release.yml
jobs:
  publish-table:
    if: startsWith(github.ref_name, 'dashkit_table-v')
    steps:
      - build component package
      - publish to PyPI
      
  publish-main:
    if: startsWith(github.ref_name, 'dashkit-v')  
    steps:
      - build main package
      - publish to PyPI
```

## Performance Considerations

### Bundle Size

- **Core package**: Minimal JavaScript (theme switching only)
- **Component packages**: Include only necessary dependencies
- **CSS**: Optimized with Tailwind's purge functionality

### Runtime Performance  

- **Lazy loading**: Optional components imported only when needed
- **Caching**: Static assets served with proper cache headers
- **Minimal DOM**: Efficient HTML structure with semantic elements

## Extension Points

### Adding New Components

1. **Create component file** in `src/dashkit/`
2. **Follow naming conventions** and type hints
3. **Add to exports** in `__init__.py`
4. **Document in** `docs/api/components/`

### Creating Component Packages

1. **Use existing package as template** (e.g., dashkit_table)
2. **Follow TypeScript/React patterns** for JavaScript components
3. **Create Python wrappers** for Dash integration
4. **Add build and release configuration**

### Theming Extensions

```python
# Custom theme injection
def setup_custom_theme(app, theme_css_url):
    app.index_string = app.index_string.replace(
        "</head>",
        f'<link href="{theme_css_url}" rel="stylesheet"></head>'
    )
```

This architecture provides a foundation for:
- **Consistent component APIs**
- **Flexible configuration**
- **Graceful error handling** 
- **Independent package evolution**
- **Easy extensibility**