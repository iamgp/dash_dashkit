# AUTO GENERATED FILE - DO NOT EDIT

#' @export
barChart <- function(children=NULL, id=NULL, className=NULL, config=NULL, data=NULL, dataKey=NULL, maxBarSize=NULL, radius=NULL, showGrid=NULL, showLegend=NULL, showTooltip=NULL, showXAxis=NULL, showYAxis=NULL, stackId=NULL, style=NULL, xAxisKey=NULL, yAxisKey=NULL) {
    
    props <- list(children=children, id=id, className=className, config=config, data=data, dataKey=dataKey, maxBarSize=maxBarSize, radius=radius, showGrid=showGrid, showLegend=showLegend, showTooltip=showTooltip, showXAxis=showXAxis, showYAxis=showYAxis, stackId=stackId, style=style, xAxisKey=xAxisKey, yAxisKey=yAxisKey)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'BarChart',
        namespace = 'dashkit_shadcn',
        propNames = c('children', 'id', 'className', 'config', 'data', 'dataKey', 'maxBarSize', 'radius', 'showGrid', 'showLegend', 'showTooltip', 'showXAxis', 'showYAxis', 'stackId', 'style', 'xAxisKey', 'yAxisKey'),
        package = 'dashkitShadcn'
        )

    structure(component, class = c('dash_component', 'list'))
}
