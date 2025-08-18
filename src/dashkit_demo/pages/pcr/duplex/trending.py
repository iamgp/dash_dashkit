import dash
from dash import html

dash.register_page(
    __name__, path="/pcr/duplex/trending", title="Trending", icon="trending-up"
)

layout = html.Div(
    [
        html.H1("Duplex PCR Trending", className="text-3xl font-bold mb-6"),
        html.P(
            "Historical trends and patterns in duplex PCR performance over time.",
            className="text-gray-600 mb-4",
        ),
        html.Div(
            [
                html.H2("Performance Trends", className="text-xl font-semibold mb-3"),
                html.P(
                    "Track efficiency, consistency, and quality metrics across multiple runs.",
                    className="text-gray-600 mb-4",
                ),
                html.Div(
                    [
                        html.Div(
                            [
                                html.H3(
                                    "Weekly Efficiency", className="font-semibold mb-2"
                                ),
                                html.P(
                                    "Average: 97.5%", className="text-sm text-gray-600"
                                ),
                                html.P(
                                    "Trend: +0.3%", className="text-sm text-green-600"
                                ),
                            ],
                            className="bg-blue-50 p-4 rounded mr-4",
                        ),
                        html.Div(
                            [
                                html.H3("Success Rate", className="font-semibold mb-2"),
                                html.P(
                                    "Current: 94.2%", className="text-sm text-gray-600"
                                ),
                                html.P(
                                    "Trend: +1.2%", className="text-sm text-green-600"
                                ),
                            ],
                            className="bg-green-50 p-4 rounded mr-4",
                        ),
                        html.Div(
                            [
                                html.H3("Run Time", className="font-semibold mb-2"),
                                html.P(
                                    "Average: 2.1h", className="text-sm text-gray-600"
                                ),
                                html.P(
                                    "Trend: -5min", className="text-sm text-green-600"
                                ),
                            ],
                            className="bg-yellow-50 p-4 rounded",
                        ),
                    ],
                    className="flex",
                ),
            ],
            className="bg-white p-6 rounded-lg shadow",
        ),
    ],
    className="p-6",
)
