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


class ContributionGraph(Component):
    """A ContributionGraph component.
ContributionGraph is the main container for a GitHub-style contribution graph.
This is a composable component that should contain ContributionGraphCalendar
and other contribution graph components.

Keyword arguments:

- children (a list of or a singular dash component, string or number; optional):
    Children components.

- id (string; optional):
    The ID used to identify this component in Dash callbacks.

- className (string; optional):
    Custom CSS class for the container.

- data (boolean | number | string | dict | list; optional):
    Array of contribution data with date and count.

- setProps (optional):
    Callback used by Dash to push prop changes from the client."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'dashkit_kiboui'
    _type = 'ContributionGraph'


    def __init__(
        self,
        children: typing.Optional[ComponentType] = None,
        id: typing.Optional[typing.Union[str, dict]] = None,
        data: typing.Optional[typing.Any] = None,
        className: typing.Optional[typing.Union[str]] = None,
        style: typing.Optional[typing.Any] = None,
        **kwargs
    ):
        self._prop_names = ['children', 'id', 'className', 'data', 'setProps', 'style']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'className', 'data', 'setProps', 'style']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        super(ContributionGraph, self).__init__(children=children, **args)

setattr(ContributionGraph, "__init__", _explicitize_args(ContributionGraph.__init__))
