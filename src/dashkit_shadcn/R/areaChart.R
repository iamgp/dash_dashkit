# AUTO GENERATED FILE - DO NOT EDIT

#' @export
areaChart <- function(children=NULL, id=NULL, className=NULL, config=NULL, curve=NULL, data=NULL, dataKey=NULL, fillOpacity=NULL, showGrid=NULL, showLegend=NULL, showTooltip=NULL, showXAxis=NULL, showYAxis=NULL, stackId=NULL, strokeWidth=NULL, style=NULL, xAxisKey=NULL, yAxisKey=NULL) {
    
    props <- list(children=children, id=id, className=className, config=config, curve=curve, data=data, dataKey=dataKey, fillOpacity=fillOpacity, showGrid=showGrid, showLegend=showLegend, showTooltip=showTooltip, showXAxis=showXAxis, showYAxis=showYAxis, stackId=stackId, strokeWidth=strokeWidth, style=style, xAxisKey=xAxisKey, yAxisKey=yAxisKey)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'AreaChart',
        namespace = 'dashkit_shadcn',
        propNames = c('children', 'id', 'className', 'config', 'curve', 'data', 'dataKey', 'fillOpacity', 'showGrid', 'showLegend', 'showTooltip', 'showXAxis', 'showYAxis', 'stackId', 'strokeWidth', 'style', 'xAxisKey', 'yAxisKey'),
        package = 'dashkitShadcn'
        )

    structure(component, class = c('dash_component', 'list'))
}
