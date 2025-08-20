
module DashkitShadcn
using Dash

const resources_path = realpath(joinpath( @__DIR__, "..", "deps"))
const version = "1.0.0"

include("jl/areachart.jl")
include("jl/barchart.jl")
include("jl/chartcontainer.jl")
include("jl/chartlegend.jl")
include("jl/charttooltip.jl")

function __init__()
    DashBase.register_package(
        DashBase.ResourcePkg(
            "dashkit_shadcn",
            resources_path,
            version = version,
            [
                DashBase.Resource(
    relative_package_path = "dashkit_shadcn.js",
    external_url = nothing,
    dynamic = nothing,
    async = :false,
    type = :js
),
DashBase.Resource(
    relative_package_path = "proptypes.js",
    external_url = nothing,
    dynamic = nothing,
    async = :false,
    type = :js
)
            ]
        )

    )
end
end
