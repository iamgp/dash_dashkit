# AUTO GENERATED FILE - DO NOT EDIT
# ruff: noqa: UP007, UP008

import typing  # noqa: F401
from typing import Literal, NotRequired  # noqa: F401

from dash.development.base_component import Component, _explicitize_args

ComponentType = typing.Union[
    str,
    int,
    float,
    Component,
    None,
    typing.Sequence[str | int | float | Component | None],
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
    _base_nodes = ["children"]
    _namespace = "dash_attio_table"
    _type = "AttioTable"

    def __init__(
        self,
        id: str | dict | None = None,
        data: typing.Sequence[typing.Sequence[typing.Any]] | None = None,
        columns: typing.Sequence[typing.Any] | None = None,
        themeName: str | None = None,
        className: str | None = None,
        cellClassName: str | None = None,
        headerClassName: str | None = None,
        height: str | NumberType | None = None,
        width: str | NumberType | None = None,
        rowHeaders: typing.Any | None = None,
        colHeaders: typing.Any | None = None,
        licenseKey: str | None = None,
        columnSorting: typing.Any | None = None,
        multiColumnSorting: typing.Any | None = None,
        filters: typing.Any | None = None,
        dropdownMenu: typing.Any | None = None,
        contextMenu: typing.Any | None = None,
        rowHeight: NumberType | None = None,
        stretchH: str | None = None,
        settings: typing.Any | None = None,
        **kwargs,
    ):
        self._prop_names = [
            "id",
            "cellClassName",
            "className",
            "colHeaders",
            "columnSorting",
            "columns",
            "contextMenu",
            "data",
            "dropdownMenu",
            "filters",
            "headerClassName",
            "height",
            "licenseKey",
            "multiColumnSorting",
            "rowHeaders",
            "rowHeight",
            "setProps",
            "settings",
            "stretchH",
            "themeName",
            "width",
        ]
        self._valid_wildcard_attributes = []
        self.available_properties = [
            "id",
            "cellClassName",
            "className",
            "colHeaders",
            "columnSorting",
            "columns",
            "contextMenu",
            "data",
            "dropdownMenu",
            "filters",
            "headerClassName",
            "height",
            "licenseKey",
            "multiColumnSorting",
            "rowHeaders",
            "rowHeight",
            "setProps",
            "settings",
            "stretchH",
            "themeName",
            "width",
        ]
        self.available_wildcard_properties = []
        _explicit_args = kwargs.pop("_explicit_args")
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(AttioTable, self).__init__(**args)


AttioTable.__init__ = _explicitize_args(AttioTable.__init__)
