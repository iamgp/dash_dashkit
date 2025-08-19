% Auto-generated: do not edit by hand
\name{contributionGraph}

\alias{contributionGraph}

\title{ContributionGraph component}

\description{
ContributionGraph is the main container for a GitHub-style contribution graph. This is a composable component that should contain ContributionGraphCalendar and other contribution graph components.
}

\usage{
contributionGraph(children=NULL, id=NULL, className=NULL, data=NULL,
style=NULL)
}

\arguments{
\item{children}{A list of or a singular dash component, string or number. Children components}

\item{id}{Character. The ID used to identify this component in Dash callbacks.}

\item{className}{Character. Custom CSS class for the container}

\item{data}{Logical | numeric | character | named list | unnamed list. Array of contribution data with date and count}

\item{style}{Logical | numeric | character | named list | unnamed list. Custom styling}
}

\value{named list of JSON elements corresponding to React.js properties and their values}

