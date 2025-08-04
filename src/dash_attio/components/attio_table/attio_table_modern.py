from typing import Any

from dash import html
from dash_handsontable import HotTable


def AttioTableModern(
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
    **kwargs: Any
) -> html.Div:
    """
    Modern Attio-styled table component with native Handsontable theming support.

    Args:
        data: List of dictionaries or 2D array of table data
        columns: List of column configurations
        height: Table height in pixels
        theme_name: Handsontable theme ('ht-theme-main', 'ht-theme-main-dark', 'ht-theme-horizon', 'ht-theme-horizon-dark')
        class_name: Custom CSS class for the table container
        **kwargs: Additional Handsontable options
    """

    # Base configuration for modern Handsontable with theming
    config = {
        "licenseKey": "non-commercial-and-evaluation",
        "data": data or [],
        "height": height,
        "rowHeaders": row_headers,
        "colHeaders": col_headers,
        "contextMenu": context_menu,
        "allowEmpty": allow_empty,
        "fillHandle": fill_handle,
        "manualColumnResize": True,
        "manualRowResize": True,
        "columnSorting": True,
        "filters": True,
        "dropdownMenu": True,
        "stretchH": "all",
        "autoWrapRow": True,
        "autoWrapCol": True,
        "className": f"{class_name} attio-table-modern {theme_name}",
        **kwargs
    }

    if columns:
        config["columns"] = columns

    # Include the theme CSS and custom styles

    return html.Div([
        HotTable(
            id=f"attio-table-{theme_name}",
            **config
        )
    ],
    className=f"attio-table-container {theme_name}",
    style={
        'borderRadius': '8px',
        'overflow': 'hidden',
        'boxShadow': '0 1px 3px 0 rgb(0 0 0 / 0.1)',
        'fontFamily': 'Inter, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif',
        'height': f'{height}px'
    })
