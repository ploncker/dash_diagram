# AUTO GENERATED FILE - DO NOT EDIT

export mermaid_export

"""
    mermaid_export(;kwargs...)

A Mermaid_export component.
A Mermaid diagram component for Dash.
Renders Mermaid diagrams from text definitions using Mermaid 11.4.1.
Keyword arguments:
- `id` (String; required): The ID used to identify this component in Dash callbacks.
- `chart` (String; required): The Mermaid diagram definition in text format.
- `className` (String; optional): Optional CSS class name for the container div.
- `config` (Dict; optional): Optional configuration object for Mermaid initialization.
- `export_trigger` (Real; optional): Trigger for exporting the diagram as PNG. Increment to trigger export.
"""
function mermaid_export(; kwargs...)
        available_props = Symbol[:id, :chart, :className, :config, :export_trigger]
        wild_props = Symbol[]
        return Component("mermaid_export", "Mermaid_export", "dash_diagram", available_props, wild_props; kwargs...)
end

