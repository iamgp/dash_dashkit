# AUTO GENERATED FILE - DO NOT EDIT

export dashkittable

"""
    dashkittable(;kwargs...)

A DashkitTable component.

Keyword arguments:
- `id` (String; optional)
- `cellClassName` (String; optional)
- `className` (String; optional)
- `colHeaders` (Bool | Real | String | Dict | Array; optional)
- `columnSorting` (Bool | Real | String | Dict | Array; optional)
- `columns` (Array of Bool | Real | String | Dict | Arrays; optional)
- `contextMenu` (Bool | Real | String | Dict | Array; optional)
- `data` (Array of Bool | Real | String | Dict | Arrays | Array of Array of Bool | Real | String | Dict | Arrayss; optional)
- `dropdownMenu` (Bool | Real | String | Dict | Array; optional)
- `filters` (Bool | Real | String | Dict | Array; optional)
- `headerClassName` (String; optional)
- `height` (String | Real; optional)
- `licenseKey` (String; optional)
- `multiColumnSorting` (Bool | Real | String | Dict | Array; optional)
- `rowHeaders` (Bool | Real | String | Dict | Array; optional)
- `rowHeight` (Real; optional)
- `setProps` (optional)
- `settings` (Bool | Real | String | Dict | Array; optional)
- `stretchH` (String; optional)
- `themeName` (String; optional)
- `width` (String | Real; optional)
"""
function dashkittable(; kwargs...)
        available_props = Symbol[:id, :cellClassName, :className, :colHeaders, :columnSorting, :columns, :contextMenu, :data, :dropdownMenu, :filters, :headerClassName, :height, :licenseKey, :multiColumnSorting, :rowHeaders, :rowHeight, :settings, :stretchH, :themeName, :width]
        wild_props = Symbol[]
        return Component("dashkittable", "DashkitTable", "dashkit_table", available_props, wild_props; kwargs...)
end

