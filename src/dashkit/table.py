from typing import Any

from dash import html

try:
    from dashkit_table import DashkitTable as CustomDashkitTable  # type: ignore
except Exception as _e:
    CustomDashkitTable = None  # type: ignore[assignment]
    _import_error = _e


def Table(
    id: str,
    data: list[dict[str, Any]] | None = None,
    columns: list[dict[str, Any]] | None = None,
    height: int = 400,
    theme_name: str = "ht-theme-main",
    class_name: str = "",
    row_headers: bool = False,
    col_headers: bool = True,
    context_menu: bool = False,
    allow_empty: bool = True,
    fill_handle: bool = False,
    **kwargs: Any,
) -> html.Div:
    """
    Modern dashboard table component with native Handsontable theming support.

    Args:
        id: The ID used to identify this component in Dash callbacks
        data: List of dictionaries or 2D array of table data
        columns: List of column configurations
        height: Table height in pixels
        theme_name: Handsontable theme ('ht-theme-main', 'ht-theme-main-dark', 'ht-theme-horizon', 'ht-theme-horizon-dark')
        class_name: Custom CSS class for the table container
        **kwargs: Additional Handsontable options
    """

    # If provided data is a list of dicts (records), convert to 2D array with
    # column order derived from the provided columns. Adjust columns to index-based
    # access to satisfy current PropTypes and Handsontable expectations.
    processed_data = data or []
    processed_columns = columns

    if processed_data and isinstance(processed_data[0], dict) and columns:
        column_keys = [c.get("data") for c in columns]
        # Only include keys that are strings/valid identifiers
        column_keys = [k for k in column_keys if isinstance(k, str)]

        # Build 2D array in the order of column_keys
        processed_data = [
            [row.get(key) for key in column_keys]  # type: ignore[arg-type]
            for row in processed_data  # type: ignore[assignment]
        ]

        # Convert columns to index-based access for array-of-arrays data
        processed_columns = [{**col, "data": idx} for idx, col in enumerate(columns)]

    # Using our custom table component with latest Handsontable v16.0.1
    if CustomDashkitTable is None:
        raise ImportError(
            "dashkit_table is not installed. Install it with `pip install dashkit_table` "
            "or install extras: `pip install dash-dashkit[table]`."
        ) from _import_error
    return CustomDashkitTable(
        id=id,
        data=processed_data,
        columns=processed_columns,
        height=height,
        themeName=theme_name,
        className=class_name,
        rowHeaders=row_headers,
        colHeaders=col_headers,
        contextMenu=context_menu,
        licenseKey="non-commercial-and-evaluation",
        columnSorting=True,
        filters=True,
        dropdownMenu=True,
        stretchH="all",
        **kwargs,
    )


def TableWithStats(
    data: list[dict[str, Any]],
    columns: list[dict[str, Any]] | None = None,
    count_label: str = "count",
    actions: list[Any] | None = None,
    **table_kwargs: Any,
) -> html.Div:
    """
    Table component with dashboard-style header showing count and actions.

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
    table_component = Table(id="table", data=data, columns=columns, **table_kwargs)

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
        className="bg-white dark:bg-dashkit-panel-dark border border-gray-200 dark:border-dashkit-border-dark ",
    )


# Demo-specific functions moved to dashkit_demo package
