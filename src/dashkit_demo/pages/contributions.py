import random
from datetime import datetime, timedelta

import dash
import dash_bootstrap_components as dbc
from dash import html

from dashkit_kiboui import ContributionGraph, ContributionGraphCalendar

# Register the page
dash.register_page(
    __name__, path="/contributions", title="Contributions", icon="chart-line"
)


def generate_sample_data(months=12):
    """Generate sample contribution data for the past N months"""
    data = []
    start_date = datetime.now() - timedelta(days=30 * months)

    for i in range(30 * months):
        date = start_date + timedelta(days=i)
        count = random.randint(0, 20) if random.random() > 0.3 else 0
        data.append({"date": date.strftime("%Y-%m-%d"), "count": count})

    return data


def layout():
    sample_data = generate_sample_data(12)  # 12 months of data
    total_contributions = sum(d["count"] for d in sample_data)

    return dbc.Container(
        [
            dbc.Row(
                [
                    dbc.Col(
                        [
                            html.H1("Contribution Graph Demo", className="mb-4"),
                            html.P(
                                "GitHub-style contribution graph using Kibo UI components.",
                                className="text-muted mb-4",
                            ),
                        ]
                    )
                ]
            ),
            dbc.Row(
                [
                    dbc.Col(
                        [
                            dbc.Card(
                                [
                                    dbc.CardHeader(
                                        [html.H4("Activity Overview", className="mb-0")]
                                    ),
                                    dbc.CardBody(
                                        [
                                            html.P(
                                                f"Total contributions in the last year: {total_contributions:,}",
                                                className="lead mb-3",
                                            ),
                                            ContributionGraph(
                                                id="main-contribution-graph",
                                                data=sample_data,
                                                children=[
                                                    ContributionGraphCalendar(
                                                        id="main-calendar",
                                                        data=sample_data,
                                                        monthsToShow=12,
                                                        blockSize=11,
                                                        blockMargin=3,
                                                        blockRadius=2,
                                                        showMonthLabels=True,
                                                        showWeekdayLabels=True,
                                                        showTooltips=True,
                                                        tooltipFormat="💻 {count} commits on {dayName}, {monthName} {date}",
                                                    )
                                                ],
                                            ),
                                        ]
                                    ),
                                ]
                            )
                        ]
                    )
                ],
                className="mb-4",
            ),
        ],
        fluid=True,
    )
