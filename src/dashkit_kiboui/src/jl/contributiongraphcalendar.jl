# AUTO GENERATED FILE - DO NOT EDIT

export contributiongraphcalendar

"""
    contributiongraphcalendar(;kwargs...)
    contributiongraphcalendar(children::Any;kwargs...)
    contributiongraphcalendar(children_maker::Function;kwargs...)


A ContributionGraphCalendar component.
ContributionGraphCalendar renders the calendar grid for contributions.
Keyword arguments:
- `children` (String | Real; optional): Children render function or components
- `id` (String; optional): The ID used to identify this component in Dash callbacks.
- `blockMargin` (Real; optional): Block margin in pixels
- `blockRadius` (Real; optional): Block border radius in pixels
- `blockSize` (Real; optional): Block size in pixels
- `className` (String; optional): Custom CSS class
- `data` (Bool | Real | String | Dict | Array; optional): Array of contribution data
- `monthsToShow` (Real; optional): Number of months to show
- `setProps` (optional): Callback used by Dash to push prop changes from the client
- `showMonthLabels` (Bool | Real | String | Dict | Array; optional): Show month labels
- `showTooltips` (Bool | Real | String | Dict | Array; optional): Enable tooltips
- `showWeekdayLabels` (Bool | Real | String | Dict | Array; optional): Show weekday labels
- `tooltipFormat` (String; optional): Custom tooltip format string. Use {count}, {date}, {dayName}, {monthName}, {year} as placeholders
"""
function contributiongraphcalendar(; kwargs...)
        available_props = Symbol[:children, :id, :blockMargin, :blockRadius, :blockSize, :className, :data, :monthsToShow, :showMonthLabels, :showTooltips, :showWeekdayLabels, :tooltipFormat]
        wild_props = Symbol[]
        return Component("contributiongraphcalendar", "ContributionGraphCalendar", "dashkit_kiboui", available_props, wild_props; kwargs...)
end

contributiongraphcalendar(children::Any; kwargs...) = contributiongraphcalendar(;kwargs..., children = children)
contributiongraphcalendar(children_maker::Function; kwargs...) = contributiongraphcalendar(children_maker(); kwargs...)

