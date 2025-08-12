
module DashkitTable
using Dash

const resources_path = realpath(joinpath( @__DIR__, "..", "deps"))
const version = "1.0.0"

include("jl/dashkittable.jl")

function __init__()
    DashBase.register_package(
        DashBase.ResourcePkg(
            "dashkit_table",
            resources_path,
            version = version,
            [
                DashBase.Resource(
    relative_package_path = "dashkit_table.js",
    external_url = nothing,
    dynamic = nothing,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = nothing,
    external_url = nothing,
    dynamic = nothing,
    async = nothing,
    type = :js
)
            ]
        )

    )
end
end
