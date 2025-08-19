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


class ContributionGraphCalendar(Component):
    """A ContributionGraphCalendar component.
ContributionGraphCalendar renders the calendar grid for contributions.

Keyword arguments:

- children (string | number; optional):
    Children render function or components.

- id (string; optional):
    The ID used to identify this component in Dash callbacks.

- blockMargin (number; default 2):
    Block margin in pixels.

- blockRadius (number; default 2):
    Block border radius in pixels.

- blockSize (number; default 12):
    Block size in pixels.

- className (string; optional):
    Custom CSS class.

- data (boolean | number | string | dict | list; optional):
    Array of contribution data.

- monthsToShow (number; default 12):
    Number of months to show.

- setProps (optional):
    Callback used by Dash to push prop changes from the client.

- showMonthLabels (boolean | number | string | dict | list; default True):
    Show month labels.

- showTooltips (boolean | number | string | dict | list; default False):
    Enable tooltips.

- showWeekdayLabels (boolean | number | string | dict | list; default True):
    Show weekday labels.

- tooltipFormat (string; optional):
    Custom tooltip format string. Use {count}, {date}, {dayName},
    {monthName}, {year} as placeholders."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'dashkit_kiboui'
    _type = 'ContributionGraphCalendar'


    def __init__(
        self,
        children: typing.Optional[ComponentType] = None,
        id: typing.Optional[typing.Union[str, dict]] = None,
        data: typing.Optional[typing.Any] = None,
        monthsToShow: typing.Optional[typing.Union[NumberType]] = None,
        blockSize: typing.Optional[typing.Union[NumberType]] = None,
        blockMargin: typing.Optional[typing.Union[NumberType]] = None,
        blockRadius: typing.Optional[typing.Union[NumberType]] = None,
        showMonthLabels: typing.Optional[typing.Any] = None,
        showWeekdayLabels: typing.Optional[typing.Any] = None,
        showTooltips: typing.Optional[typing.Any] = None,
        tooltipFormat: typing.Optional[typing.Union[str]] = None,
        className: typing.Optional[typing.Union[str]] = None,
        **kwargs
    ):
        self._prop_names = ['children', 'id', 'blockMargin', 'blockRadius', 'blockSize', 'className', 'data', 'monthsToShow', 'setProps', 'showMonthLabels', 'showTooltips', 'showWeekdayLabels', 'tooltipFormat']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'blockMargin', 'blockRadius', 'blockSize', 'className', 'data', 'monthsToShow', 'setProps', 'showMonthLabels', 'showTooltips', 'showWeekdayLabels', 'tooltipFormat']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        super(ContributionGraphCalendar, self).__init__(children=children, **args)

setattr(ContributionGraphCalendar, "__init__", _explicitize_args(ContributionGraphCalendar.__init__))
