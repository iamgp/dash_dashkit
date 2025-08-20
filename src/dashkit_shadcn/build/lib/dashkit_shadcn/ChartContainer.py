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


class ChartContainer(Component):
    """A ChartContainer component.


Keyword arguments:

- children (dict; required)

    `children` is a dict with keys:

    - type (string; required)

    - props (boolean | number | string | dict | list; required)

    - key (string; required)

- id (string; optional)

- className (string; optional)

- config (dict; required)

    `config` is a dict with strings as keys and values of type dict
    with keys:

    - label (a list of or a singular dash component, string or number; optional)

    - icon (boolean | number | string | dict | list; optional)

    - color (string; optional)

    - theme (dict; optional)

        `theme` is a dict with keys:

        - light (string; required)

        - dark (string; required)

- key (string | number; optional)

- ref (string; optional):
    Allows getting a ref to the component instance. Once the component
    unmounts, React will set `ref.current` to `None` (or call the ref
    with `None` if you passed a callback ref). @,see,,{@link
    ,https://react.dev/learn/referencing-values-with-refs#refs-and-the-dom
    React Docs,}."""
    _children_props = ['config{}.label']
    _base_nodes = ['children']
    _namespace = 'dashkit_shadcn'
    _type = 'ChartContainer'
    ConfigTheme = TypedDict(
        "ConfigTheme",
            {
            "light": str,
            "dark": str
        }
    )

    Config = TypedDict(
        "Config",
            {
            "label": NotRequired[ComponentType],
            "icon": NotRequired[typing.Any],
            "color": NotRequired[typing.Union[str]],
            "theme": NotRequired[typing.Union["ConfigTheme"]]
        }
    )


    def __init__(
        self,
        children: typing.Optional[ComponentType] = None,
        id: typing.Optional[typing.Union[str, dict]] = None,
        className: typing.Optional[typing.Union[str]] = None,
        config: typing.Optional[typing.Dict[typing.Union[str, float, int], "Config"]] = None,
        ref: typing.Optional[typing.Union[str, typing.Any]] = None,
        key: typing.Optional[typing.Union[str, NumberType]] = None,
        **kwargs
    ):
        self._prop_names = ['children', 'id', 'className', 'config', 'key', 'ref']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'className', 'config', 'key', 'ref']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        for k in ['config']:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')

        if 'children' not in _explicit_args:
            raise TypeError('Required argument children was not specified.')

        super(ChartContainer, self).__init__(children=children, **args)

setattr(ChartContainer, "__init__", _explicitize_args(ChartContainer.__init__))
