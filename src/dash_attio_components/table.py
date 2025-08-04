from typing import Any

from dash import html

from .attio_table import AttioTable


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
