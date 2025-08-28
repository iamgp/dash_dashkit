#!/usr/bin/env python3
"""Demo of the new callout components."""

import sys
from pathlib import Path

import dash
from dash import html

# Add the src directory to the Python path
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from dashkit import (
    CautionCallout,
    ImportantCallout,
    NoteCallout,
    TipCallout,
    WarningCallout,
    setup_app,
)

# Create Dash app
app = dash.Dash(__name__)
setup_app(app)

app.layout = html.Div(
    [
        html.H1(
            "Dashkit Callout Components Demo",
            className="text-3xl font-bold mb-8 text-center text-gray-900",
        ),
        # Light and Dark mode split view
        html.Div(
            [
                # Light mode section
                html.Div(
                    [
                        html.H2(
                            "Light Mode",
                            className="text-xl font-semibold mb-4 text-center text-gray-900",
                        ),
                        html.Div(
                            [
                                NoteCallout(
                                    "Useful information that users should know, even when skimming content."
                                ),
                                TipCallout(
                                    [
                                        "Helpful advice for doing things better or more easily. ",
                                        html.Strong("Pro tip: "),
                                        "Use callouts sparingly to maintain effectiveness.",
                                    ]
                                ),
                                ImportantCallout(
                                    "Key information users need to know to achieve their goal."
                                ),
                                WarningCallout(
                                    "Urgent info that needs immediate user attention to avoid problems."
                                ),
                                CautionCallout(
                                    [
                                        "Advises about risks or negative outcomes of certain actions. ",
                                        html.Strong("Be careful!"),
                                    ]
                                ),
                            ],
                            className="space-y-4 bg-white p-6 rounded-lg border border-gray-200",
                        ),
                    ],
                    className="flex-1",
                ),
                # Dark mode section
                html.Div(
                    [
                        html.H2(
                            "Dark Mode",
                            className="text-xl font-semibold mb-4 text-center text-white",
                        ),
                        html.Div(
                            [
                                NoteCallout(
                                    "Useful information that users should know, even when skimming content."
                                ),
                                TipCallout(
                                    [
                                        "Helpful advice for doing things better or more easily. ",
                                        html.Strong("Pro tip: "),
                                        "Use callouts sparingly to maintain effectiveness.",
                                    ]
                                ),
                                ImportantCallout(
                                    "Key information users need to know to achieve their goal."
                                ),
                                WarningCallout(
                                    "Urgent info that needs immediate user attention to avoid problems."
                                ),
                                CautionCallout(
                                    [
                                        "Advises about risks or negative outcomes of certain actions. ",
                                        html.Strong("Be careful!"),
                                    ]
                                ),
                            ],
                            className="dark space-y-4 bg-dashkit-gray-900 p-6 rounded-lg border border-gray-700",
                        ),
                    ],
                    className="flex-1",
                ),
            ],
            className="flex gap-8 max-w-7xl mx-auto p-8",
        ),
    ],
    className="min-h-screen bg-gray-100",
)

if __name__ == "__main__":
    print("Starting Dashkit Callout Demo...")
    print("Open http://127.0.0.1:8050 in your browser")
    app.run(debug=True)
