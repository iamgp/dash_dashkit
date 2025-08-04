# Dash Attio Components

Production-ready UI components for Dash applications styled to match Attio's design system. All components are configurable and can be used across different projects.

## Project Structure

```
dash-attio/
├── src/
│   ├── dash_attio_components/     # Reusable components package
│   │   ├── __init__.py
│   │   ├── layout.py              # Main layout component
│   │   ├── sidebar.py             # Configurable sidebar
│   │   ├── header.py              # Configurable header
│   │   ├── table.py               # Attio-style tables
│   │   ├── buttons.py             # Button components
│   │   ├── logo.py                # Logo components
│   │   ├── navigation.py          # Navigation components
│   │   └── attio_table/           # Advanced table components
│   ├── dash_attio_demo/           # Demo application
│   │   ├── __init__.py
│   │   └── app.py                 # Example usage
│   └── assets/
│       ├── style.css              # Compiled styles
│       └── input.css              # Tailwind source
├── run.py                         # Quick demo runner
└── pyproject.toml                 # Dependencies
```

## Quick Start

### Running the Demo

```bash
# Install dependencies
uv sync

# Run the demo application
python run.py
# or
python src/dash_attio_demo/app.py
```

Visit http://localhost:8050 to see the demo.

### Using Components in Your Project

```python
from dash_attio_components import create_layout, AttioTable

# Configure sidebar
sidebar_config = {
    "brand_name": "Your App",
    "brand_initial": "Y",
    "nav_items": [
        {"icon": "fas fa-home", "label": "Dashboard"},
    ],
    "sections": [
        {
            "title": "Records", 
            "items": [
                {"type": "nav_item", "icon": "fas fa-users", "label": "Users"}
            ]
        }
    ]
}

# Configure header
header_config = {
    "page_title": "Dashboard",
    "page_icon": "📊",
    "actions": [
        {"type": "primary", "label": "New Item", "icon": "fas fa-plus"}
    ]
}

# Create your content
table = AttioTable(data=your_data, columns=your_columns)

# Build the layout
app.layout = create_layout(
    content=table,
    sidebar_config=sidebar_config,
    header_config=header_config
)
```

## Available Components

### Layout Components
- `create_layout()` - Main application layout
- `create_sidebar()` - Configurable sidebar with navigation
- `create_header()` - Two-tier header with search and actions

### Table Components  
- `AttioTable()` - Modern table using Handsontable
- `AttioTableWithStats()` - Table with count header
- `AttioHTMLTable()` - Pure HTML table variant

### UI Components
- `PrimaryButton()` - Primary action buttons
- `SecondaryButton()` - Secondary action buttons

## Features

- ✅ Fully configurable components
- ✅ Attio-style design system
- ✅ TypeScript support for tables
- ✅ Modern Handsontable v16.0.1 integration
- ✅ Responsive layout
- ✅ Font Awesome icons
- ✅ Inter font typography
- ✅ Clean, linted code (ruff + basedpyright)

## Development

```bash
# Run linting
ruff check .
ruff format .

# Run type checking  
basedpyright src

# Build CSS (if modified)
npx tailwindcss -i src/assets/input.css -o src/assets/style.css --watch
```

## Configuration Examples

See `src/dash_attio_demo/app.py` for complete configuration examples including:
- Sidebar navigation structure
- Header actions and filters
- Table data formatting
- Component styling options