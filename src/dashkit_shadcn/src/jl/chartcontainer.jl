# AUTO GENERATED FILE - DO NOT EDIT

export chartcontainer

"""
    chartcontainer(;kwargs...)
    chartcontainer(children::Any;kwargs...)
    chartcontainer(children_maker::Function;kwargs...)


A ChartContainer component.

Keyword arguments:
- `children` (required): . children has the following type: lists containing elements 'type', 'props', 'key'.
Those elements have the following types:
  - `type` (String; required)
  - `props` (Bool | Real | String | Dict | Array; required)
  - `key` (String; required)
- `id` (String; optional)
- `className` (String; optional)
- `config` (required): . config has the following type: Dict with Strings as keys and values of type lists containing elements 'label', 'icon', 'color', 'theme'.
Those elements have the following types:
  - `label` (a list of or a singular dash component, string or number; optional)
  - `icon` (Bool | Real | String | Dict | Array; optional)
  - `color` (String; optional)
  - `theme` (optional): . theme has the following type: lists containing elements 'light', 'dark'.
Those elements have the following types:
  - `light` (String; required)
  - `dark` (String; required)
- `key` (String | Real; optional)
- `ref` (String; optional): Allows getting a ref to the component instance.
Once the component unmounts, React will set `ref.current` to `null`
(or call the ref with `null` if you passed a callback ref).
@,see,,{@link ,https://react.dev/learn/referencing-values-with-refs#refs-and-the-dom React Docs,}
"""
function chartcontainer(; kwargs...)
        available_props = Symbol[:children, :id, :className, :config, :key, :ref]
        wild_props = Symbol[]
        return Component("chartcontainer", "ChartContainer", "dashkit_shadcn", available_props, wild_props; kwargs...)
end

chartcontainer(children::Any; kwargs...) = chartcontainer(;kwargs..., children = children)
chartcontainer(children_maker::Function; kwargs...) = chartcontainer(children_maker(); kwargs...)

