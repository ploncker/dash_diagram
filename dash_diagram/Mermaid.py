# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class Mermaid(Component):
    """A Mermaid component.


Keyword arguments:

- id (string; required):
    The ID used to identify this component in Dash callbacks.

- chart (string; required):
    The Mermaid diagram definition in text format.

- className (string; default ''):
    Optional CSS class name for the container div.

- config (dict; optional):
    Optional configuration object for Mermaid initialization.

- export_trigger (number; default 0):
    Trigger for exporting the diagram as PNG."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'dash_diagram'
    _type = 'Mermaid'
    @_explicitize_args
    def __init__(self, id=Component.REQUIRED, chart=Component.REQUIRED, config=Component.UNDEFINED, className=Component.UNDEFINED, export_trigger=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'chart', 'className', 'config', 'export_trigger']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'chart', 'className', 'config', 'export_trigger']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        for k in ['id', 'chart']:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')

        super(Mermaid, self).__init__(**args)
