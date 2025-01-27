# AUTO GENERATED FILE - DO NOT EDIT

#' @export
litegraph <- function(id=NULL, autostart=NULL, className=NULL, connections=NULL, height=NULL, lastConnectionChange=NULL, lastNodeAdded=NULL, lastNodeRemoved=NULL, nodeDblClicked=NULL, nodes=NULL, onConnectionChange=NULL, onNodeAdded=NULL, onNodeDblClicked=NULL, onNodeRemoved=NULL, serialize=NULL, serializedGraph=NULL, width=NULL) {
    
    props <- list(id=id, autostart=autostart, className=className, connections=connections, height=height, lastConnectionChange=lastConnectionChange, lastNodeAdded=lastNodeAdded, lastNodeRemoved=lastNodeRemoved, nodeDblClicked=nodeDblClicked, nodes=nodes, onConnectionChange=onConnectionChange, onNodeAdded=onNodeAdded, onNodeDblClicked=onNodeDblClicked, onNodeRemoved=onNodeRemoved, serialize=serialize, serializedGraph=serializedGraph, width=width)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'Litegraph',
        namespace = 'dash_diagram',
        propNames = c('id', 'autostart', 'className', 'connections', 'height', 'lastConnectionChange', 'lastNodeAdded', 'lastNodeRemoved', 'nodeDblClicked', 'nodes', 'onConnectionChange', 'onNodeAdded', 'onNodeDblClicked', 'onNodeRemoved', 'serialize', 'serializedGraph', 'width'),
        package = 'dashDiagram'
        )

    structure(component, class = c('dash_component', 'list'))
}
