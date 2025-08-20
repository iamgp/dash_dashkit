# AUTO GENERATED FILE - DO NOT EDIT

export chartlegend

"""
    chartlegend(;kwargs...)

A ChartLegend component.

Keyword arguments:
- `key` (String | Real; optional)
- `ref` (String; optional): Allows getting a ref to the component instance.
Once the component unmounts, React will set `ref.current` to `null`
(or call the ref with `null` if you passed a callback ref).
@,see,,{@link ,https://react.dev/learn/referencing-values-with-refs#refs-and-the-dom React Docs,}
"""
function chartlegend(; kwargs...)
        available_props = Symbol[:key, :ref]
        wild_props = Symbol[]
        return Component("chartlegend", "ChartLegend", "dashkit_shadcn", available_props, wild_props; kwargs...)
end

