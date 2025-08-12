% Auto-generated: do not edit by hand
\name{dashkitTable}

\alias{dashkitTable}

\title{DashkitTable component}

\description{
DashkitTable is a modern Handsontable component for Dash with native theme support. * Provides a full-featured data grid with ergonomic defaults and theme-aware styling. Supports both record-style rows and 2D arrays. Pass additional Handsontable options via `settings`.
}

\usage{
dashkitTable(id=NULL, cellClassName=NULL, className=NULL,
colHeaders=NULL, columnSorting=NULL, columns=NULL,
contextMenu=NULL, data=NULL, dropdownMenu=NULL,
filters=NULL, headerClassName=NULL, height=NULL,
licenseKey=NULL, multiColumnSorting=NULL, rowHeaders=NULL,
rowHeight=NULL, settings=NULL, stretchH=NULL,
themeName=NULL, width=NULL)
}

\arguments{
\item{id}{Character. The ID used to identify this component in Dash callbacks.}

\item{cellClassName}{Character. Custom CSS class applied to all table cells.}

\item{className}{Character. Custom CSS class for the outer table container.}

\item{colHeaders}{Logical | numeric | character | named list | unnamed list. Show column headers.}

\item{columnSorting}{Logical | numeric | character | named list | unnamed list. Enable single-column sorting.}

\item{columns}{List of logical | numeric | character | named list | unnamed lists. Column configuration passed through to Handsontable.}

\item{contextMenu}{Logical | numeric | character | named list | unnamed list. Enable context menu.}

\item{data}{List of logical | numeric | character | named list | unnamed lists | list of list of logical | numeric | character | named list | unnamed listss. Data for the table. Accepts either:
- Array of objects (records) when used with column definitions using `data: <fieldName>`
- 2D array (matrix) when used with index-based columns (`data: <columnIndex>`)}

\item{dropdownMenu}{Logical | numeric | character | named list | unnamed list. Enable dropdown menu.}

\item{filters}{Logical | numeric | character | named list | unnamed list. Enable filter functionality.}

\item{headerClassName}{Character. Custom CSS class applied to all column/row headers.}

\item{height}{Character | numeric. Table height in pixels or CSS size.}

\item{licenseKey}{Character. Handsontable license key string.}

\item{multiColumnSorting}{Logical | numeric | character | named list | unnamed list. Enable multi-column sorting.}

\item{rowHeaders}{Logical | numeric | character | named list | unnamed list. Show row headers.}

\item{rowHeight}{Numeric. Row height in pixels.}

\item{settings}{Logical | numeric | character | named list | unnamed list. Additional Handsontable settings to merge into the base config.}

\item{stretchH}{Character. Column stretching behaviour.}

\item{themeName}{Character. Theme name for native Handsontable themes (e.g. `ht-theme-main`, `ht-theme-horizon`).}

\item{width}{Character | numeric. Table width in pixels or CSS size.}
}

\value{named list of JSON elements corresponding to React.js properties and their values}

