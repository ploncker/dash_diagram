# import mermaid_component
# from dash import Dash, callback, html, Input, Output

# app = Dash(__name__)


# app.layout = html.Div([
#     mermaid_component.MermaidComponent(
#         id='input',
#         value='my-value',
#         label='my-label'
#     ),
#     html.Div(id='output')
# ])


# @callback(Output('output', 'children'), Input('input', 'value'))
# def display_output(value):
#     return 'You have entered {}'.format(value)


# if __name__ == '__main__':
#     app.run(debug=True)


# import dash
# from dash import callback, html, Input, Output, dcc, State
# import mermaid_component


# app = dash.Dash(__name__)

# # Sample Mermaid diagram
# initial_diagram = """
# flowchart TD
#     A[Christmas] -->|Get money| B(Go shopping)
#     B --> C{Let me think}
#     C -->|One| D[Laptop]
#     C -->|Two| E[iPhone]
#     C -->|Three| F[Car]
# """

# app.layout = html.Div([
#     html.H1("Mermaid Diagram Demo"),
    
#     # Diagram display
#     mermaid_component.MermaidComponent(
#         id='mermaid-diagram',
#         chart=initial_diagram,
#         config={
#             'theme': 'default',
#             'securityLevel': 'loose',
#             'startOnLoad': False
#         }
#     ),
    
#     # Editor for live updates
#     html.Div([
#         html.H3("Edit Diagram Definition:"),
#         dcc.Textarea(
#             id='diagram-input',
#             value=initial_diagram,
#             style={'width': '100%', 'height': 200}
#         ),
#         html.Button('Update Diagram', id='update-button', n_clicks=0)
#     ], style={'marginTop': 20})
# ])

# @app.callback(
#     Output('mermaid-diagram', 'chart'),
#     Input('update-button', 'n_clicks'),
#     State('diagram-input', 'value'),
#     prevent_initial_call=True
# )
# def update_diagram(n_clicks, new_diagram):
#     return new_diagram

# if __name__ == '__main__':
#     app.run_server(debug=True)
    
    
    
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
        }
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

if __name__ == '__main__':
    app.run_server(debug=True)