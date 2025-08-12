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


class DashkitTable(Component):
    """A DashkitTable component.


Keyword arguments:

- id (string; optional)

- cellClassName (string; optional)

- className (string; optional)

- colHeaders (boolean | number | string | dict | list; optional)

- columnSorting (boolean | number | string | dict | list; optional)

- columns (list of boolean | number | string | dict | lists; optional)

- contextMenu (boolean | number | string | dict | list; optional)

- data (list of boolean | number | string | dict | lists | list of list of boolean | number | string | dict | listss; optional)

- dropdownMenu (boolean | number | string | dict | list; optional)

- filters (boolean | number | string | dict | list; optional)

- headerClassName (string; optional)

- height (string | number; optional)

- licenseKey (string; optional)

- multiColumnSorting (boolean | number | string | dict | list; optional)

- rowHeaders (boolean | number | string | dict | list; optional)

- rowHeight (number; optional)

- setProps (optional)

- settings (boolean | number | string | dict | list; optional)

- stretchH (string; optional)

- themeName (string; optional)

- width (string | number; optional)"""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'dashkit_table'
    _type = 'DashkitTable'


    def __init__(
        self,
        id: typing.Optional[typing.Union[str, dict]] = None,
        data: typing.Optional[typing.Union[typing.Sequence[typing.Any], typing.Sequence[typing.Sequence[typing.Any]]]] = None,
        columns: typing.Optional[typing.Union[typing.Sequence[typing.Any]]] = None,
        themeName: typing.Optional[typing.Union[str]] = None,
        className: typing.Optional[typing.Union[str]] = None,
        cellClassName: typing.Optional[typing.Union[str]] = None,
        headerClassName: typing.Optional[typing.Union[str]] = None,
        height: typing.Optional[typing.Union[str, NumberType]] = None,
        width: typing.Optional[typing.Union[str, NumberType]] = None,
        rowHeaders: typing.Optional[typing.Any] = None,
        colHeaders: typing.Optional[typing.Any] = None,
        licenseKey: typing.Optional[typing.Union[str]] = None,
        columnSorting: typing.Optional[typing.Any] = None,
        multiColumnSorting: typing.Optional[typing.Any] = None,
        filters: typing.Optional[typing.Any] = None,
        dropdownMenu: typing.Optional[typing.Any] = None,
        contextMenu: typing.Optional[typing.Any] = None,
        rowHeight: typing.Optional[typing.Union[NumberType]] = None,
        stretchH: typing.Optional[typing.Union[str]] = None,
        settings: typing.Optional[typing.Any] = None,
        **kwargs
    ):
        self._prop_names = ['id', 'cellClassName', 'className', 'colHeaders', 'columnSorting', 'columns', 'contextMenu', 'data', 'dropdownMenu', 'filters', 'headerClassName', 'height', 'licenseKey', 'multiColumnSorting', 'rowHeaders', 'rowHeight', 'setProps', 'settings', 'stretchH', 'themeName', 'width']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'cellClassName', 'className', 'colHeaders', 'columnSorting', 'columns', 'contextMenu', 'data', 'dropdownMenu', 'filters', 'headerClassName', 'height', 'licenseKey', 'multiColumnSorting', 'rowHeaders', 'rowHeight', 'setProps', 'settings', 'stretchH', 'themeName', 'width']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(DashkitTable, self).__init__(**args)

setattr(DashkitTable, "__init__", _explicitize_args(DashkitTable.__init__))
