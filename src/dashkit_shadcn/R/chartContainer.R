# AUTO GENERATED FILE - DO NOT EDIT

#' @export
chartContainer <- function(children=NULL, id=NULL, className=NULL, config=NULL, key=NULL, ref=NULL) {
    
    props <- list(children=children, id=id, className=className, config=config, key=key, ref=ref)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'ChartContainer',
        namespace = 'dashkit_shadcn',
        propNames = c('children', 'id', 'className', 'config', 'key', 'ref'),
        package = 'dashkitShadcn'
        )

    structure(component, class = c('dash_component', 'list'))
}
