# Import shadcn/ui chart components to register them with Dash
from dashkit_shadcn import AreaChart, BarChart, ChartContainer  # noqa: F401

# Re-export for convenience
__all__ = ["AreaChart", "BarChart", "ChartContainer"]
