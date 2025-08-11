# Import parent directory for components
import sys
from pathlib import Path

import dash

sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from dash_attio_components import MarkdownReport

from ..sample_report import SAMPLE_REPORT_CONTENT

dash.register_page(__name__, path="/reports", title="Reports")

layout = MarkdownReport(
    content=SAMPLE_REPORT_CONTENT, title="Q4 2024 Performance Report"
)
