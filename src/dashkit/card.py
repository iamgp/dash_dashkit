from collections.abc import Sequence

from dash import html
from dash.development.base_component import Component
from dash.html.Section import Section
from dash_iconify import DashIconify

Children = Component | Sequence[Component] | str | Section


def Card(
    children: Children,
    header: Children | None = None,
    footer: Children | None = None,
    className: str = "",
    header_className: str | None = None,
    body_className: str | None = None,
    **kwargs,
) -> Component:
    header_base = (
        "flex flex-wrap items-center justify-between gap-4 px-6 py-4 "
        "[&:has(+footer)]:border-b [&:has(+footer)]:border-ceramic-bg-separator "
        "text-ceramic-secondary leading-5 "
    )
    return html.Section(
        children=[
            (
                html.Header(
                    children=header,
                    className=(header_base + (header_className.strip() if header_className else "")).strip(),
                )
                if header
                else None
            ),
            html.Div(
                children=html.Div(
                    children=children,
                    className=(
                        ("flex flex-col " + (body_className.strip() if body_className else "px-6 py-2")).strip()
                    ),
                ),
                className="bg-white dark:bg-dashkit-surface overflow-hidden rounded-2xl ring-1 ring-[#191C21]/4 dark:ring-ceramic-black/20 shadow-[0_1px_2px_0_rgba(25,28,33,.06),0_0_2px_0_theme(colors.ceramic.black/.08)] dark:shadow-[inset_0_0_1px_1px_theme(colors.ceramic.white/.01),0_1px_3px_0_theme(colors.ceramic.black/.4),0_0_3px_0_theme(colors.ceramic.black/.2)] flex-1 min-h-0 ",
            ),
            (
                html.Footer(
                    children=html.Div(
                        children=footer,
                        className="flex items-start px-5 gap-1.5 text-ceramic-body-3 text-ceramic-secondary -mx-5 border-t border-ceramic-bg-separator  first:border-none [:where(&)]:py-3 first:[:where(&)]:pt-0 last:[:where(&)]:pb-0 flex-1 leading-5",
                    ),
                    className="px-7 pb-3 pt-4",
                )
                if footer
                else None
            ),
        ],
        className="group flex flex-col w-full h-full rounded-2xl px-[4px] [:where(&)]:py-1 bg-dashkit-panel-light dark:bg-dashkit-panel-dark "
        + className.strip(),
        **kwargs,
    )


def CardTitle(
    children: Children,
    className: str = "",
    **kwargs,
) -> html.Span:
    return html.Span(
        children=children,
        className="flex flex-wrap items-center gap-x-2 gap-y-0.5 font-medium text-ceramic-primary text-[16px] "
        + className.strip(),
    )


def CardTitleWithIcon(
    icon: str,
    children: Children,
    className: str = "",
    **kwargs,
) -> html.Span:
    return html.Span(
        children=[
            DashIconify(icon=icon, className="stroke-2"),
            CardTitle(children, className=className, **kwargs),
        ],
        className="flex flex-wrap items-center gap-x-2 gap-y-0.5 font-medium text-ceramic-primary text-[16px] "
        + className.strip(),
    )


def CardSubtitle(
    children: Children,
    className: str = "",
    **kwargs,
) -> html.Span:
    return html.Span(
        children=children,
        className="text-xs text-ceramic-secondary pr-2 " + className.strip(),
    )


def CardFooter(
    children: Children,
    className: str = "",
    **kwargs,
) -> html.Span:
    return html.Span(
        children=children,
        className="text-xs text-ceramic-secondary " + className.strip(),
    )


def MetricCard(
    title: str,
    value: str,
    trend: str | None = None,
    trend_positive: bool = True,
    className: str = "",
    **kwargs,
) -> Component:
    """
    Specialized card for displaying metrics/KPIs.

    Args:
        title: Metric title
        value: Metric value to display
        trend: Optional trend indicator (e.g., "+2.1%", "↗ +5%")
        trend_positive: Whether trend is positive (affects color)
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
        className=className,
        **kwargs,
    )


def ChartCard(
    title: str,
    chart: Children,
    className: str = "",
    **kwargs,
) -> Component:
    """
    Specialized card for displaying charts with consistent styling.

    Args:
        title: Chart title
        chart: Chart component (e.g., dmc.LineChart, dmc.BarChart, etc.)
        className: Additional CSS classes
        **kwargs: Additional props
    """
    return Card(
        chart,
        header=CardTitle(title),
        className=className,
        **kwargs,
    )
