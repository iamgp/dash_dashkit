# AUTO GENERATED FILE - DO NOT EDIT

export areachart

"""
    areachart(;kwargs...)
    areachart(children::Any;kwargs...)
    areachart(children_maker::Function;kwargs...)


An AreaChart component.
AreaChart renders an area chart using shadcn/ui styling and Recharts.
Keyword arguments:
- `children` (a list of or a singular dash component, string or number; optional): Children components
- `id` (String; optional): The ID used to identify this component in Dash callbacks.
- `className` (String; optional): Custom CSS class for the container
- `config` (Dict; optional): Chart configuration object with data key mappings and colors
- `curve` (String; optional): Curve type for the area
- `data` (Array of Dicts; optional): Array of data points for the chart
- `dataKey` (String; optional): The key in data objects to use for the area values
- `fillOpacity` (Real; optional): Fill opacity for the area
- `setProps` (optional): Callback used by Dash to push prop changes from the client
- `showGrid` (Bool | Real | String | Dict | Array; optional): Whether to show the grid
- `showLegend` (Bool | Real | String | Dict | Array; optional): Whether to show the legend
- `showTooltip` (Bool | Real | String | Dict | Array; optional): Whether to show tooltips
- `showXAxis` (Bool | Real | String | Dict | Array; optional): Whether to show the x-axis
- `showYAxis` (Bool | Real | String | Dict | Array; optional): Whether to show the y-axis
- `stackId` (String; optional): Stack ID for stacked areas
- `strokeWidth` (Real; optional): Stroke width for the area line
- `style` (Bool | Real | String | Dict | Array; optional): Custom styling
- `xAxisKey` (String; optional): The key in data objects to use for x-axis labels
- `yAxisKey` (String; optional): The key in data objects to use for y-axis labels
"""
function areachart(; kwargs...)
        available_props = Symbol[:children, :id, :className, :config, :curve, :data, :dataKey, :fillOpacity, :showGrid, :showLegend, :showTooltip, :showXAxis, :showYAxis, :stackId, :strokeWidth, :style, :xAxisKey, :yAxisKey]
        wild_props = Symbol[]
        return Component("areachart", "AreaChart", "dashkit_shadcn", available_props, wild_props; kwargs...)
end

areachart(children::Any; kwargs...) = areachart(;kwargs..., children = children)
areachart(children_maker::Function; kwargs...) = areachart(children_maker(); kwargs...)

