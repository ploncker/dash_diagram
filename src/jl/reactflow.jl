# AUTO GENERATED FILE - DO NOT EDIT

export reactflow

"""
    reactflow(;kwargs...)

A Reactflow component.

Keyword arguments:
- `id` (String; optional): The ID used to identify this component in Dash callbacks.
- `className` (String; optional): Additional CSS class names.
- `clicked_edge` (Dict; optional): Latest clicked edge data
- `clicked_node` (Dict; optional): Latest clicked node data
- `connect` (Dict; optional): Latest connection event data
- `connection_mode` (a value equal to: 'strict', 'loose'; optional): Connection mode: 'strict' (only source to target) or 'loose'.
- `default_position` (Array of Reals; optional): Default position of the viewport [x, y].
- `default_zoom` (Real; optional): Default zoom level.
- `edge_types` (Dict; optional): Custom edge types object.
- `edges` (Array of Dicts; required): Array of edge objects that connect nodes.
- `edges_change` (Array; optional): Latest edges change event data
- `elements_selectable` (Bool; optional): Allow elements to be selected.
- `export_trigger` (Real; optional): Trigger for exporting the flow diagram as PNG. Increment to trigger export.
- `fit_view` (Bool; optional): Fit the viewport to the nodes on first render.
- `max_zoom` (Real; optional): Maximum zoom level.
- `min_zoom` (Real; optional): Minimum zoom level.
- `node_types` (Dict; optional): Custom node types object.
- `nodes` (Array of Dicts; required): Array of node objects with positions and data.
- `nodes_change` (Array; optional): Latest nodes change event data
- `nodes_connectable` (Bool; optional): Allow nodes to be connected.
- `nodes_draggable` (Bool; optional): Allow nodes to be dragged.
- `pan_on_drag` (Bool; optional): Enable panning when dragging on the canvas.
- `pan_on_scroll` (Bool; optional): Enable panning when scrolling.
- `snap_grid` (Array of Reals; optional): Grid size for snapping [x, y].
- `snap_to_grid` (Bool; optional): Enable snapping nodes to grid.
- `style` (Dict; optional): CSS styles to apply to the container.
- `zoom_on_pinch` (Bool; optional): Enable zooming on pinch.
- `zoom_on_scroll` (Bool; optional): Enable zooming when scrolling.
"""
function reactflow(; kwargs...)
        available_props = Symbol[:id, :className, :clicked_edge, :clicked_node, :connect, :connection_mode, :default_position, :default_zoom, :edge_types, :edges, :edges_change, :elements_selectable, :export_trigger, :fit_view, :max_zoom, :min_zoom, :node_types, :nodes, :nodes_change, :nodes_connectable, :nodes_draggable, :pan_on_drag, :pan_on_scroll, :snap_grid, :snap_to_grid, :style, :zoom_on_pinch, :zoom_on_scroll]
        wild_props = Symbol[]
        return Component("reactflow", "Reactflow", "dash_diagram", available_props, wild_props; kwargs...)
end

