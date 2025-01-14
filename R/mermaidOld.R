# AUTO GENERATED FILE - DO NOT EDIT

#' @export
mermaidOld <- function(id=NULL, chart=NULL, className=NULL, config=NULL) {
    
    props <- list(id=id, chart=chart, className=className, config=config)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'Mermaid_old',
        namespace = 'dash_diagram',
        propNames = c('id', 'chart', 'className', 'config'),
        package = 'dashDiagram'
        )

    structure(component, class = c('dash_component', 'list'))
}
