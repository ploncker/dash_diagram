% Auto-generated: do not edit by hand
\name{litegraph}

\alias{litegraph}

\title{Litegraph component}

\description{
LiteGraph component for creating graph-based node editors in Dash. Based on litegraph.js library.
}

\usage{
litegraph(id=NULL, autostart=NULL, className=NULL, connections=NULL,
height=NULL, lastConnectionChange=NULL, lastNodeAdded=NULL,
lastNodeRemoved=NULL, nodeDblClicked=NULL, nodes=NULL,
onConnectionChange=NULL, onNodeAdded=NULL,
onNodeDblClicked=NULL, onNodeRemoved=NULL, serialize=NULL,
serializedGraph=NULL, width=NULL)
}

\arguments{
\item{id}{Character. The ID used to identify this component in Dash callbacks.}

\item{autostart}{Logical. Whether to automatically start graph execution}

\item{className}{Character. Additional CSS class for the canvas element}

\item{connections}{List of lists containing elements 'origin_id', 'target_id', 'origin_slot', 'target_slot'.
those elements have the following types:
  - origin_id (numeric; required)
  - target_id (numeric; required)
  - origin_slot (numeric; required)
  - target_slot (numeric; required)s. Array of connection configurations}

\item{height}{Numeric. Canvas height in pixels}

\item{lastConnectionChange}{Named list. Last connection change that occurred}

\item{lastNodeAdded}{Named list. Last node that was added}

\item{lastNodeRemoved}{Numeric. Last node that was removed}

\item{nodeDblClicked}{Lists containing elements 'id', 'type', 'pos', 'properties', 'title', 'inputs', 'outputs', 'event'.
those elements have the following types:
  - id (numeric; optional)
  - type (character; optional)
  - pos (list of numerics; optional)
  - properties (named list; optional)
  - title (character; optional)
  - inputs (optional): . inputs has the following type: list of lists containing elements 'name', 'type', 'link'.
those elements have the following types:
  - name (character; optional)
  - type (character; optional)
  - link (logical | numeric | character | named list | unnamed list; optional)s
  - outputs (optional): . outputs has the following type: list of lists containing elements 'name', 'type', 'links'.
those elements have the following types:
  - name (character; optional)
  - type (character; optional)
  - links (logical | numeric | character | named list | unnamed list; optional)s
  - event (named list; optional). Currently selected node and its properties}

\item{nodes}{List of lists containing elements 'type', 'pos', 'properties'.
those elements have the following types:
  - type (character; required)
  - pos (list of numerics; optional)
  - properties (named list; optional)s. Array of node configurations}

\item{onConnectionChange}{Named list. Temporary storage for connection change event}

\item{onNodeAdded}{Named list. Temporary storage for node added event}

\item{onNodeDblClicked}{Callback triggered when a node is double-clicked.
Returns an object containing node data including id, type, position,
properties, title, inputs, outputs, and the triggering event.}

\item{onNodeRemoved}{Numeric. Temporary storage for node removed event}

\item{serialize}{Logical. Serialise currently selected graph}

\item{serializedGraph}{Named list. Serialised data}

\item{width}{Numeric. Canvas width in pixels}
}

\value{named list of JSON elements corresponding to React.js properties and their values}

