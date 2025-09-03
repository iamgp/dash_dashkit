import dash_iconify
from dash import Input, Output, State, clientside_callback, dcc, html


def create_theme_toggle() -> html.Div:
    """Create a theme toggle with clear visual indication of the selected theme."""
    return html.Div(
        [
            html.Div(
                [
                    # System theme option
                    html.Button(
                        dash_iconify.DashIconify(
                            icon="mynaui:desktop",
                            width=16,
                            height=16,
                            className="text-dashkit-icon-light dark:text-dashkit-icon-dark align-middle inline-block w-4 h-4 shrink-0",
                        ),
                        id="theme-system",
                        className="p-1.5 rounded-md hover:bg-dashkit-hover-light dark:hover:bg-dashkit-hover-dark transition-colors duration-150 cursor-pointer",
                        title="System theme",
                    ),
                    # Light theme option
                    html.Button(
                        dash_iconify.DashIconify(
                            icon="mynaui:sun",
                            width=16,
                            height=16,
                            className="text-dashkit-icon-light dark:text-dashkit-icon-dark align-middle inline-block w-4 h-4 shrink-0",
                        ),
                        id="theme-light",
                        className="p-1.5 rounded-md hover:bg-dashkit-hover-light dark:hover:bg-dashkit-hover-dark transition-colors duration-150 cursor-pointer",
                        title="Light theme",
                    ),
                    # Dark theme option
                    html.Button(
                        dash_iconify.DashIconify(
                            icon="mynaui:moon-star",
                            width=16,
                            height=16,
                            className="text-dashkit-icon-light dark:text-dashkit-icon-dark align-middle inline-block w-4 h-4 shrink-0",
                        ),
                        id="theme-dark",
                        className="p-1.5 rounded-md hover:bg-dashkit-hover-light dark:hover:bg-dashkit-hover-dark transition-colors duration-150 cursor-pointer",
                        title="Dark theme",
                    ),
                ],
                className="inline-flex gap-1",
            )
        ],
        id="theme-toggle-container",
    )


