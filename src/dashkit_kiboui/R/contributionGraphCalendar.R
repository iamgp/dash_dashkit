# AUTO GENERATED FILE - DO NOT EDIT

#' @export
contributionGraphCalendar <- function(children=NULL, id=NULL, blockMargin=NULL, blockRadius=NULL, blockSize=NULL, className=NULL, data=NULL, monthsToShow=NULL, showMonthLabels=NULL, showTooltips=NULL, showWeekdayLabels=NULL, tooltipFormat=NULL) {
    
    props <- list(children=children, id=id, blockMargin=blockMargin, blockRadius=blockRadius, blockSize=blockSize, className=className, data=data, monthsToShow=monthsToShow, showMonthLabels=showMonthLabels, showTooltips=showTooltips, showWeekdayLabels=showWeekdayLabels, tooltipFormat=tooltipFormat)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'ContributionGraphCalendar',
        namespace = 'dashkit_kiboui',
        propNames = c('children', 'id', 'blockMargin', 'blockRadius', 'blockSize', 'className', 'data', 'monthsToShow', 'showMonthLabels', 'showTooltips', 'showWeekdayLabels', 'tooltipFormat'),
        package = 'dashkitKiboui'
        )

    structure(component, class = c('dash_component', 'list'))
}
