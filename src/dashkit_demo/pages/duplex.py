import sys
from pathlib import Path

import dash
from dash import html

sys.path.insert(0, str(Path(__file__).parent.parent.parent))

dash.register_page(
    __name__,
    path="/pcr/duplex",
    title="Duplex",
    icon="mynaui:flask",
    sidebar_section="PCR",
    sidebar_parent="PCR",
    sidebar_collapsible=True,
    sidebar_expanded=True,
)

layout = html.Div(
    [
        html.H1("Duplex PCR", className="text-3xl font-bold mb-6"),
        html.P(
            "Duplex PCR analysis for simultaneous amplification of two different targets.",
            className="text-gray-600 mb-4",
        ),
        html.Div(
            [
                html.H2("Duplex Configuration", className="text-xl font-semibold mb-3"),
                html.P(
                    "Configure and monitor duplex PCR reactions.",
                    className="text-gray-600 mb-4",
                ),
                html.Div(
                    [
                        html.A(
                            "Analysis",
                            href="/pcr/duplex/analysis",
                            className="bg-blue-500 text-white px-4 py-2 rounded mr-2 hover:bg-blue-600",
                        ),
                        html.A(
                            "Trending",
                            href="/pcr/duplex/trending",
                            className="bg-green-500 text-white px-4 py-2 rounded hover:bg-green-600",
                        ),
                    ]
                ),
            ],
            className="bg-white p-6 rounded-lg shadow",
        ),
    ],
    className="p-6",
)
