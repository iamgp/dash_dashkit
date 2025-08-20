from pathlib import Path

from ._imports_ import *  # noqa: F401,F403
from .DashkitTable import DashkitTable  # noqa: F401

try:
    from importlib.metadata import version as _pkg_version
    __version__ = _pkg_version("dashkit_table")
except Exception:
    __version__ = "0.0.0"

# Get the directory of this package
_current_dir = Path(__file__).parent

# Define the JavaScript distribution files for Dash
_js_dist = [
    {"relative_package_path": "dashkit_table.js", "namespace": "dashkit_table"}
]

_js_dist.append(dict(
    dev_package_path="proptypes.js",
    dev_only=True,
    namespace="dashkit_table"
))

# Set the _js_dist attribute on the DashkitTable class so Dash can find it
DashkitTable._js_dist = _js_dist
