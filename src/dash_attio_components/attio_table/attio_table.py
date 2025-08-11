from typing import Any

from dash import html
from dash_attio_table import AttioTable as CustomAttioTable


def AttioTable(
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
    Modern Attio-styled table component with native Handsontable theming support.

    Args:
        id: The ID used to identify this component in Dash callbacks
        data: List of dictionaries or 2D array of table data
        columns: List of column configurations
        height: Table height in pixels
        theme_name: Handsontable theme ('ht-theme-main', 'ht-theme-main-dark', 'ht-theme-horizon', 'ht-theme-horizon-dark')
        class_name: Custom CSS class for the table container
        **kwargs: Additional Handsontable options
    """

    # Using our custom AttioTable component with latest Handsontable v16.0.1
    return CustomAttioTable(
        id=id,
        data=data or [],
        columns=columns,
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
