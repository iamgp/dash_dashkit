# AUTO GENERATED FILE - DO NOT EDIT

import typing  # noqa: F401
from typing_extensions import TypedDict, NotRequired, Literal # noqa: F401
from dash.development.base_component import Component, _explicitize_args

ComponentType = typing.Union[
    str,
    int,
    float,
    Component,
    None,
    typing.Sequence[typing.Union[str, int, float, Component, None]],
]

NumberType = typing.Union[
    typing.SupportsFloat, typing.SupportsInt, typing.SupportsComplex
]


class ChartLegend(Component):
    """A ChartLegend component.


Keyword arguments:

- key (string | number; optional)

- ref (string; optional):
    Allows getting a ref to the component instance. Once the component
    unmounts, React will set `ref.current` to `None` (or call the ref
    with `None` if you passed a callback ref). @,see,,{@link
    ,https://react.dev/learn/referencing-values-with-refs#refs-and-the-dom
    React Docs,}."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'dashkit_shadcn'
    _type = 'ChartLegend'


    def __init__(
        self,
        ref: typing.Optional[typing.Union[str, typing.Any]] = None,
        key: typing.Optional[typing.Union[str, NumberType]] = None,
        **kwargs
    ):
        self._prop_names = ['key', 'ref']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['key', 'ref']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(ChartLegend, self).__init__(**args)

setattr(ChartLegend, "__init__", _explicitize_args(ChartLegend.__init__))
