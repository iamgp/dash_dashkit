from dash import html, dcc


def MarkdownReport(content: str, title: str = None, className: str = "") -> html.Div:
    """Create a markdown report component with typography styling.
    
    Args:
        content: Markdown content to render
        title: Optional title for the report
        className: Additional CSS classes
    
    Returns:
        html.Div: Styled markdown report component
    """
    children = []
    
    if title:
        children.append(
            html.H1(title, className="text-3xl font-bold text-gray-900 dark:text-white mb-8")
        )
    
    children.append(
        dcc.Markdown(
            content, 
            className="prose max-w-none"
        )
    )
    
    return html.Div([
        html.Div(
            children, 
            className="p-8 max-w-4xl mx-auto"
        )
    ], className=f"bg-white dark:bg-gray-900 min-h-full overflow-auto {className}".strip())