# AUTO GENERATED FILE - DO NOT EDIT

export attiotable

"""
    attiotable(;kwargs...)

An AttioTable component.

Keyword arguments:
- `id` (String; optional): The ID used to identify this component in Dash callbacks
- `cellClassName` (String; optional): Custom CSS class for table cells
- `className` (String; optional): Custom CSS class for the table container
- `colHeaders` (Bool | Real | String | Dict | Array; optional): Show column headers
- `columnSorting` (Bool | Real | String | Dict | Array; optional): Enable column sorting
- `columns` (Array of Bool | Real | String | Dict | Arrays; optional): Column configuration
- `contextMenu` (Bool | Real | String | Dict | Array; optional): Enable context menu
- `data` (Array of Array of Bool | Real | String | Dict | Arrayss; optional): Data for the table
- `dropdownMenu` (Bool | Real | String | Dict | Array; optional): Enable dropdown menu
- `filters` (Bool | Real | String | Dict | Array; optional): Enable filters
- `headerClassName` (String; optional): Custom CSS class for headers
- `height` (String | Real; optional): Table height
- `licenseKey` (String; optional): License key for Handsontable
- `multiColumnSorting` (Bool | Real | String | Dict | Array; optional): Enable multi-column sorting
- `rowHeaders` (Bool | Real | String | Dict | Array; optional): Show row headers
- `rowHeight` (Real; optional): Custom row height
- `setProps` (optional): Callback when data changes
- `settings` (Bool | Real | String | Dict | Array; optional): Any additional Handsontable settings
- `stretchH` (String; optional): Stretch columns to fill container
- `themeName` (String; optional): Theme name - supports Handsontable native themes
- `width` (String | Real; optional): Table width
"""
function attiotable(; kwargs...)
        available_props = Symbol[:id, :cellClassName, :className, :colHeaders, :columnSorting, :columns, :contextMenu, :data, :dropdownMenu, :filters, :headerClassName, :height, :licenseKey, :multiColumnSorting, :rowHeaders, :rowHeight, :settings, :stretchH, :themeName, :width]
        wild_props = Symbol[]
        return Component("attiotable", "AttioTable", "dash_attio_table", available_props, wild_props; kwargs...)
end

