from dash import html, dcc
from dash_handsontable import HotTable


def AttioTableModern(
    data=None,
    columns=None,
    height=400,
    theme_name="ht-theme-main",
    cell_class_name="",
    header_class_name="",
    class_name="",
    row_height=35,
    row_headers=False,
    col_headers=True,
    context_menu=False,
    allow_empty=True,
    fill_handle=False,
    **kwargs
):
    """
    Modern Attio-styled table component with native Handsontable theming support.
    
    Args:
        data: List of dictionaries or 2D array of table data
        columns: List of column configurations
        height: Table height in pixels
        theme_name: Handsontable theme ('ht-theme-main', 'ht-theme-main-dark', 'ht-theme-horizon', 'ht-theme-horizon-dark')
        cell_class_name: Custom CSS class for table cells
        header_class_name: Custom CSS class for headers
        class_name: Custom CSS class for the table container
        row_height: Custom row height in pixels
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
    theme_css = f"""
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/handsontable@16.0.1/styles/handsontable.min.css" />
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/handsontable@16.0.1/styles/{theme_name}.min.css" />
    <style>
        .attio-table-modern {{
            font-family: Inter, -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
        }}
        
        .{theme_name} .handsontable tbody td,
        .{theme_name} .handsontable .ht_clone_left td {{
            height: {row_height}px !important;
            font-family: Inter !important;
            letter-spacing: -0.02em !important;
            font-weight: 500 !important;
            line-height: 20px !important;
            font-size: 14px !important;
            color: #1f2937 !important;
            border-bottom: 1px solid #f9fafb !important;
            border-right: none !important;
            padding: 7.5px 8px !important;
            overflow: hidden !important;
            text-overflow: ellipsis !important;
            white-space: nowrap !important;
        }}
        
        .{theme_name} .handsontable thead th,
        .{theme_name} .handsontable .ht_clone_top th {{
            height: {row_height}px !important;
            font-family: Inter !important;
            font-weight: 600 !important;
            font-size: 12px !important;
            color: #6b7280 !important;
            background: #f9fafb !important;
            border-bottom: 1px solid #e5e7eb !important;
            text-transform: uppercase !important;
            letter-spacing: 0.05em !important;
        }}
        
        .{theme_name} .handsontable tr:hover td {{
            background-color: #f8fafc !important;
        }}
        
        .{theme_name} .handsontable {{
            border: 1px solid #e5e7eb !important;
            border-radius: 8px !important;
            overflow: hidden !important;
        }}
        
        .attio-table-container.{theme_name} {{
            border-radius: 8px;
            overflow: hidden;
            box-shadow: 0 1px 3px 0 rgb(0 0 0 / 0.1);
        }}
    </style>
    """
    
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
        'height': f'{height}px' if isinstance(height, int) else str(height)
    })