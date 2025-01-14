% Auto-generated: do not edit by hand
\name{mermaidExport}

\alias{mermaidExport}

\title{Mermaid_export component}

\description{
A Mermaid diagram component for Dash. Renders Mermaid diagrams from text definitions using Mermaid 11.4.1.
}

\usage{
mermaidExport(id=NULL, chart=NULL, className=NULL, config=NULL,
export_trigger=NULL)
}

\arguments{
\item{id}{Character. The ID used to identify this component in Dash callbacks.}

\item{chart}{Character. The Mermaid diagram definition in text format.}

\item{className}{Character. Optional CSS class name for the container div.}

\item{config}{Named list. Optional configuration object for Mermaid initialization.}

\item{export_trigger}{Numeric. Trigger for exporting the diagram as PNG. Increment to trigger export.}
}

\value{named list of JSON elements corresponding to React.js properties and their values}

