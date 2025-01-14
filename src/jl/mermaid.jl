# AUTO GENERATED FILE - DO NOT EDIT

export mermaid

"""
    mermaid(;kwargs...)

A Mermaid component.

Keyword arguments:
- `id` (String; required): The ID used to identify this component in Dash callbacks.
- `chart` (String; required): The Mermaid diagram definition in text format.
- `className` (String; optional): Optional CSS class name for the container div.
- `config` (Dict; optional): Optional configuration object for Mermaid initialization.
- `export_trigger` (Real; optional): Trigger for exporting the diagram as PNG.
"""
function mermaid(; kwargs...)
        available_props = Symbol[:id, :chart, :className, :config, :export_trigger]
        wild_props = Symbol[]
        return Component("mermaid", "Mermaid", "dash_diagram", available_props, wild_props; kwargs...)
end