class ThemeManager(html.Div):
    def __init__(self, id: str = "theme-manager"):
        super().__init__(
            id=id,
            children=[
                dcc.Store(id="theme-store", storage_type="local"),
                dcc.Store(id="system-theme-trigger", data={"timestamp": 0}),
                dcc.Location(id="url", refresh=False),
            ],
        )

        clientside_callback(
            """
            function(pathname, data) {
                console.log('Clientside callback (dcc.Location) triggered.');
                const storedTheme = localStorage.getItem('theme');
                const theme = storedTheme || 'system';
                console.log('Clientside callback (dcc.Location) - Theme:', theme);

                // Apply theme based on preference
                if (theme === 'system') {
                    const systemPrefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
                    document.documentElement.classList.toggle('dark', systemPrefersDark);
                } else {
                    document.documentElement.classList.toggle('dark', theme === 'dark');
                }

                return { theme: theme };
            }
            """,
            Output("theme-store", "data"),
            Input("url", "pathname"),
            State("theme-store", "data"),
        )

        # System theme button callback
        clientside_callback(
            """
            function(n_clicks) {
                if (n_clicks > 0) {
                    console.log('Setting theme to: system');
                    const systemPrefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
                    document.documentElement.classList.toggle('dark', systemPrefersDark);
                    localStorage.removeItem('theme'); // Use system default

                    // Emit custom theme change event
                    window.dispatchEvent(new CustomEvent('dashkit:theme-changed', {
                        detail: { theme: 'system', isDark: systemPrefersDark }
                    }));

                    return { theme: 'system' };
                }
                return window.dash_clientside.no_update;
            }
            """,
            Output("theme-store", "data", allow_duplicate=True),
            Input("theme-system", "n_clicks"),
            prevent_initial_call=True,
        )

        # Light theme button callback
        clientside_callback(
            """
            function(n_clicks) {
                if (n_clicks > 0) {
                    console.log('Setting theme to: light');
                    document.documentElement.classList.remove('dark');
                    localStorage.setItem('theme', 'light');

                    // Emit custom theme change event
                    window.dispatchEvent(new CustomEvent('dashkit:theme-changed', {
                        detail: { theme: 'light', isDark: false }
                    }));

                    return { theme: 'light' };
                }
                return window.dash_clientside.no_update;
            }
            """,
            Output("theme-store", "data", allow_duplicate=True),
            Input("theme-light", "n_clicks"),
            prevent_initial_call=True,
        )

        # Dark theme button callback
        clientside_callback(
            """
            function(n_clicks) {
                if (n_clicks > 0) {
                    console.log('Setting theme to: dark');
                    document.documentElement.classList.add('dark');
                    localStorage.setItem('theme', 'dark');

                    // Emit custom theme change event
                    window.dispatchEvent(new CustomEvent('dashkit:theme-changed', {
                        detail: { theme: 'dark', isDark: true }
                    }));

                    return { theme: 'dark' };
                }
                return window.dash_clientside.no_update;
            }
            """,
            Output("theme-store", "data", allow_duplicate=True),
            Input("theme-dark", "n_clicks"),
            prevent_initial_call=True,
        )

        clientside_callback(
            """
            function(data, triggerData) {
                const theme = data && data.theme ? data.theme : 'system';
                console.log('Clientside callback - Updating table theme to:', theme);

                let isDark = false;
                if (theme === 'dark') {
                    isDark = true;
                } else if (theme === 'system') {
                    // If we have trigger data, use that, otherwise check current system preference
                    if (triggerData && typeof triggerData.isDark === 'boolean') {
                        isDark = triggerData.isDark;
                    } else {
                        isDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
                    }

                    // Set up listener for system theme changes when using system theme
                    const mediaQuery = window.matchMedia('(prefers-color-scheme: dark)');
                    const updateTableTheme = (e) => {
                        console.log('System preference changed, updating table theme to:', e.matches ? 'dark' : 'light');

                        // Update the trigger store to force table theme callback to re-run
                        if (window.dash_clientside && window.dash_clientside.set_props) {
                            window.dash_clientside.set_props('system-theme-trigger', {
                                data: { timestamp: Date.now(), isDark: e.matches }
                            });
                        }
                    };

                    // Remove any existing listener to prevent duplicates
                    if (window.tableThemeSystemListener) {
                        mediaQuery.removeEventListener('change', window.tableThemeSystemListener);
                    }
                    window.tableThemeSystemListener = updateTableTheme;
                    mediaQuery.addEventListener('change', updateTableTheme);
                } else {
                    // Remove system theme listener when not using system theme
                    if (window.tableThemeSystemListener) {
                        const mediaQuery = window.matchMedia('(prefers-color-scheme: dark)');
                        mediaQuery.removeEventListener('change', window.tableThemeSystemListener);
                        window.tableThemeSystemListener = null;
                    }
                }

                return isDark ? "ht-theme-main-dark" : "ht-theme-main";
            }
            """,
            Output("companies-table", "themeName"),
            [Input("theme-store", "data"), Input("system-theme-trigger", "data")],
            prevent_initial_call=False,
        )

        # Update button states based on current theme
        clientside_callback(
            r"""
            function(data) {
                const theme = data && data.theme ? data.theme : 'system';
                console.log('Clientside callback - Updating theme buttons for:', theme);

                // Get all theme buttons
                const systemBtn = document.getElementById('theme-system');
                const lightBtn = document.getElementById('theme-light');
                const darkBtn = document.getElementById('theme-dark');

                // Define active and inactive styles
                const activeClasses = 'bg-dashkit-hover-light dark:bg-dashkit-hover-dark';
                const inactiveClasses = '';

                // Reset all buttons to inactive state
                [systemBtn, lightBtn, darkBtn].forEach(btn => {
                    if (btn) {
                        btn.className = btn.className.replace(/\bbg-dashkit-hover-light\b|\bbg-dashkit-hover-dark\b/g, '');
                    }
                });

                // Set active button based on theme
                let activeBtn;
                if (theme === 'system') activeBtn = systemBtn;
                else if (theme === 'light') activeBtn = lightBtn;
                else if (theme === 'dark') activeBtn = darkBtn;

                if (activeBtn) {
                    activeBtn.className = activeBtn.className.replace(/\bbg-dashkit-hover-light\b|\bbg-dashkit-hover-dark\b/g, '');
                    activeBtn.className += ' ' + activeClasses;
                }

                // Set up system preference change listener for system theme
                if (theme === 'system') {
                    const mediaQuery = window.matchMedia('(prefers-color-scheme: dark)');
                    const handleSystemChange = (e) => {
                        document.documentElement.classList.toggle('dark', e.matches);

                        // Emit custom theme change event for system theme changes
                        window.dispatchEvent(new CustomEvent('dashkit:theme-changed', {
                            detail: { theme: 'system', isDark: e.matches }
                        }));

                        // Trigger table theme update by updating the theme store
                        const themeStore = document.querySelector('#theme-store');
                        if (themeStore && window.dash_clientside) {
                            // Force table theme callback to re-run
                            window.dispatchEvent(new CustomEvent('dash:clientside-callback', {
                                detail: { output: 'companies-table.themeName' }
                            }));
                        }
                    };
                    // Remove any existing listener to prevent duplicates
                    if (window.systemThemeListener) {
                        mediaQuery.removeEventListener('change', window.systemThemeListener);
                    }
                    window.systemThemeListener = handleSystemChange;
                    mediaQuery.addEventListener('change', handleSystemChange);
                }

                return window.dash_clientside.no_update;
            }
            """,
            Output("theme-toggle-container", "children"),
            Input("theme-store", "data"),
            prevent_initial_call=False,
        )

        # Add mantine and plotly theme management callback
        clientside_callback(
            """
            function(data) {
                const theme = data && data.theme ? data.theme : 'system';
                let isDark = false;

                if (theme === 'dark') {
                    isDark = true;
                } else if (theme === 'system') {
                    isDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
                }

                // Update Mantine theme
                const mantineProvider = document.querySelector('[data-mantine-color-scheme]');
                if (mantineProvider) {
                    mantineProvider.setAttribute('data-mantine-color-scheme', isDark ? 'dark' : 'light');
                }

                // Update all Plotly figures to use dark theme
                if (window.Plotly) {
                    const plotlyDivs = document.querySelectorAll('div[id*="graph"], div.plotly-graph-div');
                    plotlyDivs.forEach(div => {
                        if (div._fullData && div._fullLayout) {
                            const newTemplate = isDark ? 'plotly_dark' : 'plotly';
                            window.Plotly.relayout(div, {
                                template: newTemplate
                            });
                        }
                    });
                }

                // Listen for theme change events and update themes accordingly
                if (!window.themeChangeListener) {
                    window.themeChangeListener = function(event) {
                        const isDarkTheme = event.detail.isDark;

                        // Update Mantine theme
                        const mantineProvider = document.querySelector('[data-mantine-color-scheme]');
                        if (mantineProvider) {
                            mantineProvider.setAttribute('data-mantine-color-scheme', isDarkTheme ? 'dark' : 'light');
                        }

                        // Update Plotly figures
                        if (window.Plotly) {
                            const plotlyDivs = document.querySelectorAll('div[id*="graph"], div.plotly-graph-div');
                            plotlyDivs.forEach(div => {
                                if (div._fullData && div._fullLayout) {
                                    const newTemplate = isDarkTheme ? 'plotly_dark' : 'plotly';
                                    window.Plotly.relayout(div, {
                                        template: newTemplate
                                    });
                                }
                            });
                        }
                    };
                    window.addEventListener('dashkit:theme-changed', window.themeChangeListener);
                }

                return window.dash_clientside.no_update;
            }
            """,
            Output("theme-store", "storage_type"),
            Input("theme-store", "data"),
            prevent_initial_call=False,
        )
