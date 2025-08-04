from dash import dcc, html, Input, Output, State, clientside_callback


def create_dark_mode_toggle() -> html.Button:
    """Create a dark mode toggle button."""
    return html.Button(
        [
            # Sun icon for light mode
            html.I(className="fas fa-sun text-gray-500 dark:text-gray-400"),
            # Moon icon for dark mode (hidden by default)
            html.I(className="fas fa-moon text-gray-500 dark:text-gray-400"),
        ],
        id="dark-mode-toggle",
        className="p-2 rounded-full hover:bg-gray-100 dark:hover:bg-gray-700",
    )


class ThemeManager(html.Div):
    def __init__(self, id: str = "theme-manager"):
        super().__init__(
            id=id,
            children=[
                dcc.Store(id="theme-store", storage_type="local"),
                dcc.Location(id='url', refresh=False),
            ]
        )

        clientside_callback(
            """
            function(pathname, data) {
                console.log('Clientside callback (dcc.Location) triggered.');
                const storedTheme = localStorage.getItem('theme');
                if (storedTheme) {
                    console.log('Clientside callback (dcc.Location) - Stored theme:', storedTheme);
                    return { theme: storedTheme };
                }
                console.log('Clientside callback (dcc.Location) - No stored theme, returning no_update.');
                return window.dash_clientside.no_update;
            }
            """,
            Output('theme-store', 'data'),
            Input('url', 'pathname'),
            State('theme-store', 'data'),
        )

        clientside_callback(
            """
            function(n_clicks, data) {
                if (n_clicks > 0) {
                    const currentTheme = data && data.theme ? data.theme : 'light';
                    const newTheme = currentTheme === 'light' ? 'dark' : 'light';
                    console.log('Toggling theme to:', newTheme);
                    document.documentElement.classList.toggle('dark', newTheme === 'dark');
                    localStorage.setItem('theme', newTheme);
                    return { theme: newTheme };
                }
                return window.dash_clientside.no_update;
            }
            """,
            Output("theme-store", "data", allow_duplicate=True),
            Input("dark-mode-toggle", "n_clicks"),
            State("theme-store", "data"),
            prevent_initial_call=True,
        )

        clientside_callback(
            """
            function(data) {
                const theme = data && data.theme ? data.theme : 'light';
                console.log('Clientside callback - Updating table theme to:', theme);
                if (theme === 'dark') {
                    return "ht-theme-main-dark";
                }
                return "ht-theme-main";
            }
            """,
            Output("attio-table", "themeName"),
            Input("theme-store", "data"),
            prevent_initial_call=False
        )
