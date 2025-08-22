from typing import Any

from dash import dcc, html


def MarkdownReport(
    content: str,
    title: str | None = None,
    className: str = "",
) -> html.Div:
    """Create a markdown report component with typography styling.

    Args:
        content: Markdown content to render
        title: Optional title rendered within the report body
        className: Additional CSS classes

    Returns:
        html.Div: Styled markdown report component
    """
    children: list[Any] = []

    # Render title inside the markdown when provided (header is managed globally)
    if title:
        children.append(html.H1(title))

    children.append(
        dcc.Markdown(content, className="prose prose-sm dark:prose-invert max-w-none")
    )

    return html.Div(
        children,
        className=(
            f"min-h-full overflow-auto [&_h1:first-child]:mt-0 {className}"
        ).strip(),
    )
