from pathlib import Path

from ._imports_ import *  # noqa: F401,F403
from .AttioTable import AttioTable  # noqa: F401

__version__ = "1.0.0"

# Get the directory of this package
_current_dir = Path(__file__).parent

# Define the JavaScript distribution files for Dash
_js_dist = [
    {"relative_package_path": "dashkit_table.js", "namespace": "dashkit_table"}
]

# Set the _js_dist attribute on the AttioTable class so Dash can find it
AttioTable._js_dist = _js_dist
