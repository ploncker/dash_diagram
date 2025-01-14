#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan  9 11:49:27 2025

@author: ross
"""

import dash
from dash import Input, Output, State, dcc, html
import dash_diagram 
import json

#dash_diagram.Reactflow

app = dash.Dash(__name__)

# Initial nodes with parent and child nodes
initial_nodes = [
    # Parent node A with sub-flow
    {
        'id': 'A',
        'type': 'group',  # Special type for parent nodes
        'data': {'label': 'Process Group A'},
        'position': {'x': 100, 'y': 100},
        'style': {
            'width': 300,
            'height': 200,
            'backgroundColor': 'rgba(240, 240, 240, 0.5)',
            'border': '1px solid #222138',
            'borderRadius': '5px',
            'padding': '10px',
            'resize': 'both',     # Enable resizing
            'overflow': 'hidden'  # Ensure resize handle is visible
        }
    },
    # Children of node A
    {
        'id': 'A-1',
        'data': {'label': 'Sub-Task 1'},
        'position': {'x': 50, 'y': 50},
        'parentNode': 'A',  # This makes it a child of node A
        'extent': 'parent',  # Keeps the node within parent bounds
        'style': {
            'background': '#6ede87',
            'color': 'white',
            'border': '1px solid #222138'
        }
    },
    {
        'id': 'A-2',
        'data': {'label': 'Sub-Task 2'},
        'position': {'x': 50, 'y': 120},
        'parentNode': 'A',
        'extent': 'parent',
        'style': {
            'background': '#6ede87',
            'color': 'white',
            'border': '1px solid #222138'
        }
    }
]

# Initial edges connecting nodes
initial_edges = [
    # Connection within group A
    {
        'id': 'a1-a2',
        'source': 'A-1',
        'target': 'A-2',
        'style': {'stroke': '#6ede87'}
    }
]

app.layout = html.Div([
    html.H2("ReactFlow Sub-Flows Example", className="mb-4"),
    
    # Controls
    html.Div([
        html.Button("Add New Process Group", id="add-group-button", className="m-2"),
        html.Button("Add Sub-Task to Selected Group", id="add-subtask-button", className="m-2"),
        html.Button("Clear All", id="clear-button", className="m-2"),
        html.Button("Export PNG", id="export-button", className="m-2"),  # Added export button
    ], className="mb-4"),
    
    # Main flowchart
    dash_diagram.Reactflow(
        id='flowchart',
        nodes=initial_nodes,
        edges=initial_edges,
        style={
            'width': '100%', 
            'height': '600px'
        },  # Removed background styling from here as it's handled by Background component
        nodes_draggable=True,
        nodes_connectable=True,
        elements_selectable=True,
        fit_view=True,
        zoom_on_scroll=True,
        pan_on_scroll=False,
        export_trigger=0  # Initial value
    ),
    
    # Status display
    html.Div([
        html.H4("Flow Status"),
        html.Div(id='selected-group'),
        html.Div(id='nodes-status'),
        html.Div(id='edges-status')
    ], className="mt-4"),
    
    # Store components
    dcc.Store(id='group-counter', data=1),  # Start after A
    dcc.Store(id='selected-node-id', data=None),
    dcc.Store(id='export-counter', data=0),
])

# Callback for node selection
@app.callback(
    [Output('selected-node-id', 'data'),
     Output('selected-group', 'children')],
    [Input('flowchart', 'clicked_node')]
)
def handle_node_selection(node):
    if not node:
        return None, "No group selected"
    
    # If we clicked a sub-task, get its parent group
    if node.get('parentNode'):
        group_id = node['parentNode']
    else:
        group_id = node['id']
    
    return group_id, f"Selected Group: {group_id}"

# Main callback for flow updates
@app.callback(
    [Output('flowchart', 'nodes'),
     Output('flowchart', 'edges'),
     Output('group-counter', 'data'),
     Output('nodes-status', 'children'),
     Output('edges-status', 'children')],
    [Input('add-group-button', 'n_clicks'),
     Input('add-subtask-button', 'n_clicks'),
     Input('clear-button', 'n_clicks'),
     Input('flowchart', 'nodes_change'),
     Input('flowchart', 'edges_change'),
     Input('flowchart', 'connect')],  # Changed from 'connect' to 'onConnect'
    [State('flowchart', 'nodes'),
     State('flowchart', 'edges'),
     State('group-counter', 'data'),
     State('selected-node-id', 'data')],
    prevent_initial_call=True
)
def update_flow(add_group_clicks, add_subtask_clicks, clear_clicks, 
                nodes_change, edges_change, new_connection,
                current_nodes, current_edges, counter, selected_node):
    ctx = dash.callback_context
    if not ctx.triggered:
        return dash.no_update
    
    trigger_id = ctx.triggered[0]['prop_id'].split('.')[1]
    
    nodes = current_nodes.copy() if current_nodes else []
    edges = current_edges.copy() if current_edges else []
    
    if trigger_id == 'n_clicks' and ctx.triggered[0]['prop_id'].startswith('add-group'):
        # Add new group with two default sub-tasks
        group_id = chr(ord('A') + counter)  # Generate next letter (A, B, C, etc.)
        new_group = {
            'id': group_id,
            'type': 'group',
            'data': {'label': f'Process Group {group_id}'},
            'position': {'x': 100 + (counter * 150), 'y': 100 + (counter * 50)},
            'style': {
                'width': 300,
                'height': 200,
                'backgroundColor': 'rgba(240, 240, 240, 0.5)',
                'border': '1px solid #222138',
                'borderRadius': '5px',
                'padding': '10px',
                'resize': 'both',     # Enable resizing
                'overflow': 'hidden'  # Ensure resize handle is visible
            }
        }
        
        # Add two sub-tasks to the new group
        sub_tasks = [
            {
                'id': f'{group_id}-1',
                'data': {'label': 'Sub-Task 1'},
                'position': {'x': 50, 'y': 50},
                'parentNode': group_id,
                'extent': 'parent',
                'style': {
                    'background': '#6ede87',
                    'color': 'white',
                    'border': '1px solid #222138'
                }
            },
            {
                'id': f'{group_id}-2',
                'data': {'label': 'Sub-Task 2'},
                'position': {'x': 50, 'y': 120},
                'parentNode': group_id,
                'extent': 'parent',
                'style': {
                    'background': '#6ede87',
                    'color': 'white',
                    'border': '1px solid #222138'
                }
            }
        ]
        
        nodes.extend([new_group] + sub_tasks)
        counter += 1
        
    elif trigger_id == 'n_clicks' and ctx.triggered[0]['prop_id'].startswith('add-subtask'):
        if selected_node:
            # Find all existing sub-tasks for this group
            parent_id = selected_node
            existing_subtasks = [n for n in nodes if n.get('parentNode') == parent_id]
            task_count = len(existing_subtasks)
            
            # Add new sub-task to selected group
            new_task = {
                'id': f'{parent_id}-{task_count + 1}',
                'data': {'label': f'Sub-Task {task_count + 1}'},
                'position': {'x': 50, 'y': 50 + (task_count * 70)},
                'parentNode': parent_id,
                'extent': 'parent',
                'style': {
                    'background': '#6ede87',
                    'color': 'white',
                    'border': '1px solid #222138',
                    'padding': '10px'
                }
            }
            nodes.append(new_task)
    
    elif trigger_id == 'n_clicks' and ctx.triggered[0]['prop_id'].startswith('clear'):
        nodes = initial_nodes
        edges = initial_edges
        counter = 1
        
    elif trigger_id == 'nodes_change' and nodes_change:
        for change in nodes_change:
            print(f"Node change event received: {json.dumps(change, indent=2)}")  # Debug info
            node_idx = next(i for i, node in enumerate(nodes) if node['id'] == change['id'])
            
            if change['type'] == 'position' and 'position' in change:
                nodes[node_idx]['position'] = change['position']
                print(f"Updated position for node {change['id']}")
            
            elif change['type'] == 'dimensions':
                # Handle resize events
                current_style = nodes[node_idx].get('style', {})
                if 'dimensions' in change:
                    current_style.update({
                        'width': change['dimensions']['width'],
                        'height': change['dimensions']['height']
                    })
                    nodes[node_idx]['style'] = current_style
                    print(f"Updated dimensions for node {change['id']}")
            
            else:
                print(f"Unhandled change type: {change['type']}")  # Debug info
    
    elif trigger_id == 'connect' and new_connection:
        new_edge = {
            'id': f"e{new_connection['source']}-{new_connection['target']}",
            'source': new_connection['source'],
            'target': new_connection['target'],
            'style': {'stroke': '#333'}
        }
        edges.append(new_edge)
    
    # Generate status displays
    nodes_info = html.Div([
        html.P(f"Total Groups: {len([n for n in nodes if n.get('type') == 'group'])}"),
        html.P(f"Total Sub-Tasks: {len([n for n in nodes if n.get('parentNode')])}"),
        html.Pre(json.dumps([{'id': n['id'], 'type': n.get('type', 'task')} for n in nodes], indent=2)),
    ])
    
    edges_info = html.Div([
        html.P(f"Total Connections: {len(edges)}"),
        html.Pre(json.dumps(edges, indent=2)),
    ])
    
    return nodes, edges, counter, nodes_info, edges_info

# Callback to trigger export
@app.callback(
    Output("flowchart", "export_trigger"),
    Input("export-button", "n_clicks"),
    State("flowchart", "export_trigger"),
    prevent_initial_call=True
)
def trigger_export(n_clicks, current_trigger):
    if n_clicks:
        # Increment the trigger value
        return (current_trigger or 0) + 1
    return dash.no_update

if __name__ == '__main__':
    app.run_server(debug=True)