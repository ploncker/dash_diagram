# AUTO GENERATED FILE - DO NOT EDIT

#' @export
reactflow <- function(id=NULL, className=NULL, clicked_edge=NULL, clicked_node=NULL, connect=NULL, connection_mode=NULL, default_position=NULL, default_zoom=NULL, edge_types=NULL, edges=NULL, edges_change=NULL, elements_selectable=NULL, export_trigger=NULL, fit_view=NULL, max_zoom=NULL, min_zoom=NULL, node_types=NULL, nodes=NULL, nodes_change=NULL, nodes_connectable=NULL, nodes_draggable=NULL, pan_on_drag=NULL, pan_on_scroll=NULL, snap_grid=NULL, snap_to_grid=NULL, style=NULL, zoom_on_pinch=NULL, zoom_on_scroll=NULL) {
    
    props <- list(id=id, className=className, clicked_edge=clicked_edge, clicked_node=clicked_node, connect=connect, connection_mode=connection_mode, default_position=default_position, default_zoom=default_zoom, edge_types=edge_types, edges=edges, edges_change=edges_change, elements_selectable=elements_selectable, export_trigger=export_trigger, fit_view=fit_view, max_zoom=max_zoom, min_zoom=min_zoom, node_types=node_types, nodes=nodes, nodes_change=nodes_change, nodes_connectable=nodes_connectable, nodes_draggable=nodes_draggable, pan_on_drag=pan_on_drag, pan_on_scroll=pan_on_scroll, snap_grid=snap_grid, snap_to_grid=snap_to_grid, style=style, zoom_on_pinch=zoom_on_pinch, zoom_on_scroll=zoom_on_scroll)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'Reactflow',
        namespace = 'dash_diagram',
        propNames = c('id', 'className', 'clicked_edge', 'clicked_node', 'connect', 'connection_mode', 'default_position', 'default_zoom', 'edge_types', 'edges', 'edges_change', 'elements_selectable', 'export_trigger', 'fit_view', 'max_zoom', 'min_zoom', 'node_types', 'nodes', 'nodes_change', 'nodes_connectable', 'nodes_draggable', 'pan_on_drag', 'pan_on_scroll', 'snap_grid', 'snap_to_grid', 'style', 'zoom_on_pinch', 'zoom_on_scroll'),
        package = 'dashDiagram'
        )

    structure(component, class = c('dash_component', 'list'))
}
