

import dash
from dash import html, dcc, callback, Input, Output, State, MATCH, ALL
import dash_diagram
import json

app = dash.Dash(__name__)

# Example nodes for a simple math operation graph
initial_nodes = [
    {
        'type': 'basic/const',
        'pos': [200, 200],
        'properties': {'value': 5}
    },
    {
        'type': 'basic/const',
        'pos': [200, 400],
        'properties': {'value': 3}
    },
    {
        'type': 'basic/operation',
        'pos': [200, 300],
        'properties': {'operation': '+'}
    },
]

# Example connections between nodes
initial_connections = [
    {
        'origin_id': 1,  # First const node
        'target_id': 3,  # Operation node
        'origin_slot': 0,
        'target_slot': 0
    },
    {
        'origin_id': 2,  # Second const node
        'target_id': 3,  # Operation node
        'origin_slot': 0,
        'target_slot': 1
    }
]

app.layout = html.Div([
    html.Div([
        # Graph editor
        html.Div(
            dash_diagram.Litegraph(
                id='graph-editor',
                nodes=initial_nodes,
                connections=initial_connections,
                width=800,
                height=600,
                autostart=True
            ),
            style={'flex': '2'}
        ),
        
        
        # Properties panel
        html.Div([
            html.H3("Node Properties"),
            html.Div([
                html.Strong("Title: "),
                html.Span(id='node-title')
            ]),
            html.Div([
                html.Strong("Type: "),
                html.Span(id='node-type')
            ]),
            html.Div([
                html.Strong("Position: "),
                html.Span(id='node-position')
            ]),
            html.H4("Properties:"),
            html.Pre(id='node-properties', style={'whiteSpace': 'pre-wrap'}),
            html.H4("Inputs:"),
            html.Pre(id='node-inputs', style={'whiteSpace': 'pre-wrap'}),
            html.H4("Outputs:"),
            html.Pre(id='node-outputs', style={'whiteSpace': 'pre-wrap'})
        ], style={
            'flex': '1',
            'padding': '20px',
            'backgroundColor': '#f5f5f5',
            'minWidth': '300px'
        }),
            
        html.Button(
            'Export Diagram', 
            id='export-button', 
        ),
        dcc.Download(id='download-json'),
        dcc.Store(id="graph-editor-data", data={}),  # Store for serialized data
        dcc.Store(id="trigger-serialize", data=0),  # Store for the trigger
            
    ], style={'display': 'flex', 'gap': '20px'}),
    
    html.Div([
        html.H3("Events Log"),
        html.Div(id='node-added-output'),
        html.Div(id='node-removed-output'),
        html.Div(id='connection-changed-output')
    ], style={'marginTop': '20px'})
])

#This displays the property of our node when double-clicked                    
@callback(
    [
     Output('node-title', 'children'),
     Output('node-type', 'children'),
     Output('node-position', 'children'),
     Output('node-properties', 'children'),
     Output('node-inputs', 'children'),
     Output('node-outputs', 'children')],
    Input('graph-editor', 'nodeDblClicked')
)
def display_node_properties(node_data):
    print('node_data', node_data)

    if not node_data:
        return dash.no_update, dash.no_update, dash.no_update, dash.no_update, dash.no_update, dash.no_update

    print('node_data', node_data)
    if node_data is None:
        return ["No node selected"] * 6
    
    return [
        node_data.get('title', 'Untitled'),
        node_data.get('type', 'Unknown'),
        f"({node_data['pos'][0]}, {node_data['pos'][1]})",
        json.dumps(node_data.get('properties', {}), indent=2),
        json.dumps(node_data.get('inputs', []), indent=2),
        json.dumps(node_data.get('outputs', []), indent=2)
    ]

#This triggers the serialisation function of our component
@callback(
    Output('graph-editor', 'serialize'),  # Updates the trigger
    Input("export-button", "n_clicks"),
    prevent_initial_call=True
)
def trigger_serialization(n_clicks):
    if not n_clicks:
        return False
    return True  # This will trigger handleSerialize

#This callback is triggered by the above callback
@callback(
    Output("download-json", "data"),
    Input("graph-editor", "serializedGraph"),  # Listen for serialized data
    prevent_initial_call=True
)
def export_graph(serialized_data):
    print("🚀 Received Serialized Data:", serialized_data)

    if not serialized_data:
        return None

    return dict(
        content=json.dumps(serialized_data, indent=2),
        filename="graph.json",
        type="text/json"
    )




if __name__ == '__main__':
    app.run_server(debug=True)