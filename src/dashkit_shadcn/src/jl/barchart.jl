# AUTO GENERATED FILE - DO NOT EDIT

export barchart

"""
    barchart(;kwargs...)
    barchart(children::Any;kwargs...)
    barchart(children_maker::Function;kwargs...)


A BarChart component.
BarChart renders a bar chart using shadcn/ui styling and Recharts.
Keyword arguments:
- `children` (a list of or a singular dash component, string or number; optional): Children components
- `id` (String; optional): The ID used to identify this component in Dash callbacks.
- `className` (String; optional): Custom CSS class for the container
- `config` (Dict; optional): Chart configuration object with data key mappings and colors
- `data` (Array of Dicts; optional): Array of data points for the chart
- `dataKey` (String; optional): The key in data objects to use for the bar values
- `maxBarSize` (Real; optional): Maximum bar size
- `radius` (Real; optional): Border radius for the bars
- `setProps` (optional): Callback used by Dash to push prop changes from the client
- `showGrid` (Bool | Real | String | Dict | Array; optional): Whether to show the grid
- `showLegend` (Bool | Real | String | Dict | Array; optional): Whether to show the legend
- `showTooltip` (Bool | Real | String | Dict | Array; optional): Whether to show tooltips
- `showXAxis` (Bool | Real | String | Dict | Array; optional): Whether to show the x-axis
- `showYAxis` (Bool | Real | String | Dict | Array; optional): Whether to show the y-axis
- `stackId` (String; optional): Stack ID for stacked bars
- `style` (Bool | Real | String | Dict | Array; optional): Custom styling
- `xAxisKey` (String; optional): The key in data objects to use for x-axis labels
- `yAxisKey` (String; optional): The key in data objects to use for y-axis labels
"""
function barchart(; kwargs...)
        available_props = Symbol[:children, :id, :className, :config, :data, :dataKey, :maxBarSize, :radius, :showGrid, :showLegend, :showTooltip, :showXAxis, :showYAxis, :stackId, :style, :xAxisKey, :yAxisKey]
        wild_props = Symbol[]
        return Component("barchart", "BarChart", "dashkit_shadcn", available_props, wild_props; kwargs...)
end

barchart(children::Any; kwargs...) = barchart(;kwargs..., children = children)
barchart(children_maker::Function; kwargs...) = barchart(children_maker(); kwargs...)

