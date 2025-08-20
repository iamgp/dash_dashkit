# dashkit_shadcn

Shadcn/ui inspired chart components for Dash (AreaChart, BarChart, ChartContainer, etc.).

## Install

```bash
pip install dashkit_shadcn
```

## Usage

```python
from dash import Dash, html
from dashkit_shadcn import AreaChart, ChartContainer

app = Dash(__name__)

app.layout = ChartContainer(
    children=[
        AreaChart(
            id="chart",
            data=[{"x": 1, "y": 3}, {"x": 2, "y": 5}],
            xKey="x",
            yKey="y",
        )
    ]
)

if __name__ == "__main__":
    app.run(debug=True)
```

## License
MIT
