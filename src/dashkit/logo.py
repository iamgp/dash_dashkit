import dash_iconify
from dash import html


def LogoSection(logo_text, logo_icon=None, logo_bg="bg-blue-600", height="h-12"):
    """Reusable logo section component."""
    logo_elements = []

    if logo_icon:
        logo_elements.append(
            html.Span(
                logo_icon,
                className=f"inline-flex items-center justify-center w-6 h-6 {logo_bg} text-white font-semibold rounded-lg text-sm",
            )
        )

    logo_elements.append(
        html.Span(
            logo_text,
            className="opacity-100 transition-all duration-200 ml-3 text-md font-semibold text-dashkit-text dark:text-dashkit-text-invert",
        )
    )

    # Add collapse button
    collapse_button = html.Button(
        dash_iconify.DashIconify(
            icon="mynaui:sidebar",
            width=16,
            height=16,
            className="text-dashkit-icon-light dark:text-dashkit-icon-dark align-middle inline-block w-4 h-4 shrink-0",
        ),
        id="sidebar-collapse-toggle",
        className="ml-auto mr-2 p-1.5 rounded-md hover:bg-dashkit-hover-light dark:hover:bg-dashkit-hover-dark transition-colors duration-150 cursor-pointer",
        title="Toggle sidebar",
    )

    return html.Div(
        [
            html.Div(
                [
                    html.Div(
                        logo_elements,
                        className="flex items-center px-2.5 py-2",
                    ),
                    collapse_button,
                ],
                className=f"border-b border-dashkit-border-light dark:border-dashkit-border-dark flex items-center justify-between {height}",
            ),
        ]
    )


def BrandHeader(brand_name, icon=None, subtitle=None):
    """Brand header for main content areas."""
    header_content = []

    # Add collapsed sidebar toggle button (hidden by default)
    collapse_toggle = html.Button(
        dash_iconify.DashIconify(
            icon="mynaui:sidebar",
            width=16,
            height=16,
            className="text-dashkit-icon-light dark:text-dashkit-icon-dark align-middle inline-block w-4 h-4 shrink-0",
        ),
        id="header-sidebar-toggle",
        className="hidden mr-3 p-1.5 rounded-md hover:bg-dashkit-hover-light dark:hover:bg-dashkit-hover-dark transition-colors duration-150 cursor-pointer",
        title="Show sidebar",
    )
    header_content.append(collapse_toggle)

    if icon:
        # Check if icon is a dash_iconify icon name (contains ':') or emoji/text
        if ":" in icon:
            header_content.append(
                dash_iconify.DashIconify(
                    icon=icon,
                    width=16,
                    height=16,
                    className="mr-2 text-dashkit-icon-light dark:text-dashkit-icon-dark",
                )
            )
        else:
            header_content.append(html.Span(icon, className="mr-2"))

    header_content.append(
        html.Span(
            brand_name or "",
            id="brand-header-title",
            className="text-md text-dashkit-text dark:text-dashkit-text-invert",
        )
    )

    if subtitle:
        header_content.append(
            html.Span(subtitle, className="ml-2 text-sm text-gray-500")
        )

    return html.Nav(header_content, className="flex items-center")
