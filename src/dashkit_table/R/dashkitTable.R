# AUTO GENERATED FILE - DO NOT EDIT

#' @export
dashkitTable <- function(id=NULL, cellClassName=NULL, className=NULL, colHeaders=NULL, columnSorting=NULL, columns=NULL, contextMenu=NULL, data=NULL, dropdownMenu=NULL, filters=NULL, headerClassName=NULL, height=NULL, licenseKey=NULL, multiColumnSorting=NULL, rowHeaders=NULL, rowHeight=NULL, settings=NULL, stretchH=NULL, themeName=NULL, width=NULL) {
    
    props <- list(id=id, cellClassName=cellClassName, className=className, colHeaders=colHeaders, columnSorting=columnSorting, columns=columns, contextMenu=contextMenu, data=data, dropdownMenu=dropdownMenu, filters=filters, headerClassName=headerClassName, height=height, licenseKey=licenseKey, multiColumnSorting=multiColumnSorting, rowHeaders=rowHeaders, rowHeight=rowHeight, settings=settings, stretchH=stretchH, themeName=themeName, width=width)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'DashkitTable',
        namespace = 'dashkit_table',
        propNames = c('id', 'cellClassName', 'className', 'colHeaders', 'columnSorting', 'columns', 'contextMenu', 'data', 'dropdownMenu', 'filters', 'headerClassName', 'height', 'licenseKey', 'multiColumnSorting', 'rowHeaders', 'rowHeight', 'settings', 'stretchH', 'themeName', 'width'),
        package = 'dashkitTable'
        )

    structure(component, class = c('dash_component', 'list'))
}
