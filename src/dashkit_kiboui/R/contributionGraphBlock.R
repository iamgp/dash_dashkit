# AUTO GENERATED FILE - DO NOT EDIT

#' @export
contributionGraphBlock <- function(id=NULL, activity=NULL, className=NULL, count=NULL, date=NULL, dayIndex=NULL, margin=NULL, onClick=NULL, radius=NULL, size=NULL, style=NULL, weekIndex=NULL) {
    
    props <- list(id=id, activity=activity, className=className, count=count, date=date, dayIndex=dayIndex, margin=margin, onClick=onClick, radius=radius, size=size, style=style, weekIndex=weekIndex)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'ContributionGraphBlock',
        namespace = 'dashkit_kiboui',
        propNames = c('id', 'activity', 'className', 'count', 'date', 'dayIndex', 'margin', 'onClick', 'radius', 'size', 'style', 'weekIndex'),
        package = 'dashkitKiboui'
        )

    structure(component, class = c('dash_component', 'list'))
}
