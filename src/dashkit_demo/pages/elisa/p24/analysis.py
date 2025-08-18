import dash
from dash import html

dash.register_page(
    __name__, path="/elisa/p24/analysis", title="Analysis", icon="chart-line"
)

layout = html.Div(
    [
        html.H1("Duplex PCR Analysis", className="text-3xl font-bold mb-6"),
        html.P(
            "Detailed analysis of duplex PCR results and data interpretation.",
            className="text-gray-600 mb-4",
        ),
        html.Div(
            [
                html.H2("Analysis Results", className="text-xl font-semibold mb-3"),
                html.P(
                    "Real-time analysis of duplex PCR amplification curves, melting curves, and quantification.",
                    className="text-gray-600 mb-4",
                ),
                html.Div(
                    [
                        html.Div(
                            [
                                html.H3("Target 1", className="font-semibold mb-2"),
                                html.P(
                                    "Ct value: 25.4", className="text-sm text-gray-600"
                                ),
                                html.P(
                                    "Efficiency: 98.2%",
                                    className="text-sm text-gray-600",
                                ),
                            ],
                            className="bg-blue-50 p-4 rounded mr-4",
                        ),
                        html.Div(
                            [
                                html.H3("Target 2", className="font-semibold mb-2"),
                                html.P(
                                    "Ct value: 23.1", className="text-sm text-gray-600"
                                ),
                                html.P(
                                    "Efficiency: 97.8%",
                                    className="text-sm text-gray-600",
                                ),
                            ],
                            className="bg-green-50 p-4 rounded",
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
