# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class Litegraph(Component):
    """A Litegraph component.
LiteGraph component for creating graph-based node editors in Dash.
Based on litegraph.js library.

Keyword arguments:

- id (string; required):
    The ID used to identify this component in Dash callbacks.

- autostart (boolean; default True):
    Whether to automatically start graph execution.

- className (string; optional):
    Additional CSS class for the canvas element.

- connections (list of dicts; optional):
    Array of connection configurations.

    `connections` is a list of dicts with keys:

    - origin_id (number; required)

    - target_id (number; required)

    - origin_slot (number; required)

    - target_slot (number; required)

- height (number; default 720):
    Canvas height in pixels.

- lastConnectionChange (dict; optional):
    Last connection change that occurred.

- lastNodeAdded (dict; optional):
    Last node that was added.

- lastNodeRemoved (number; optional):
    Last node that was removed.

- nodeDblClicked (dict; optional):
    Currently selected node and its properties.

    `nodeDblClicked` is a dict with keys:

    - id (number; optional)

    - type (string; optional)

    - pos (list of numbers; optional)

    - properties (dict; optional)

    - title (string; optional)

    - inputs (list of dicts; optional)

        `inputs` is a list of dicts with keys:

        - name (string; optional)

        - type (string; optional)

        - link (boolean | number | string | dict | list; optional)

    - outputs (list of dicts; optional)

        `outputs` is a list of dicts with keys:

        - name (string; optional)

        - type (string; optional)

        - links (boolean | number | string | dict | list; optional)

    - event (dict; optional)

- nodes (list of dicts; optional):
    Array of node configurations.

    `nodes` is a list of dicts with keys:

    - type (string; required)

    - pos (list of numbers; optional)

    - properties (dict; optional)

- onConnectionChange (dict; optional):
    Temporary storage for connection change event.

- onNodeAdded (dict; optional):
    Temporary storage for node added event.

- onNodeRemoved (number; optional):
    Temporary storage for node removed event.

- serialize (boolean; default False):
    Serialise currently selected graph.

- serializedGraph (dict; optional):
    Serialised data.

- width (number; default 1024):
    Canvas width in pixels."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'dash_diagram'
    _type = 'Litegraph'
    @_explicitize_args
    def __init__(self, id=Component.REQUIRED, width=Component.UNDEFINED, height=Component.UNDEFINED, autostart=Component.UNDEFINED, nodes=Component.UNDEFINED, connections=Component.UNDEFINED, className=Component.UNDEFINED, lastNodeAdded=Component.UNDEFINED, lastNodeRemoved=Component.UNDEFINED, lastConnectionChange=Component.UNDEFINED, serializedGraph=Component.UNDEFINED, onNodeAdded=Component.UNDEFINED, onNodeRemoved=Component.UNDEFINED, onConnectionChange=Component.UNDEFINED, nodeDblClicked=Component.UNDEFINED, onNodeDblClicked=Component.UNDEFINED, serialize=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'autostart', 'className', 'connections', 'height', 'lastConnectionChange', 'lastNodeAdded', 'lastNodeRemoved', 'nodeDblClicked', 'nodes', 'onConnectionChange', 'onNodeAdded', 'onNodeRemoved', 'serialize', 'serializedGraph', 'width']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'autostart', 'className', 'connections', 'height', 'lastConnectionChange', 'lastNodeAdded', 'lastNodeRemoved', 'nodeDblClicked', 'nodes', 'onConnectionChange', 'onNodeAdded', 'onNodeRemoved', 'serialize', 'serializedGraph', 'width']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        for k in ['id']:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')

        super(Litegraph, self).__init__(**args)
