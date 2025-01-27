    
import dash
from dash import callback, html, Input, Output, dcc, State
import dash_diagram


app = dash.Dash(__name__)

# Sample Mermaid diagram
initial_diagram = """sequenceDiagram
    participant Alice
    participant Bob
    Alice->>John: Hello John, how are you?
    loop Healthcheck
        John->>John: Fight against hypochondria
    end
    Note right of John: Rational thoughts
    John-->>Alice: Great!
    John->>Bob: How about you?
    Bob-->>John: Jolly good!"""

app.layout = html.Div([
    html.H1("Mermaid Diagram Demo"),
    html.P("Using Mermaid 11.4.1"),
    
    # Diagram display
    dash_diagram.Mermaid(
        id='mermaid-diagram',
        chart=initial_diagram,
        config={
            'theme': 'default',
            'securityLevel': 'loose',
            'startOnLoad': False
        },
        export_trigger=0
    ),
    
    # Editor for live updates
    html.Div([
        html.H3("Edit Diagram Definition:"),
        dcc.Textarea(
            id='diagram-input',
            value=initial_diagram,
            style={
                'width': '100%', 
                'height': 200,
                'fontFamily': 'monospace',
                'fontSize': '14px'
            }
        ),
        html.Button(
            'Update Diagram', 
            id='update-button', 
            n_clicks=0,
            style={
                'marginTop': '10px',
                'padding': '10px 20px'
            }
        ),
        html.Button(
            'Export Diagram', 
            id='export-mermaid-button', 
            n_clicks=0,
            style={
                'marginTop': '10px',
                'padding': '10px 20px'
            }
        )
    ], style={'marginTop': 20})
])

@app.callback(
    Output('mermaid-diagram', 'chart'),
    Input('update-button', 'n_clicks'),
    State('diagram-input', 'value'),
    prevent_initial_call=True
)
def update_diagram(n_clicks, new_diagram):
    return new_diagram

# Callback to trigger export
@app.callback(
    Output("mermaid-diagram", "export_trigger"),
    Input("export-mermaid-button", "n_clicks"),
    State("mermaid-diagram", "export_trigger"),
    prevent_initial_call=True
)
def trigger_mermaid_export(n_clicks, current_trigger):
    if n_clicks:
        return (current_trigger or 0) + 1
    return dash.no_update

if __name__ == '__main__':
    app.run_server(debug=True)
