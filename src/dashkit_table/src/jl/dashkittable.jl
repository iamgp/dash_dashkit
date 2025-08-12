# AUTO GENERATED FILE - DO NOT EDIT

export dashkittable

"""
    dashkittable(;kwargs...)

A DashkitTable component.
DashkitTable is a modern Handsontable component for Dash with native theme support.
*
Provides a full-featured data grid with ergonomic defaults and theme-aware styling.
Supports both record-style rows and 2D arrays. Pass additional Handsontable options via `settings`.
Keyword arguments:
- `id` (String; optional): The ID used to identify this component in Dash callbacks.
- `cellClassName` (String; optional): Custom CSS class applied to all table cells.
- `className` (String; optional): Custom CSS class for the outer table container.
- `colHeaders` (Bool | Real | String | Dict | Array; optional): Show column headers.
- `columnSorting` (Bool | Real | String | Dict | Array; optional): Enable single-column sorting.
- `columns` (Array of Bool | Real | String | Dict | Arrays; optional): Column configuration passed through to Handsontable.
- `contextMenu` (Bool | Real | String | Dict | Array; optional): Enable context menu.
- `data` (Array of Bool | Real | String | Dict | Arrays | Array of Array of Bool | Real | String | Dict | Arrayss; optional): Data for the table. Accepts either:
- Array of objects (records) when used with column definitions using `data: <fieldName>`
- 2D array (matrix) when used with index-based columns (`data: <columnIndex>`)
- `dropdownMenu` (Bool | Real | String | Dict | Array; optional): Enable dropdown menu.
- `filters` (Bool | Real | String | Dict | Array; optional): Enable filter functionality.
- `headerClassName` (String; optional): Custom CSS class applied to all column/row headers.
- `height` (String | Real; optional): Table height in pixels or CSS size.
- `licenseKey` (String; optional): Handsontable license key string.
- `multiColumnSorting` (Bool | Real | String | Dict | Array; optional): Enable multi-column sorting.
- `rowHeaders` (Bool | Real | String | Dict | Array; optional): Show row headers.
- `rowHeight` (Real; optional): Row height in pixels.
- `setProps` (optional): Callback used by Dash to push prop changes from the client.
- `settings` (Bool | Real | String | Dict | Array; optional): Additional Handsontable settings to merge into the base config.
- `stretchH` (String; optional): Column stretching behaviour.
- `themeName` (String; optional): Theme name for native Handsontable themes (e.g. `ht-theme-main`, `ht-theme-horizon`).
- `width` (String | Real; optional): Table width in pixels or CSS size.
"""
function dashkittable(; kwargs...)
        available_props = Symbol[:id, :cellClassName, :className, :colHeaders, :columnSorting, :columns, :contextMenu, :data, :dropdownMenu, :filters, :headerClassName, :height, :licenseKey, :multiColumnSorting, :rowHeaders, :rowHeight, :settings, :stretchH, :themeName, :width]
        wild_props = Symbol[]
        return Component("dashkittable", "DashkitTable", "dashkit_table", available_props, wild_props; kwargs...)
end

