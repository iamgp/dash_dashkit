# AUTO GENERATED FILE - DO NOT EDIT

export contributiongraphblock

"""
    contributiongraphblock(;kwargs...)

A ContributionGraphBlock component.
ContributionGraphBlock represents a single day in the contribution calendar.
Keyword arguments:
- `id` (String; optional): The ID used to identify this component in Dash callbacks.
- `activity` (Real; optional): Activity level (0-4)
- `className` (String; optional): Custom CSS class
- `count` (Real; optional): Count of contributions
- `date` (String; optional): Date string in ISO format
- `dayIndex` (Real; optional): Day index in the week (0-6)
- `margin` (Real; optional): Block margin in pixels
- `onClick` (optional): Click handler
- `radius` (Real; optional): Block border radius in pixels
- `setProps` (optional): Callback used by Dash to push prop changes from the client
- `size` (Real; optional): Block size in pixels
- `style` (Bool | Real | String | Dict | Array; optional): Custom styling
- `weekIndex` (Real; optional): Week index in the calendar
"""
function contributiongraphblock(; kwargs...)
        available_props = Symbol[:id, :activity, :className, :count, :date, :dayIndex, :margin, :onClick, :radius, :size, :style, :weekIndex]
        wild_props = Symbol[]
        return Component("contributiongraphblock", "ContributionGraphBlock", "dashkit_kiboui", available_props, wild_props; kwargs...)
end

