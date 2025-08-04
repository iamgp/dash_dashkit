from typing import Any

from dash import html

from .attio_table import AttioTable


def AttioTableWithStats(
    data: list[dict[str, Any]],
    columns: list[dict[str, Any]] | None = None,
    count_label: str = "count",
    actions: list[Any] | None = None,
    **table_kwargs: Any,
) -> html.Div:
    """
    Table component with Attio-style header showing count and actions.

    Args:
        data: Table data
        columns: Column configurations
        title: Table title
        count_label: Label for the count display
        actions: List of action buttons/components
        **table_kwargs: Additional table configuration
    """

    # Calculate row count
    row_count = len(data)

    header_content = [
        # Left side - count
        html.Div(
            [
                html.Span(
                    f"{row_count} {count_label}", className="text-sm text-gray-600"
                ),
            ],
            className="flex items-center",
        ),
        # Right side - actions
        html.Div(actions or [], className="flex items-center space-x-2"),
    ]

    # Use Handsontable component
    table_component = AttioTable(data, columns, **table_kwargs)

    return html.Div(
        [
            # Header with count and actions
            html.Div(
                header_content,
                className="flex items-center justify-between px-6 py-3 border-b border-gray-200 bg-gray-50",
            ),
            # Table
            html.Div([table_component], className="overflow-x-auto"),
        ],
        className="bg-white dark:bg-[#1B1D21] border border-gray-200 dark:border-[#27282B] ",
    )


# Demo-specific functions moved to dash_attio_demo package
