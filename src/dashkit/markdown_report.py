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
        title: Optional title rendered within the report body and used in header
        className: Additional CSS classes

    Returns:
        html.Div: Styled markdown report component
    """
    children: list[Any] = []

    # If title provided, use it to update header via Store consumed by header
    if title:
        children.append(dcc.Store(id="page_header_config", data={"title": title}))

    children.append(
        dcc.Markdown(content, className="prose prose-sm dark:prose-invert max-w-none")
    )

    return html.Div(
        children,
        className=(
            f"min-h-full overflow-auto [&_h1:first-child]:mt-0 {className}"
        ).strip(),
    )
