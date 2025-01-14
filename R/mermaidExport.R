# AUTO GENERATED FILE - DO NOT EDIT

#' @export
mermaidExport <- function(id=NULL, chart=NULL, className=NULL, config=NULL, export_trigger=NULL) {
    
    props <- list(id=id, chart=chart, className=className, config=config, export_trigger=export_trigger)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'Mermaid_export',
        namespace = 'dash_diagram',
        propNames = c('id', 'chart', 'className', 'config', 'export_trigger'),
        package = 'dashDiagram'
        )

    structure(component, class = c('dash_component', 'list'))
}
