import sys
from pathlib import Path

import dash
from dash import html

sys.path.insert(0, str(Path(__file__).parent.parent.parent))

dash.register_page(__name__, path="/pcr", title="PCR", icon="dna")

layout = html.Div(
    [
        html.H1("PCR Dashboard", className="text-3xl font-bold mb-6"),
        html.P(
            "Polymerase Chain Reaction analysis and monitoring.",
            className="text-gray-600 mb-4",
        ),
        html.Div(
            [
                html.H2("Overview", className="text-xl font-semibold mb-3"),
                html.P(
                    "Monitor PCR processes, analyze results, and track trends.",
                    className="text-gray-600",
                ),
            ],
            className="bg-white p-6 rounded-lg shadow",
        ),
    ],
    className="p-6",
)
