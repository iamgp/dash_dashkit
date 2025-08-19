% Auto-generated: do not edit by hand
\name{contributionGraphBlock}

\alias{contributionGraphBlock}

\title{ContributionGraphBlock component}

\description{
ContributionGraphBlock represents a single day in the contribution calendar.
}

\usage{
contributionGraphBlock(id=NULL, activity=NULL, className=NULL, count=NULL,
date=NULL, dayIndex=NULL, margin=NULL, onClick=NULL,
radius=NULL, size=NULL, style=NULL, weekIndex=NULL)
}

\arguments{
\item{id}{Character. The ID used to identify this component in Dash callbacks.}

\item{activity}{Numeric. Activity level (0-4)}

\item{className}{Character. Custom CSS class}

\item{count}{Numeric. Count of contributions}

\item{date}{Character. Date string in ISO format}

\item{dayIndex}{Numeric. Day index in the week (0-6)}

\item{margin}{Numeric. Block margin in pixels}

\item{onClick}{Click handler}

\item{radius}{Numeric. Block border radius in pixels}

\item{size}{Numeric. Block size in pixels}

\item{style}{Logical | numeric | character | named list | unnamed list. Custom styling}

\item{weekIndex}{Numeric. Week index in the calendar}
}

\value{named list of JSON elements corresponding to React.js properties and their values}

