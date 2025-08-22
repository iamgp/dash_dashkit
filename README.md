# Dashkit

Production-ready UI components for Dash applications with modern dashboard styling. All components are configurable and can be used across different projects.

## Project Structure

```
dashkit/
├── src/
│   ├── dashkit/                   # Reusable components package
│   │   ├── __init__.py
│   │   ├── layout.py              # Main layout component
│   │   ├── sidebar.py             # Configurable sidebar
│   │   ├── header.py              # Configurable header
│   │   ├── table.py               # Dashkit-style tables
│   │   ├── buttons.py             # Button components
│   │   ├── logo.py                # Logo components
│   │   ├── navigation.py          # Navigation components
│   │   └── dashkit_table/         # Advanced table components
│   └── assets/
│       ├── style.css              # Compiled styles
│       └── input.css              # Tailwind source
├── run.py                         # Quick demo runner
└── pyproject.toml                 # Dependencies
```

## Installation

```bash
pip install dash-dashkit
# Also ensure these dependencies are available (they install automatically):
# dashkit_table, dashkit_shadcn, dashkit_kiboui
```

## Quick Start

### Minimal app

```python
from dash import Dash, html
import dashkit

app = Dash(__name__)
dashkit.setup_app(app)

rows = [{"name":"Alice","score":10},{"name":"Bob","score":20}]
cols = [{"data":"name","title":"Name"},{"data":"score","title":"Score"}]

app.layout = dashkit.create_layout(
    content=html.Div([
        html.H3("Example"),
        dashkit.Table(id="t", data=rows, columns=cols, height=240),
    ])
)

if __name__ == "__main__":
    app.run(debug=True)
```

- Install core: `pip install dash-dashkit`
- With table: `pip install dash-dashkit[table]`
- With everything: `pip install dash-dashkit[all]`

### Using Components in Your Project

```python
from dashkit import create_layout, setup_app, Table

app = Dash(__name__)

# Configure app with dashkit styling (handles CSS and theme injection)
setup_app(app)

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
table = Table(id="my-table", data=your_data, columns=your_columns)

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

- `Table()` - Modern table using Handsontable
- `TableWithStats()` - Table with count header

### UI Components

- `PrimaryButton()` - Primary action buttons
- `SecondaryButton()` - Secondary action buttons

## Features

- ✅ Fully configurable components
- ✅ Modern dashboard design system
- ✅ TypeScript support for tables
- ✅ Modern Handsontable v16.0.1 integration
- ✅ Responsive layout
- ✅ Font Awesome icons
- ✅ Inter font typography
- ✅ Clean, linted code (ruff + basedpyright)

## Development

### Available Tasks

This project uses taskipy for common development tasks:

```bash
# Complete setup (install npm deps, build table component, install Python package)
uv run task setup

# Build only the table component
uv run task build-table

# Install only the table component
uv run task install-table

# Run linting and formatting
uv run task lint

# Run type checking
uv run task typecheck

# Run both linting and type checking
uv run task check

# Start the development server
uv run task dev
```

### Manual Development Commands

```bash
# Run linting
ruff check .
ruff format .

# Run type checking
basedpyright src

# Build CSS (if modified)
npx tailwindcss -i src/assets/input.css -o src/assets/style.css --watch

# Manual table component build
cd src/dashkit_table
npm install
npm run build
uv pip install -e .
```

## Releasing (manual tags)

Releases are driven by tags. Publishing runs in CI and a smoke test validates PyPI install.

Prerequisites:

- GitHub Actions secret: `PYPI_API_TOKEN` (PyPI API token with upload permission)

Subpackages

- dashkit_table
  1. Bump version in `src/dashkit_table/pyproject.toml`
  2. Commit and push (if ignored, force add): `git add -f src/dashkit_table/pyproject.toml && git commit -m "release(table): X.Y.Z" && git push`
  3. Tag and push: `git tag dashkit_table-vX.Y.Z && git push origin dashkit_table-vX.Y.Z`
- dashkit_kiboui
  1. Bump version in `src/dashkit_kiboui/pyproject.toml`
  2. Commit and push
  3. Tag and push: `git tag dashkit_kiboui-vX.Y.Z && git push origin dashkit_kiboui-vX.Y.Z`

Main package (dash-dashkit)

- Bump version in `pyproject.toml` (update subpackage minimums as needed)
- Commit and push
- Tag and push: `git tag dashkit-vX.Y.Z && git push origin dashkit-vX.Y.Z`
  - Legacy form `vX.Y.Z` is also supported

CI workflows

- Publish: builds the package for the matching tag and uploads to PyPI
- Smoke: installs the just-published version in a clean venv and imports/instantiates components
- Manual fallback: both workflows support `workflow_dispatch` with `tag_name` if you need to re-run

Notes

- If `src/dashkit_table` is ignored in `.gitignore`, use `git add -f` or remove the ignore entry
- Tag patterns must match exactly as above (component-vX.Y.Z)

## Configuration Examples

See `src/dashkit_demo/app.py` for complete configuration examples including:

- Sidebar navigation structure
- Header actions and filters
- Table data formatting
- Component styling options
