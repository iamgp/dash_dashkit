% Auto-generated: do not edit by hand
\name{chartContainer}

\alias{chartContainer}

\title{ChartContainer component}

\description{

}

\usage{
chartContainer(children=NULL, id=NULL, className=NULL, config=NULL,
key=NULL, ref=NULL)
}

\arguments{
\item{children}{Lists containing elements 'type', 'props', 'key'.
those elements have the following types:
  - type (character; required)
  - props (logical | numeric | character | named list | unnamed list; required)
  - key (character; required). }

\item{id}{Character. }

\item{className}{Character. }

\item{config}{List with named elements and values of type lists containing elements 'label', 'icon', 'color', 'theme'.
those elements have the following types:
  - label (a list of or a singular dash component, string or number; optional)
  - icon (logical | numeric | character | named list | unnamed list; optional)
  - color (character; optional)
  - theme (optional): . theme has the following type: lists containing elements 'light', 'dark'.
those elements have the following types:
  - light (character; required)
  - dark (character; required). }

\item{key}{Character | numeric. }

\item{ref}{Character. Allows getting a ref to the component instance.
Once the component unmounts, React will set `ref.current` to `null`
(or call the ref with `null` if you passed a callback ref).
@,see,,{@link ,https://react.dev/learn/referencing-values-with-refs#refs-and-the-dom React Docs,}}
}

\value{named list of JSON elements corresponding to React.js properties and their values}

