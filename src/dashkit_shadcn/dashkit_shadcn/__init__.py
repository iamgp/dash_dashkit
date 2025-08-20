from pathlib import Path
import sys

try:
    from importlib.metadata import version as _pkg_version
    __version__ = _pkg_version("dashkit_shadcn")
except Exception:
    __version__ = "0.0.0"

# Get the directory of this package
_current_dir = Path(__file__).parent

# Define the JavaScript distribution files for Dash
_js_dist = [
    {
        "relative_package_path": "dashkit_shadcn.js",
        "namespace": "dashkit_shadcn",
        "async": False
    }
]

# For development/debugging, also include the proptypes
_js_dist.append({
    "relative_package_path": "proptypes.js",
    "dev_only": True,
    "namespace": "dashkit_shadcn",
    "async": False
})

# Import the component classes and set _js_dist directly on them
from .AreaChart import AreaChart
from .BarChart import BarChart
from .ChartContainer import ChartContainer
from .ChartLegend import ChartLegend
from .ChartTooltip import ChartTooltip

# Set the _js_dist attribute on each component class so Dash can find them
AreaChart._js_dist = _js_dist
BarChart._js_dist = _js_dist
ChartContainer._js_dist = _js_dist
ChartLegend._js_dist = _js_dist
ChartTooltip._js_dist = _js_dist

# Export components so they're available at module level
__all__ = [
    "AreaChart",
    "BarChart", 
    "ChartContainer",
    "ChartLegend",
    "ChartTooltip"
]