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


class BarChart(Component):
    """A BarChart component.
BarChart renders a bar chart using shadcn/ui styling and Recharts.

Keyword arguments:

- children (a list of or a singular dash component, string or number; optional):
    Children components.

- id (string; optional):
    The ID used to identify this component in Dash callbacks.

- className (string; optional):
    Custom CSS class for the container.

- config (dict; optional):
    Chart configuration object with data key mappings and colors.

- data (list of dicts; optional):
    Array of data points for the chart.

- dataKey (string; default 'value'):
    The key in data objects to use for the bar values.

- maxBarSize (number; optional):
    Maximum bar size.

- radius (number; default 4):
    Border radius for the bars.

- setProps (optional):
    Callback used by Dash to push prop changes from the client.

- showGrid (boolean | number | string | dict | list; default True):
    Whether to show the grid.

- showLegend (boolean | number | string | dict | list; default False):
    Whether to show the legend.

- showTooltip (boolean | number | string | dict | list; default True):
    Whether to show tooltips.

- showXAxis (boolean | number | string | dict | list; default True):
    Whether to show the x-axis.

- showYAxis (boolean | number | string | dict | list; default False):
    Whether to show the y-axis.

- stackId (string; optional):
    Stack ID for stacked bars.

- xAxisKey (string; default 'name'):
    The key in data objects to use for x-axis labels.

- yAxisKey (string; optional):
    The key in data objects to use for y-axis labels."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'dashkit_shadcn'
    _type = 'BarChart'


    def __init__(
        self,
        children: typing.Optional[ComponentType] = None,
        id: typing.Optional[typing.Union[str, dict]] = None,
        className: typing.Optional[typing.Union[str]] = None,
        config: typing.Optional[typing.Union[dict]] = None,
        data: typing.Optional[typing.Union[typing.Sequence[dict]]] = None,
        dataKey: typing.Optional[typing.Union[str]] = None,
        xAxisKey: typing.Optional[typing.Union[str]] = None,
        yAxisKey: typing.Optional[typing.Union[str]] = None,
        showXAxis: typing.Optional[typing.Any] = None,
        showYAxis: typing.Optional[typing.Any] = None,
        showGrid: typing.Optional[typing.Any] = None,
        showTooltip: typing.Optional[typing.Any] = None,
        showLegend: typing.Optional[typing.Any] = None,
        stackId: typing.Optional[typing.Union[str]] = None,
        radius: typing.Optional[typing.Union[NumberType]] = None,
        maxBarSize: typing.Optional[typing.Union[NumberType]] = None,
        style: typing.Optional[typing.Any] = None,
        **kwargs
    ):
        self._prop_names = ['children', 'id', 'className', 'config', 'data', 'dataKey', 'maxBarSize', 'radius', 'setProps', 'showGrid', 'showLegend', 'showTooltip', 'showXAxis', 'showYAxis', 'stackId', 'style', 'xAxisKey', 'yAxisKey']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'className', 'config', 'data', 'dataKey', 'maxBarSize', 'radius', 'setProps', 'showGrid', 'showLegend', 'showTooltip', 'showXAxis', 'showYAxis', 'stackId', 'style', 'xAxisKey', 'yAxisKey']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        super(BarChart, self).__init__(children=children, **args)

setattr(BarChart, "__init__", _explicitize_args(BarChart.__init__))
