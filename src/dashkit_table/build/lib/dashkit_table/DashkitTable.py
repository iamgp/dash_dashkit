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
DashkitTable is a modern Handsontable component for Dash with native theme support.
*
Provides a full-featured data grid with ergonomic defaults and theme-aware styling.
Supports both record-style rows and 2D arrays. Pass additional Handsontable options via `settings`.

Keyword arguments:

- id (string; optional):
    The ID used to identify this component in Dash callbacks.

- cellClassName (string; default ''):
    Custom CSS class applied to all table cells.

- className (string; default ''):
    Custom CSS class for the outer table container.

- colHeaders (boolean | number | string | dict | list; default True):
    Show column headers.

- columnSorting (boolean | number | string | dict | list; default True):
    Enable single-column sorting.

- columns (list of boolean | number | string | dict | lists; optional):
    Column configuration passed through to Handsontable.

- contextMenu (boolean | number | string | dict | list; default False):
    Enable context menu.

- data (list of boolean | number | string | dict | lists | list of list of boolean | number | string | dict | listss; optional):
    Data for the table. Accepts either: - Array of objects (records)
    when used with column definitions using `data: <fieldName>` - 2D
    array (matrix) when used with index-based columns (`data:
    <columnIndex>`).

- dropdownMenu (boolean | number | string | dict | list; default False):
    Enable dropdown menu.

- filters (boolean | number | string | dict | list; default False):
    Enable filter functionality.

- headerClassName (string; default ''):
    Custom CSS class applied to all column/row headers.

- height (string | number; default 400):
    Table height in pixels or CSS size.

- licenseKey (string; default 'non-commercial-and-evaluation'):
    Handsontable license key string.

- multiColumnSorting (boolean | number | string | dict | list; default False):
    Enable multi-column sorting.

- rowHeaders (boolean | number | string | dict | list; default False):
    Show row headers.

- rowHeight (number; default 35):
    Row height in pixels.

- setProps (optional):
    Callback used by Dash to push prop changes from the client.

- settings (boolean | number | string | dict | list; optional):
    Additional Handsontable settings to merge into the base config.

- stretchH (string; default 'all'):
    Column stretching behaviour.

- themeName (string; default 'ht-theme-main'):
    Theme name for native Handsontable themes (e.g. `ht-theme-main`,
    `ht-theme-horizon`).

- width (string | number; default '100%'):
    Table width in pixels or CSS size."""
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
