# AUTO GENERATED FILE - DO NOT EDIT

#' @export
contributionGraph <- function(children=NULL, id=NULL, className=NULL, data=NULL, style=NULL) {
    
    props <- list(children=children, id=id, className=className, data=data, style=style)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'ContributionGraph',
        namespace = 'dashkit_kiboui',
        propNames = c('children', 'id', 'className', 'data', 'style'),
        package = 'dashkitKiboui'
        )

    structure(component, class = c('dash_component', 'list'))
}
