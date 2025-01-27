
module DashDiagram
using Dash

const resources_path = realpath(joinpath( @__DIR__, "..", "deps"))
const version = "0.0.1"

include("jl/litegraph.jl")
include("jl/mermaid.jl")
include("jl/reactflow.jl")

function __init__()
    DashBase.register_package(
        DashBase.ResourcePkg(
            "dash_diagram",
            resources_path,
            version = version,
            [
                DashBase.Resource(
    relative_package_path = "dash_diagram.min.js",
    external_url = nothing,
    dynamic = nothing,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "dash_diagram.min.js.map",
    external_url = nothing,
    dynamic = true,
    async = nothing,
    type = :js
)
            ]
        )

    )
end
end
