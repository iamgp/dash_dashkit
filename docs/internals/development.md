# Development Setup Guide

Internal guide for setting up the development environment for Dashkit maintainers.

## Prerequisites

### Required Software

- **Python 3.10 or higher** - Check with `python --version`
- **uv package manager** - Install from [astral-sh.github.io/uv](https://astral-sh.github.io/uv/)
- **Node.js 18 or higher** - For building JavaScript components
- **Git** - For version control

### Installation

```bash
# Install uv (if not already installed)
curl -LsSf https://astral-sh.github.io/uv/install.sh | sh

# Verify installations
python --version   # Should be 3.10+
uv --version       # Should be 0.1.0+
node --version     # Should be 18.0.0+
npm --version      # Should be 8.0.0+
```

## Repository Setup

### 1. Clone Repository

```bash
git clone https://github.com/iamgp/dash_dashkit.git
cd dash_dashkit
```

### 2. Environment Setup

```bash
# Complete setup (recommended for first-time setup)
uv run task setup

# This command:
# 1. Creates Python virtual environment
# 2. Installs all Python dependencies  
# 3. Installs npm dependencies for table component
# 4. Builds the table component
# 5. Installs the package in development mode
```

### 3. Verify Installation

```bash
# Run quality checks
uv run task check

# Expected output:
# ✓ Linting passed
# ✓ Type checking passed with warnings (this is normal)
```

## Development Environment

### Project Structure

```
dash-dashkit/
├── src/
│   ├── dashkit/              # Core Python components
│   │   ├── __init__.py       # Main package exports
│   │   ├── layout.py         # Layout components
│   │   ├── buttons.py        # Button components
│   │   └── ...               # Other core components
│   │
│   ├── dashkit_table/        # Table component package
│   │   ├── src/ts/           # TypeScript source
│   │   ├── package.json      # npm configuration
│   │   └── pyproject.toml    # Python package config
│   │
│   ├── dashkit_shadcn/       # Chart components
│   └── dashkit_kiboui/       # Contribution graph components
│
├── docs/                     # Documentation
├── scripts/                  # Build and utility scripts
├── pyproject.toml           # Main package configuration
└── package.json             # CSS build configuration
```

### Available Tasks

The project uses taskipy for common development tasks:

```bash
# Complete project setup
uv run task setup

# Build only the table component
uv run task build-table

# Install only the table component
uv run task install-table

# Build CSS (if you modify Tailwind styles)
uv run task build-css

# Run linting and formatting
uv run task lint

# Run type checking
uv run task typecheck

# Run both linting and type checking
uv run task check
```

## Development Workflow

### Daily Development

```bash
# Start your development session
cd dash-dashkit

# Pull latest changes
git pull origin main

# Make your changes...

# Run checks before committing
uv run task check

# Commit changes
git add .
git commit -m "feat: add new feature"
git push origin main
```

### Working with Core Components

Core components are in `src/dashkit/`. These are pure Python files:

```bash
# Edit core components
code src/dashkit/buttons.py

# Test your changes immediately (no build required)
python test_script.py

# Run quality checks
uv run task check
```

### Working with JavaScript Components

For components that include JavaScript (table, charts, etc.):

```bash
# Navigate to component directory
cd src/dashkit_table

# Install npm dependencies (if not already done)
npm install

# Make changes to TypeScript files in src/ts/

# Build the component
npm run build

# Install the updated package
uv pip install -e .

# Test your changes
cd ../..
python test_script.py
```

### CSS Development

If you need to modify styles:

```bash
# Edit the Tailwind source
code src/input.css

# Build CSS (with watching for changes)
npm run build-css

# Or build once
uv run task build-css
```

## Testing Changes

### Manual Testing

Create test scripts to verify your changes:

```python
# test_my_changes.py
from dash import Dash, html
import dashkit

app = Dash(__name__)
dashkit.setup_app(app)

# Test your component
app.layout = dashkit.create_layout(
    content=html.Div([
        html.H2("Testing My Changes"),
        # Your component here
        dashkit.MyNewComponent(id="test")
    ])
)

if __name__ == "__main__":
    app.run(debug=True, port=8050)
```

### Quality Checks

Always run these before committing:

```bash
# Comprehensive check
uv run task check

# Individual checks
uv run task lint      # Code formatting and style
uv run task typecheck # Type checking with basedpyright
```

## Common Development Tasks

### Adding a New Core Component

1. **Create the component file**:
   ```bash
   touch src/dashkit/my_component.py
   ```

2. **Implement the component**:
   ```python
   # src/dashkit/my_component.py
   from dash import html
   from typing import Any
   
   def MyComponent(
       id: str,
       children: Any = None,
       **kwargs: Any
   ) -> html.Div:
       """My new component."""
       return html.Div(
           children=children,
           id=id,
           className="my-component-class",
           **kwargs
       )
   ```

3. **Export in __init__.py**:
   ```python
   # Add to src/dashkit/__init__.py
   from .my_component import MyComponent
   
   __all__ = [
       # ... existing exports
       "MyComponent",
   ]
   ```

4. **Test and document**:
   ```bash
   # Test your component
   python test_my_component.py
   
   # Run quality checks
   uv run task check
   
   # Create API documentation
   code docs/api/components/my_component.md
   ```

### Adding a JavaScript Component

For components requiring React/TypeScript:

1. **Use existing component packages** as templates
2. **Follow the structure** in `src/dashkit_table/`
3. **Build and test** using npm commands
4. **Integrate with Python** wrapper functions

### Updating Dependencies

```bash
# Update Python dependencies
uv sync

# Update npm dependencies (for component packages)
cd src/dashkit_table
npm update
cd ../dashkit_shadcn  
npm update
cd ../dashkit_kiboui
npm update
```

## Release Process

### Version Bumping

Use the provided script to bump versions:

```bash
# Bump patch version for all packages
uv run python scripts/bump_version.py

# Bump minor version
uv run python scripts/bump_version.py --minor

# Bump major version  
uv run python scripts/bump_version.py --major

# Interactive mode
uv run python scripts/bump_version.py --interactive
```

### Creating Releases

```bash
# For subpackages
git tag dashkit_table-v1.2.3
git push origin dashkit_table-v1.2.3

# For main package
git tag dashkit-v1.3.0
git push origin dashkit-v1.3.0
```

### Build for Distribution

```bash
# Build all subpackages
uv run task build-subpackages

# Build main package
uv run task build-main

# Test upload to TestPyPI (optional)
uv run task publish-subpackages-test
uv run task publish-main-test

# Upload to PyPI (production)
uv run task publish-subpackages
uv run task publish-main
```

## Troubleshooting

### Common Issues

**"Command not found: uv"**
```bash
# Install uv
curl -LsSf https://astral-sh.github.io/uv/install.sh | sh
# Restart your terminal
```

**"Task setup failed"**
```bash
# Try individual steps
cd src/dashkit_table
npm install
npm run build
cd ../..
uv pip install -e .
```

**"Type checking errors"**
- Check that basedpyright is installed: `uv run basedpyright --version`
- Some warnings are expected - focus on errors

**"Import errors in tests"**
```bash
# Reinstall in development mode
uv pip install -e .
```

## Development Tools

### Recommended VS Code Extensions

- **Python** - Python language support
- **Pylance** - Python language server  
- **Tailwind CSS IntelliSense** - CSS class autocomplete
- **TypeScript Importer** - Auto import for TypeScript (if working on JS components)

### Editor Configuration

The project includes configuration files:

- **`pyproject.toml`** - Python tool configuration (ruff, basedpyright)
- **`tsconfig.json`** - TypeScript configuration (in component packages)

## Performance Optimization

### Development Performance

- Use `npm run build` instead of `npm run watch` for components unless actively developing
- Run `uv run task check` frequently but not on every save
- Use virtual environments to avoid dependency conflicts

### Build Performance

- The `uv run task setup` command only needs to be run once
- Individual component builds are faster: `uv run task build-table`
- CSS builds are very fast with Tailwind 4.0

## Documentation

### Updating Documentation

When adding new components or features:

1. **Create API documentation** in `docs/api/components/`
2. **Update examples** in `docs/guides/`
3. **Test documentation examples** to ensure they work
4. **Update main README** if needed

### Documentation Structure

```
docs/
├── api/                    # API reference documentation
│   ├── components/         # Individual component docs
│   └── setup.md           # Setup and configuration
├── guides/                # User guides and tutorials
├── internals/             # Internal documentation
└── README.md              # Documentation hub
```

This development guide provides maintainers with all the information needed to work effectively on the Dashkit codebase.