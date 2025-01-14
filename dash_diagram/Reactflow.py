# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class Reactflow(Component):
    """A Reactflow component.


Keyword arguments:

- id (string; optional):
    The ID used to identify this component in Dash callbacks.

- className (string; optional):
    Additional CSS class names.

- clicked_edge (dict; optional):
    Latest clicked edge data.

- clicked_node (dict; optional):
    Latest clicked node data.

- connect (dict; optional):
    Latest connection event data.

- connection_mode (a value equal to: 'strict', 'loose'; default 'strict'):
    Connection mode: 'strict' (only source to target) or 'loose'.

- default_position (list of numbers; default [0, 0]):
    Default position of the viewport [x, y].

- default_zoom (number; default 1):
    Default zoom level.

- edge_types (dict; optional):
    Custom edge types object.

- edges (list of dicts; required):
    Array of edge objects that connect nodes.

- edges_change (list; optional):
    Latest edges change event data.

- elements_selectable (boolean; default True):
    Allow elements to be selected.

- export_trigger (number; default 0):
    Trigger for exporting the flow diagram as PNG. Increment to
    trigger export.

- fit_view (boolean; default False):
    Fit the viewport to the nodes on first render.

- max_zoom (number; default 2):
    Maximum zoom level.

- min_zoom (number; default 0.5):
    Minimum zoom level.

- node_types (dict; optional):
    Custom node types object.

- nodes (list of dicts; required):
    Array of node objects with positions and data.

- nodes_change (list; optional):
    Latest nodes change event data.

- nodes_connectable (boolean; default True):
    Allow nodes to be connected.

- nodes_draggable (boolean; default True):
    Allow nodes to be dragged.

- pan_on_drag (boolean; default True):
    Enable panning when dragging on the canvas.

- pan_on_scroll (boolean; default False):
    Enable panning when scrolling.

- snap_grid (list of numbers; default [15, 15]):
    Grid size for snapping [x, y].

- snap_to_grid (boolean; default False):
    Enable snapping nodes to grid.

- style (dict; optional):
    CSS styles to apply to the container.

- zoom_on_pinch (boolean; default True):
    Enable zooming on pinch.

- zoom_on_scroll (boolean; default True):
    Enable zooming when scrolling."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'dash_diagram'
    _type = 'Reactflow'
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, nodes=Component.REQUIRED, edges=Component.REQUIRED, nodes_change=Component.UNDEFINED, edges_change=Component.UNDEFINED, connect=Component.UNDEFINED, clicked_node=Component.UNDEFINED, clicked_edge=Component.UNDEFINED, node_types=Component.UNDEFINED, edge_types=Component.UNDEFINED, min_zoom=Component.UNDEFINED, max_zoom=Component.UNDEFINED, default_zoom=Component.UNDEFINED, default_position=Component.UNDEFINED, fit_view=Component.UNDEFINED, snap_to_grid=Component.UNDEFINED, snap_grid=Component.UNDEFINED, nodes_draggable=Component.UNDEFINED, nodes_connectable=Component.UNDEFINED, elements_selectable=Component.UNDEFINED, pan_on_drag=Component.UNDEFINED, pan_on_scroll=Component.UNDEFINED, zoom_on_scroll=Component.UNDEFINED, zoom_on_pinch=Component.UNDEFINED, connection_mode=Component.UNDEFINED, style=Component.UNDEFINED, className=Component.UNDEFINED, export_trigger=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'className', 'clicked_edge', 'clicked_node', 'connect', 'connection_mode', 'default_position', 'default_zoom', 'edge_types', 'edges', 'edges_change', 'elements_selectable', 'export_trigger', 'fit_view', 'max_zoom', 'min_zoom', 'node_types', 'nodes', 'nodes_change', 'nodes_connectable', 'nodes_draggable', 'pan_on_drag', 'pan_on_scroll', 'snap_grid', 'snap_to_grid', 'style', 'zoom_on_pinch', 'zoom_on_scroll']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'className', 'clicked_edge', 'clicked_node', 'connect', 'connection_mode', 'default_position', 'default_zoom', 'edge_types', 'edges', 'edges_change', 'elements_selectable', 'export_trigger', 'fit_view', 'max_zoom', 'min_zoom', 'node_types', 'nodes', 'nodes_change', 'nodes_connectable', 'nodes_draggable', 'pan_on_drag', 'pan_on_scroll', 'snap_grid', 'snap_to_grid', 'style', 'zoom_on_pinch', 'zoom_on_scroll']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        for k in ['edges', 'nodes']:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')

        super(Reactflow, self).__init__(**args)
