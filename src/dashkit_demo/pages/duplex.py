import dash
from dash import html, dcc

# Register Duplex as a sidebar container only (no actual page content)
dash.register_page(
    __name__,
    path="/duplex-container",  # Use a non-intuitive path since this shouldn't be accessed directly
    title="Duplex",
    sidebar_section="PCR",
    sidebar_container_only=True,  # This makes it a container without a real page
    sidebar_expanded=True,
    sidebar_order=1,
    icon="two-circles",
)

# Layout redirects to a child page since this is a container-only item
layout = html.Div(
    [
        dcc.Location(id="redirect-location", refresh=True),
        html.Script(
            """
        // Redirect to the first child page (Analysis)
        window.location.href = '/analysis';
        """
        ),
        html.Div(
            [
                html.H1("Redirecting...", className="text-gray-500"),
                html.P("This is a navigation container. Redirecting to Analysis page."),
            ],
            className="p-6",
        ),
    ]
)
