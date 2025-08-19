
module DashkitKiboui
using Dash

const resources_path = realpath(joinpath( @__DIR__, "..", "deps"))
const version = "1.0.0"

include("jl/contributiongraph.jl")
include("jl/contributiongraphblock.jl")
include("jl/contributiongraphcalendar.jl")

function __init__()
    DashBase.register_package(
        DashBase.ResourcePkg(
            "dashkit_kiboui",
            resources_path,
            version = version,
            [
                DashBase.Resource(
    relative_package_path = "dashkit_kiboui.js",
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
