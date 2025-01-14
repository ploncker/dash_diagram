# AUTO GENERATED FILE - DO NOT EDIT

export mermaid_old

"""
    mermaid_old(;kwargs...)

A Mermaid_old component.
A Mermaid diagram component for Dash.
Renders Mermaid diagrams from text definitions using Mermaid 11.4.1.
Keyword arguments:
- `id` (String; required): The ID used to identify this component in Dash callbacks.
- `chart` (String; required): The Mermaid diagram definition in text format.
- `className` (String; optional): Optional CSS class name for the container div.
- `config` (Dict; optional): Optional configuration object for Mermaid initialization.
"""
function mermaid_old(; kwargs...)
        available_props = Symbol[:id, :chart, :className, :config]
        wild_props = Symbol[]
        return Component("mermaid_old", "Mermaid_old", "dash_diagram", available_props, wild_props; kwargs...)
end

