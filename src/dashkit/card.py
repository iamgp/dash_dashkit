from typing import Any, Literal

from dash import html


def Card(
    children: Any,
    className: str = "",
    title: str | None = None,
    grid_cols: Literal[1, 2, 3, 4, 6, 12, "full"] = 1,
    **kwargs: Any,
) -> html.Div:
    """
    Reusable card component with consistent dashkit styling and grid support.

    Args:
        children: Content to display inside the card
        className: Additional CSS classes
        title: Optional title to display at the top of the card
        grid_cols: Grid columns span (1-12, or "full" for col-span-full)
        **kwargs: Additional props passed to the outer div
    """
    # Map grid_cols to CSS classes
    grid_class_map = {
        1: "col-span-1",
        2: "col-span-2",
        3: "col-span-3",
        4: "col-span-4",
        6: "col-span-6",
        12: "col-span-12",
        "full": "col-span-full",
    }

    grid_class = grid_class_map.get(grid_cols, "col-span-1")

    # Base card styling with dashkit colors
    base_classes = "bg-white dark:bg-dashkit-panel-dark p-6 rounded-lg border border-dashkit-border-light dark:border-dashkit-border-dark"
    combined_classes = f"{base_classes} {grid_class} {className}".strip()

    # Build card content
    card_content = []

    # Add title if provided
    if title:
        card_content.append(
            html.H3(
                title,
                className="text-lg font-medium mb-4 text-dashkit-text dark:text-dashkit-text-invert",
            )
        )

    # Add children (can be a single element or list)
    if isinstance(children, list):
        card_content.extend(children)
    else:
        card_content.append(children)

    return html.Div(card_content, className=combined_classes, **kwargs)


def MetricCard(
    title: str,
    value: str,
    trend: str | None = None,
    trend_positive: bool = True,
    grid_cols: Literal[1, 2, 3, 4, 6, 12, "full"] = 1,
    className: str = "",
    **kwargs: Any,
) -> html.Div:
    """
    Specialized card for displaying metrics/KPIs.

    Args:
        title: Metric title
        value: Metric value to display
        trend: Optional trend indicator (e.g., "+2.1%", "↗ +5%")
        trend_positive: Whether trend is positive (affects color)
        grid_cols: Grid columns span
        className: Additional CSS classes
        **kwargs: Additional props
    """
    content = [
        html.H4(
            title,
            className="text-sm font-medium text-dashkit-text dark:text-dashkit-text-invert mb-2",
        ),
        html.P(
            value,
            className="text-2xl font-bold text-dashkit-text dark:text-dashkit-text-invert mb-1",
        ),
    ]

    # Add trend if provided
    if trend:
        trend_color = "text-green-600" if trend_positive else "text-red-600"
        content.append(
            html.P(
                trend,
                className=f"text-sm font-medium {trend_color}",
            )
        )

    return Card(
        html.Div(content, className="text-center"),
        className=f"bg-dashkit-panel-light dark:bg-dashkit-surface {className}",
        grid_cols=grid_cols,
        **kwargs,
    )


def ChartCard(
    title: str,
    chart: Any,
    grid_cols: Literal[1, 2, 3, 4, 6, 12, "full"] = 1,
    className: str = "",
    **kwargs: Any,
) -> html.Div:
    """
    Specialized card for displaying charts with consistent styling.

    Args:
        title: Chart title
        chart: Chart component (e.g., dmc.LineChart, dmc.BarChart, etc.)
        grid_cols: Grid columns span
        className: Additional CSS classes
        **kwargs: Additional props
    """
    return Card(
        [
            html.H3(
                title,
                className="text-lg font-medium mb-4 text-dashkit-text dark:text-dashkit-text-invert",
            ),
            chart,
        ],
        className=className,
        grid_cols=grid_cols,
        **kwargs,
    )
