% Auto-generated: do not edit by hand
\name{barChart}

\alias{barChart}

\title{BarChart component}

\description{
BarChart renders a bar chart using shadcn/ui styling and Recharts.
}

\usage{
barChart(children=NULL, id=NULL, className=NULL, config=NULL,
data=NULL, dataKey=NULL, maxBarSize=NULL, radius=NULL,
showGrid=NULL, showLegend=NULL, showTooltip=NULL,
showXAxis=NULL, showYAxis=NULL, stackId=NULL, style=NULL,
xAxisKey=NULL, yAxisKey=NULL)
}

\arguments{
\item{children}{A list of or a singular dash component, string or number. Children components}

\item{id}{Character. The ID used to identify this component in Dash callbacks.}

\item{className}{Character. Custom CSS class for the container}

\item{config}{Named list. Chart configuration object with data key mappings and colors}

\item{data}{List of named lists. Array of data points for the chart}

\item{dataKey}{Character. The key in data objects to use for the bar values}

\item{maxBarSize}{Numeric. Maximum bar size}

\item{radius}{Numeric. Border radius for the bars}

\item{showGrid}{Logical | numeric | character | named list | unnamed list. Whether to show the grid}

\item{showLegend}{Logical | numeric | character | named list | unnamed list. Whether to show the legend}

\item{showTooltip}{Logical | numeric | character | named list | unnamed list. Whether to show tooltips}

\item{showXAxis}{Logical | numeric | character | named list | unnamed list. Whether to show the x-axis}

\item{showYAxis}{Logical | numeric | character | named list | unnamed list. Whether to show the y-axis}

\item{stackId}{Character. Stack ID for stacked bars}

\item{style}{Logical | numeric | character | named list | unnamed list. Custom styling}

\item{xAxisKey}{Character. The key in data objects to use for x-axis labels}

\item{yAxisKey}{Character. The key in data objects to use for y-axis labels}
}

\value{named list of JSON elements corresponding to React.js properties and their values}

