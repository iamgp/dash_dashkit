# dashkit_kiboui

Contribution graph components for Dash (GitHub-like heatmap calendar and blocks).

## Install

```bash
pip install dashkit_kiboui
```

## Usage

```python
from dash import Dash, html
from dashkit_kiboui import ContributionGraph

app = Dash(__name__)

data = [
    {"date": "2025-01-01", "count": 1},
    {"date": "2025-01-02", "count": 5},
]

app.layout = html.Div(
    ContributionGraph(id="cg", data=data)
)

if __name__ == "__main__":
    app.run(debug=True)
```

## License
MIT
