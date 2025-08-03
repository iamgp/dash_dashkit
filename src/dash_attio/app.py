import sys
from pathlib import Path

# Add the current directory to the path for imports
sys.path.insert(0, str(Path(__file__).parent))

from dash import Dash, html

from components.layout import create_layout

# External stylesheets including Font Awesome for icons
external_stylesheets = [
    "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css",
]

app = Dash(__name__, external_stylesheets=external_stylesheets)

# Serve custom CSS by embedding it in the index string
app.index_string = '''
<!DOCTYPE html>
<html>
    <head>
        {%metas%}
        <title>{%title%}</title>
        {%favicon%}
        {%css%}
        <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css" rel="stylesheet">
        <style>
            ''' + open(Path(__file__).parent / "assets/style.css").read() + '''
        </style>
    </head>
    <body>
        {%app_entry%}
        <footer>
            {%config%}
            {%scripts%}
            {%renderer%}
        </footer>
    </body>
</html>
'''

# Example content for the main area - proper Attio-style table
example_content = html.Div([
    # Top section with count and actions
    html.Div([
        html.Div([
            html.Span("10 count", className="text-sm text-gray-500"),
        ], className="flex items-center"),
        
        html.Button([
            html.I(className="fas fa-plus mr-1 text-xs"),
            "Add calculation",
        ], className="text-sm text-blue-600 hover:text-blue-700 font-medium"),
    ], className="flex items-center justify-between px-6 py-4 bg-white border-b border-gray-200"),

    # Full-width table
    html.Div([
        # Table header
        html.Div([
            html.Div("Company", className="text-left text-xs font-medium text-gray-500 uppercase tracking-wider"),
            html.Div("Categories", className="text-left text-xs font-medium text-gray-500 uppercase tracking-wider"),
            html.Div("LinkedIn", className="text-left text-xs font-medium text-gray-500 uppercase tracking-wider"),
            html.Div("Last interaction", className="text-left text-xs font-medium text-gray-500 uppercase tracking-wider"),
            html.Div("Connection strength", className="text-left text-xs font-medium text-gray-500 uppercase tracking-wider"),
            html.Div("Twitter followers", className="text-left text-xs font-medium text-gray-500 uppercase tracking-wider"),
            html.Div("Twitter", className="text-left text-xs font-medium text-gray-500 uppercase tracking-wider"),
        ], className="grid grid-cols-7 gap-8 px-6 py-3 bg-gray-50 border-b border-gray-200"),

        # Table rows
        *[html.Div([
            # Company column
            html.Div([
                html.Div([
                    html.Div(className="w-8 h-8 rounded-full bg-gray-200 flex items-center justify-center text-gray-600 text-sm font-semibold mr-3", children=company[0]),
                    html.Span(company, className="text-sm font-medium text-gray-900"),
                ], className="flex items-center"),
            ], className="flex items-center"),
            
            # Categories column
            html.Div([
                html.Span(category, className="inline-flex items-center px-2 py-1 rounded-md text-xs font-medium bg-blue-100 text-blue-800 mr-1 mb-1")
                for category in categories[:2]  # Only show first 2 categories
            ] + ([html.Span(f"+{len(categories)-2}", className="text-xs text-gray-400")] if len(categories) > 2 else []),
                className="flex flex-wrap items-center"
            ),
            
            # LinkedIn column
            html.Div("No contact", className="text-sm text-gray-500"),
            
            # Last interaction column
            html.Div("No communication", className="text-sm text-gray-500"),
            
            # Connection strength column
            html.Div("", className="text-sm text-gray-500"),
            
            # Twitter followers column
            html.Div(f"{followers:,}" if isinstance(followers, int) else followers, className="text-sm text-gray-900 font-medium"),
            
            # Twitter column
            html.Div([
                html.A(twitter, href="#", className="text-sm text-blue-600 hover:text-blue-700 font-medium"),
            ], className=""),
            
        ], className="grid grid-cols-7 gap-8 px-6 py-4 bg-white border-b border-gray-100 hover:bg-gray-50 transition-colors duration-150")
        for company, categories, followers, twitter in [
            ("United Airlines", ["Airlines", "B2C", "E-commerce", "Transport"], "1,174,209", "united"),
            ("Airbnb", ["B2C", "Information", "Internet", "Marketplace"], "883,549", "Airbnb"),
            ("Attio", ["Automation", "B2B", "Enterprise", "Information"], "1,340", "attio"),
            ("Google", ["B2B", "B2C", "Broadcasting", "Information"], "28,946,065", "Google"),
            ("Microsoft", ["B2B", "Enterprise", "Information", "Publishing"], "12,814,907", "Microsoft"),
        ]],

    ], className="bg-white"),

], className="")

app.layout = create_layout(example_content)

if __name__ == "__main__":
    app.run(debug=True)
