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


class ContributionGraphBlock(Component):
    """A ContributionGraphBlock component.
ContributionGraphBlock represents a single day in the contribution calendar.

Keyword arguments:

- id (string; optional):
    The ID used to identify this component in Dash callbacks.

- activity (number; default 0):
    Activity level (0-4).

- className (string; optional):
    Custom CSS class.

- count (number; default 0):
    Count of contributions.

- date (string; optional):
    Date string in ISO format.

- dayIndex (number; default 0):
    Day index in the week (0-6).

- margin (number; default 2):
    Block margin in pixels.

- onClick (optional):
    Click handler.

- radius (number; default 2):
    Block border radius in pixels.

- setProps (optional):
    Callback used by Dash to push prop changes from the client.

- size (number; default 12):
    Block size in pixels.

- weekIndex (number; default 0):
    Week index in the calendar."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'dashkit_kiboui'
    _type = 'ContributionGraphBlock'


    def __init__(
        self,
        id: typing.Optional[typing.Union[str, dict]] = None,
        activity: typing.Optional[typing.Union[NumberType]] = None,
        dayIndex: typing.Optional[typing.Union[NumberType]] = None,
        weekIndex: typing.Optional[typing.Union[NumberType]] = None,
        date: typing.Optional[typing.Union[str]] = None,
        count: typing.Optional[typing.Union[NumberType]] = None,
        size: typing.Optional[typing.Union[NumberType]] = None,
        margin: typing.Optional[typing.Union[NumberType]] = None,
        radius: typing.Optional[typing.Union[NumberType]] = None,
        className: typing.Optional[typing.Union[str]] = None,
        style: typing.Optional[typing.Any] = None,
        onClick: typing.Optional[typing.Union[typing.Any]] = None,
        **kwargs
    ):
        self._prop_names = ['id', 'activity', 'className', 'count', 'date', 'dayIndex', 'margin', 'onClick', 'radius', 'setProps', 'size', 'style', 'weekIndex']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'activity', 'className', 'count', 'date', 'dayIndex', 'margin', 'onClick', 'radius', 'setProps', 'size', 'style', 'weekIndex']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(ContributionGraphBlock, self).__init__(**args)

setattr(ContributionGraphBlock, "__init__", _explicitize_args(ContributionGraphBlock.__init__))
