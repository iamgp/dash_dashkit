from typing import Any

from dash import html

from .attio_table import AttioTableModern


def AttioHTMLTable(data: list[dict[str, Any]], columns: list[dict[str, Any]] | None = None, **kwargs: Any) -> html.Div | html.Table:
    """
    Create an Attio-style HTML table that supports complex content like icons, tags, and links.
    """
    if not data:
        return html.Div("No data available", className="p-4 text-gray-500")

    # Create table headers
    headers = []
    if columns:
        for col in columns:
            headers.append(
                html.Th(
                    col.get("title", col.get("data", "")),
                    className="px-4 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider border-b border-gray-200 bg-gray-50",
                )
            )
    else:
        # Auto-generate headers from first data row
        if data:
            for key in data[0].keys():
                headers.append(
                    html.Th(
                        key.replace("_", " ").title(),
                        className="px-4 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider border-b border-gray-200 bg-gray-50",
                    )
                )

    # Create table rows
    rows = []
    for row_data in data:
        cells = []
        if columns:
            for col in columns:
                data_key = col.get("data", "")
                cell_value = row_data.get(data_key, "")
                cell_class = (
                    f"px-4 py-3 border-b border-gray-100 {col.get('className', '')}"
                )
                cells.append(html.Td(cell_value, className=cell_class))
        else:
            for value in row_data.values():
                cells.append(
                    html.Td(value, className="px-4 py-3 border-b border-gray-100")
                )

        rows.append(html.Tr(cells, className="hover:bg-gray-50"))

    return html.Table(
        [html.Thead(html.Tr(headers)), html.Tbody(rows)],
        className="min-w-full bg-white",
    )


def AttioTable(
    data: list[dict[str, Any]],
    columns: list[dict[str, Any]] | None = None,
    height: int = 400,
    theme_name: str = "ht-theme-horizon",
    row_headers: bool = False,
    col_headers: bool = True,
    context_menu: bool = False,
    allow_empty: bool = True,
    fill_handle: bool = False,
    **kwargs: Any,
) -> html.Div:
    """
    Modern Attio-styled table component using latest Handsontable with native theming.

    Args:
        data: List of dictionaries or 2D array of table data
        columns: List of column configurations
        height: Table height in pixels
        theme_name: Handsontable theme ('ht-theme-main', 'ht-theme-main-dark', 'ht-theme-horizon', 'ht-theme-horizon-dark')
        row_headers: Show row numbers
        col_headers: Show column headers
        context_menu: Enable right-click context menu
        allow_empty: Allow empty cells
        fill_handle: Enable Excel-like fill handle
        **kwargs: Additional Handsontable options
    """

    return AttioTableModern(
        data=data,
        columns=columns,
        height=height,
        theme_name=theme_name,
        row_headers=row_headers,
        col_headers=col_headers,
        context_menu=context_menu,
        allow_empty=allow_empty,
        fill_handle=fill_handle,
        **kwargs,
    )


def AttioTableWithStats(
    data: list[dict[str, Any]],
    columns: list[dict[str, Any]] | None = None,
    count_label: str = "count",
    actions: list[Any] | None = None,
    **table_kwargs: Any
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
        className="bg-white border border-gray-200 rounded-lg shadow-sm",
    )


def create_company_columns() -> list[dict[str, Any]]:
    """Create column configuration for the companies table matching Attio style."""
    return [
        {
            "data": "company_name",
            "title": "Company",
            "type": "text",
            "className": "attio-cell attio-primary-cell",
            "width": 200,
        },
        {
            "data": "categories",
            "title": "Categories",
            "type": "text",
            "className": "attio-cell attio-categories-cell",
            "width": 300,
        },
        {
            "data": "linkedin",
            "title": "LinkedIn",
            "type": "text",
            "className": "attio-cell attio-link-cell",
            "width": 120,
        },
        {
            "data": "last_interaction",
            "title": "Last interaction",
            "type": "text",
            "className": "attio-cell attio-center-cell",
            "width": 150,
        },
        {
            "data": "connection_strength",
            "title": "Connection strength",
            "type": "text",
            "className": "attio-cell attio-center-cell",
            "width": 150,
        },
        {
            "data": "twitter_followers",
            "title": "Twitter followers",
            "type": "numeric",
            "className": "attio-cell attio-right-cell",
            "width": 150,
        },
        {
            "data": "twitter_handle",
            "title": "Twitter",
            "type": "text",
            "className": "attio-cell attio-link-cell",
            "width": 120,
        },
    ]


def format_company_data(companies: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """Format company data for Handsontable with proper string representations."""
    formatted_data = []

    for company in companies:
        # Format company name with icon as string for Handsontable
        company_name = f"{company.get('icon', '')} {company.get('name', '')}"

        # Format categories as comma-separated string (we'll style with CSS)
        categories = company.get("categories", [])
        if categories and isinstance(categories[0], dict):
            category_names = [cat["name"] for cat in categories]
            categories_str = ", ".join(category_names)
        else:
            categories_str = ", ".join(categories)

        # LinkedIn and Twitter as simple strings
        linkedin = company.get("linkedin", "No contact")
        twitter_handle = company.get("twitter_handle", "")

        formatted_data.append(
            {
                "company_name": company_name,
                "categories": categories_str,
                "linkedin": linkedin,
                "last_interaction": company.get("last_interaction", "No communication"),
                "connection_strength": company.get("connection_strength", ""),
                "twitter_followers": company.get("twitter_followers", 0),
                "twitter_handle": twitter_handle,
            }
        )

    return formatted_data
