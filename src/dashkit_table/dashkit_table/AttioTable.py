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


class AttioTable(Component):
    """An AttioTable component.


Keyword arguments:

- id (string; optional):
    The ID used to identify this component in Dash callbacks.

- cellClassName (string; optional):
    Custom CSS class for table cells.

- className (string; optional):
    Custom CSS class for the table container.

- colHeaders (boolean | number | string | dict | list; optional):
    Show column headers.

- columnSorting (boolean | number | string | dict | list; optional):
    Enable column sorting.

- columns (list of boolean | number | string | dict | lists; optional):
    Column configuration.

- contextMenu (boolean | number | string | dict | list; optional):
    Enable context menu.

- data (list of list of boolean | number | string | dict | listss; optional):
    Data for the table.

- dropdownMenu (boolean | number | string | dict | list; optional):
    Enable dropdown menu.

- filters (boolean | number | string | dict | list; optional):
    Enable filters.

- headerClassName (string; optional):
    Custom CSS class for headers.

- height (string | number; optional):
    Table height.

- licenseKey (string; optional):
    License key for Handsontable.

- multiColumnSorting (boolean | number | string | dict | list; optional):
    Enable multi-column sorting.

- rowHeaders (boolean | number | string | dict | list; optional):
    Show row headers.

- rowHeight (number; optional):
    Custom row height.

- setProps (optional):
    Callback when data changes.

- settings (boolean | number | string | dict | list; optional):
    Any additional Handsontable settings.

- stretchH (string; optional):
    Stretch columns to fill container.

- themeName (string; optional):
    Theme name - supports Handsontable native themes.

- width (string | number; optional):
    Table width."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'dashkit_table'
    _type = 'AttioTable'


    def __init__(
        self,
        id: typing.Optional[typing.Union[str, dict]] = None,
        data: typing.Optional[typing.Union[typing.Sequence[typing.Sequence[typing.Any]]]] = None,
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

        super(AttioTable, self).__init__(**args)

setattr(AttioTable, "__init__", _explicitize_args(AttioTable.__init__))
