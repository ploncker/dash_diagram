% Auto-generated: do not edit by hand
\name{reactflow}

\alias{reactflow}

\title{Reactflow component}

\description{

}

\usage{
reactflow(id=NULL, className=NULL, clicked_edge=NULL,
clicked_node=NULL, connect=NULL, connection_mode=NULL,
default_position=NULL, default_zoom=NULL, edge_types=NULL,
edges=NULL, edges_change=NULL, elements_selectable=NULL,
export_trigger=NULL, fit_view=NULL, max_zoom=NULL,
min_zoom=NULL, node_types=NULL, nodes=NULL,
nodes_change=NULL, nodes_connectable=NULL,
nodes_draggable=NULL, pan_on_drag=NULL, pan_on_scroll=NULL,
snap_grid=NULL, snap_to_grid=NULL, style=NULL,
zoom_on_pinch=NULL, zoom_on_scroll=NULL)
}

\arguments{
\item{id}{Character. The ID used to identify this component in Dash callbacks.}

\item{className}{Character. Additional CSS class names.}

\item{clicked_edge}{Named list. Latest clicked edge data}

\item{clicked_node}{Named list. Latest clicked node data}

\item{connect}{Named list. Latest connection event data}

\item{connection_mode}{A value equal to: 'strict', 'loose'. Connection mode: 'strict' (only source to target) or 'loose'.}

\item{default_position}{List of numerics. Default position of the viewport [x, y].}

\item{default_zoom}{Numeric. Default zoom level.}

\item{edge_types}{Named list. Custom edge types object.}

\item{edges}{List of named lists. Array of edge objects that connect nodes.}

\item{edges_change}{Unnamed list. Latest edges change event data}

\item{elements_selectable}{Logical. Allow elements to be selected.}

\item{export_trigger}{Numeric. Trigger for exporting the flow diagram as PNG. Increment to trigger export.}

\item{fit_view}{Logical. Fit the viewport to the nodes on first render.}

\item{max_zoom}{Numeric. Maximum zoom level.}

\item{min_zoom}{Numeric. Minimum zoom level.}

\item{node_types}{Named list. Custom node types object.}

\item{nodes}{List of named lists. Array of node objects with positions and data.}

\item{nodes_change}{Unnamed list. Latest nodes change event data}

\item{nodes_connectable}{Logical. Allow nodes to be connected.}

\item{nodes_draggable}{Logical. Allow nodes to be dragged.}

\item{pan_on_drag}{Logical. Enable panning when dragging on the canvas.}

\item{pan_on_scroll}{Logical. Enable panning when scrolling.}

\item{snap_grid}{List of numerics. Grid size for snapping [x, y].}

\item{snap_to_grid}{Logical. Enable snapping nodes to grid.}

\item{style}{Named list. CSS styles to apply to the container.}

\item{zoom_on_pinch}{Logical. Enable zooming on pinch.}

\item{zoom_on_scroll}{Logical. Enable zooming when scrolling.}
}

\value{named list of JSON elements corresponding to React.js properties and their values}

