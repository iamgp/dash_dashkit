# Dashkit Documentation

Welcome to the Dashkit documentation! This directory contains comprehensive guides and API references for using and maintaining dash-dashkit.

## 📚 Documentation Structure

### For Users
- **[API Reference](api/README.md)** - Complete component API documentation
- **[Quick Start Guide](guides/quickstart.md)** - Get up and running quickly

### For Maintainers  
- **[Development Setup](internals/development.md)** - Local development environment
- **[Architecture Overview](internals/architecture.md)** - Understanding the codebase

## 🚀 Getting Started

If you're new to Dashkit, start with the [Quick Start Guide](guides/quickstart.md).

## 📖 Building Documentation

This documentation is built with MkDocs and Material for MkDocs theme.

### Local Development

```bash
# Install documentation dependencies
uv run task docs-install

# Serve documentation locally with hot reload
uv run task docs-serve

# Build static documentation
uv run task docs-build
```

### Deployment

Documentation is automatically deployed to GitHub Pages when changes are pushed to the main branch.

```bash
# Manual deployment to GitHub Pages
uv run task docs-deploy
```

## 📖 Additional Resources

- [Main README](../README.md) - Project overview and basic setup
- [CHANGELOG](../CHANGELOG.md) - Version history and changes  
- [PyPI Package](https://pypi.org/project/dash-dashkit/) - Official package
- [GitHub Repository](https://github.com/iamgp/dash_dashkit) - Source code and issues