import dash

from dashkit import MarkdownReport
from dashkit_demo.pages.elisa.sample_report import SAMPLE_REPORT_CONTENT

dash.register_page(
    __name__,
    path="/reports",
    title="Reports",
    icon="mynaui:chart-bar",
    sidebar_section="Main",
)

layout = MarkdownReport(
    content=SAMPLE_REPORT_CONTENT,
    title="Reports",
)
