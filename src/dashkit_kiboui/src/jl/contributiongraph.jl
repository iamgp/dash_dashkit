# AUTO GENERATED FILE - DO NOT EDIT

export contributiongraph

"""
    contributiongraph(;kwargs...)
    contributiongraph(children::Any;kwargs...)
    contributiongraph(children_maker::Function;kwargs...)


A ContributionGraph component.
ContributionGraph is the main container for a GitHub-style contribution graph.
This is a composable component that should contain ContributionGraphCalendar
and other contribution graph components.
Keyword arguments:
- `children` (a list of or a singular dash component, string or number; optional): Children components
- `id` (String; optional): The ID used to identify this component in Dash callbacks.
- `className` (String; optional): Custom CSS class for the container
- `data` (Bool | Real | String | Dict | Array; optional): Array of contribution data with date and count
- `setProps` (optional): Callback used by Dash to push prop changes from the client
- `style` (Bool | Real | String | Dict | Array; optional): Custom styling
"""
function contributiongraph(; kwargs...)
        available_props = Symbol[:children, :id, :className, :data, :style]
        wild_props = Symbol[]
        return Component("contributiongraph", "ContributionGraph", "dashkit_kiboui", available_props, wild_props; kwargs...)
end

contributiongraph(children::Any; kwargs...) = contributiongraph(;kwargs..., children = children)
contributiongraph(children_maker::Function; kwargs...) = contributiongraph(children_maker(); kwargs...)

