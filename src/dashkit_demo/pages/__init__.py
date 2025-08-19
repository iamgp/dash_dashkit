# Import pages to register them
from . import companies as companies
from . import contributions as contributions
from . import reports as reports

# Container configuration for main pages
CONTAINER_CONFIG = {"icon": "home", "order": 0}

__all__ = ["companies", "reports", "contributions"]
