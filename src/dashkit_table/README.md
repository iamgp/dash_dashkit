# dashkit_table

Dash component wrapping Handsontable (v16) with Dashkit-native theming and sensible defaults.

## Install

```bash
pip install dashkit_table
```

## Usage

```python
from dash import Dash, html
from dashkit_table import DashkitTable

app = Dash(__name__)

app.layout = html.Div(
    DashkitTable(
        id="table",
        data=[["Alice", 10], ["Bob", 20]],
        columns=[{"data": 0, "title": "Name"}, {"data": 1, "title": "Score"}],
        themeName="ht-theme-main",
        stretchH="all",
    )
)

if __name__ == "__main__":
    app.run(debug=True)
```

## Features
- Handsontable v16 with column sorting, filters, dropdown menu enabled by default
- Theme switching support via `themeName`
- Bundled JS assets for immediate use in Dash

## License
MIT
