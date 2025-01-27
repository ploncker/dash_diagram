# AUTO GENERATED FILE - DO NOT EDIT

export litegraph

"""
    litegraph(;kwargs...)

A Litegraph component.
LiteGraph component for creating graph-based node editors in Dash.
Based on litegraph.js library.
Keyword arguments:
- `id` (String; required): The ID used to identify this component in Dash callbacks.
- `autostart` (Bool; optional): Whether to automatically start graph execution
- `className` (String; optional): Additional CSS class for the canvas element
- `connections` (optional): Array of connection configurations. connections has the following type: Array of lists containing elements 'origin_id', 'target_id', 'origin_slot', 'target_slot'.
Those elements have the following types:
  - `origin_id` (Real; required)
  - `target_id` (Real; required)
  - `origin_slot` (Real; required)
  - `target_slot` (Real; required)s
- `height` (Real; optional): Canvas height in pixels
- `lastConnectionChange` (Dict; optional): Last connection change that occurred
- `lastNodeAdded` (Dict; optional): Last node that was added
- `lastNodeRemoved` (Real; optional): Last node that was removed
- `nodeDblClicked` (optional): Currently selected node and its properties. nodeDblClicked has the following type: lists containing elements 'id', 'type', 'pos', 'properties', 'title', 'inputs', 'outputs', 'event'.
Those elements have the following types:
  - `id` (Real; optional)
  - `type` (String; optional)
  - `pos` (Array of Reals; optional)
  - `properties` (Dict; optional)
  - `title` (String; optional)
  - `inputs` (optional): . inputs has the following type: Array of lists containing elements 'name', 'type', 'link'.
Those elements have the following types:
  - `name` (String; optional)
  - `type` (String; optional)
  - `link` (Bool | Real | String | Dict | Array; optional)s
  - `outputs` (optional): . outputs has the following type: Array of lists containing elements 'name', 'type', 'links'.
Those elements have the following types:
  - `name` (String; optional)
  - `type` (String; optional)
  - `links` (Bool | Real | String | Dict | Array; optional)s
  - `event` (Dict; optional)
- `nodes` (optional): Array of node configurations. nodes has the following type: Array of lists containing elements 'type', 'pos', 'properties'.
Those elements have the following types:
  - `type` (String; required)
  - `pos` (Array of Reals; optional)
  - `properties` (Dict; optional)s
- `onConnectionChange` (Dict; optional): Temporary storage for connection change event
- `onNodeAdded` (Dict; optional): Temporary storage for node added event
- `onNodeRemoved` (Real; optional): Temporary storage for node removed event
- `serialize` (Bool; optional): Serialise currently selected graph
- `serializedGraph` (Dict; optional): Serialised data
- `width` (Real; optional): Canvas width in pixels
"""
function litegraph(; kwargs...)
        available_props = Symbol[:id, :autostart, :className, :connections, :height, :lastConnectionChange, :lastNodeAdded, :lastNodeRemoved, :nodeDblClicked, :nodes, :onConnectionChange, :onNodeAdded, :onNodeRemoved, :serialize, :serializedGraph, :width]
        wild_props = Symbol[]
        return Component("litegraph", "Litegraph", "dash_diagram", available_props, wild_props; kwargs...)
end

