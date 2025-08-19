% Auto-generated: do not edit by hand
\name{contributionGraphCalendar}

\alias{contributionGraphCalendar}

\title{ContributionGraphCalendar component}

\description{
ContributionGraphCalendar renders the calendar grid for contributions.
}

\usage{
contributionGraphCalendar(children=NULL, id=NULL, blockMargin=NULL, blockRadius=NULL,
blockSize=NULL, className=NULL, data=NULL,
monthsToShow=NULL, showMonthLabels=NULL, showTooltips=NULL,
showWeekdayLabels=NULL, tooltipFormat=NULL)
}

\arguments{
\item{children}{Character | numeric. Children render function or components}

\item{id}{Character. The ID used to identify this component in Dash callbacks.}

\item{blockMargin}{Numeric. Block margin in pixels}

\item{blockRadius}{Numeric. Block border radius in pixels}

\item{blockSize}{Numeric. Block size in pixels}

\item{className}{Character. Custom CSS class}

\item{data}{Logical | numeric | character | named list | unnamed list. Array of contribution data}

\item{monthsToShow}{Numeric. Number of months to show}

\item{showMonthLabels}{Logical | numeric | character | named list | unnamed list. Show month labels}

\item{showTooltips}{Logical | numeric | character | named list | unnamed list. Enable tooltips}

\item{showWeekdayLabels}{Logical | numeric | character | named list | unnamed list. Show weekday labels}

\item{tooltipFormat}{Character. Custom tooltip format string. Use {count}, {date}, {dayName}, {monthName}, {year} as placeholders}
}

\value{named list of JSON elements corresponding to React.js properties and their values}

