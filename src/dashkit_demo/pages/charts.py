import random
from datetime import datetime, timedelta

import dash
import dash_mantine_components as dmc
from dash import html

from dashkit import Card, ChartCard, MetricCard


# Generate mock assay data
def generate_assay_data():
    """Generate mock assay data for charts"""
    start_date = datetime(2024, 1, 1)
    end_date = datetime(2024, 12, 31)

    # Daily assay counts over time
    daily_data = []
    current_date = start_date
    while current_date <= end_date:
        # Add some seasonality and trends
        base_count = 50 + random.randint(-10, 15)
        if current_date.weekday() >= 5:  # Weekend reduction
            base_count = int(base_count * 0.3)

        daily_data.append(
            {
                "date": current_date.strftime("%Y-%m-%d"),
                "assays": base_count,
                "passed": int(base_count * (0.85 + random.uniform(-0.1, 0.1))),
                "failed": None,
            }
        )
        daily_data[-1]["failed"] = daily_data[-1]["assays"] - daily_data[-1]["passed"]
        current_date += timedelta(days=1)

    return daily_data


def generate_weekly_pass_fail_data():
    """Generate weekly pass/fail summary"""
    data = []
    for week in range(1, 53):
        total_assays = random.randint(300, 500)
        passed = int(total_assays * (0.85 + random.uniform(-0.15, 0.1)))
        failed = total_assays - passed

        data.append(
            {
                "week": f"Week {week}",
                "passed": passed,
                "failed": failed,
                "total": total_assays,
            }
        )

    return data


def generate_assay_type_data():
    """Generate assay type distribution"""
    assay_types = [
        "PCR",
        "ELISA",
        "Western Blot",
        "qPCR",
        "Immunoassay",
        "Flow Cytometry",
    ]
    data = []

    for assay_type in assay_types:
        count = random.randint(500, 2000)
        data.append(
            {
                "type": assay_type,
                "count": count,
                "percentage": count / 8000 * 100,  # Rough percentage
            }
        )

    return data


def generate_monthly_efficiency_data():
    """Generate monthly efficiency trends"""
    months = [
        "Jan",
        "Feb",
        "Mar",
        "Apr",
        "May",
        "Jun",
        "Jul",
        "Aug",
        "Sep",
        "Oct",
        "Nov",
        "Dec",
    ]
    data = []

    for month in months:
        efficiency = 85 + random.uniform(-8, 10)
        throughput = random.randint(800, 1200)

        data.append(
            {
                "month": month,
                "efficiency": round(efficiency, 1),
                "throughput": throughput,
            }
        )

    return data


# Generate all data
daily_assays = generate_assay_data()
weekly_data = generate_weekly_pass_fail_data()
assay_types = generate_assay_type_data()
monthly_efficiency = generate_monthly_efficiency_data()

# Register page
dash.register_page(
    __name__,
    path="/charts",
    title="Analytics Dashboard",
    icon="chart-line",
)

layout = html.Div(
    [
        html.Div(
            [
                html.H1("Analytics Dashboard", className="text-2xl font-semibold mb-2"),
                html.P(
                    "Laboratory assay metrics and performance indicators (Now with shadcn/ui charts!)",
                    className="text-dashkit-text dark:text-dashkit-text-invert mb-6",
                ),
            ]
        ),
        # First row - Time series charts (existing DMC charts)
        html.Div(
            [
                # Daily assays over time
                ChartCard(
                    title="Daily Assay Volume (DMC)",
                    chart=dmc.LineChart(
                        h=300,
                        data=[
                            {"date": d["date"], "Assays": d["assays"]}
                            for d in daily_assays[-90:]
                        ],  # Last 90 days
                        dataKey="date",
                        series=[{"name": "Assays", "color": "blue.6"}],
                        curveType="monotone",
                        strokeWidth=2,
                        withDots=False,
                        withTooltip=True,
                        tooltipAnimationDuration=200,
                    ),
                    grid_cols=1,
                ),
                # Weekly pass/fail rates
                ChartCard(
                    title="Weekly Pass/Fail Analysis (DMC)",
                    chart=dmc.BarChart(
                        h=300,
                        data=[
                            {
                                "week": w["week"],
                                "Passed": w["passed"],
                                "Failed": w["failed"],
                            }
                            for w in weekly_data[-12:]
                        ],  # Last 12 weeks
                        dataKey="week",
                        series=[
                            {"name": "Passed", "color": "green.6"},
                            {"name": "Failed", "color": "red.6"},
                        ],
                        withTooltip=True,
                        tooltipAnimationDuration=200,
                    ),
                    grid_cols=1,
                ),
            ],
            className="grid grid-cols-1 lg:grid-cols-2 gap-6 mb-6",
        ),
        # Second row - Distribution and trends
        html.Div(
            [
                # Assay type distribution (donut chart)
                ChartCard(
                    title="Assay Type Distribution (DMC)",
                    chart=dmc.DonutChart(
                        h=300,
                        data=[
                            {
                                "name": a["type"],
                                "value": a["count"],
                                "color": f"blue.{i + 1}",
                            }
                            for i, a in enumerate(assay_types)
                        ],
                        withTooltip=True,
                        tooltipDataSource="segment",
                        mx="auto",
                    ),
                    grid_cols=1,
                ),
                # Monthly efficiency trends (area chart)
                ChartCard(
                    title="Monthly Lab Efficiency (DMC)",
                    chart=dmc.AreaChart(
                        h=300,
                        data=[
                            {
                                "month": m["month"],
                                "Efficiency": m["efficiency"],
                                "Throughput": m["throughput"] / 10,
                            }
                            for m in monthly_efficiency
                        ],
                        dataKey="month",
                        series=[
                            {"name": "Efficiency", "color": "indigo.6"},
                            {"name": "Throughput (×10)", "color": "teal.6"},
                        ],
                        withTooltip=True,
                        tooltipAnimationDuration=200,
                        curveType="monotone",
                        fillOpacity=0.3,
                        withGradient=True,
                    ),
                    grid_cols=1,
                ),
            ],
            className="grid grid-cols-1 lg:grid-cols-2 gap-6 mb-6",
        ),
        # Third row - Summary metrics
        Card(
            [
                html.H3(
                    "Key Performance Indicators",
                    className="text-lg font-medium mb-4",
                ),
                html.Div(
                    [
                        MetricCard(
                            title="Success Rate",
                            value="87.3%",
                            trend="+1.2%",
                            trend_positive=True,
                            grid_cols=1,
                        ),
                        MetricCard(
                            title="Total Assays",
                            value="12,847",
                            trend="+247",
                            trend_positive=True,
                            grid_cols=1,
                        ),
                        MetricCard(
                            title="Avg Daily Volume",
                            value="47",
                            trend="-3",
                            trend_positive=False,
                            grid_cols=1,
                        ),
                        MetricCard(
                            title="Efficiency Trend",
                            value="91.2%",
                            trend="↗ +2.1%",
                            trend_positive=True,
                            grid_cols=1,
                        ),
                    ],
                    className="grid grid-cols-2 lg:grid-cols-4 gap-4",
                ),
            ],
            grid_cols="full",
        ),
    ],
    className="space-y-6",
)
