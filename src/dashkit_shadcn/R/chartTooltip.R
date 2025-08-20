# AUTO GENERATED FILE - DO NOT EDIT

#' @export
chartTooltip <- function(key=NULL, ref=NULL) {
    
    props <- list(key=key, ref=ref)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'ChartTooltip',
        namespace = 'dashkit_shadcn',
        propNames = c('key', 'ref'),
        package = 'dashkitShadcn'
        )

    structure(component, class = c('dash_component', 'list'))
}
