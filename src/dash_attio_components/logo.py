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
        html.Span(logo_text, className="ml-3 text-md font-semibold text-gray-900")
    )

    return html.Div(
        [
            html.Div(
                [
                    html.Div(logo_elements, className="flex items-center px-6 py-2"),
                ],
                className=f"border-b border-gray-200 flex items-center {height}",
            ),
        ]
    )


def BrandHeader(brand_name, icon=None, subtitle=None):
    """Brand header for main content areas."""
    header_content = []

    if icon:
        header_content.append(html.Span(icon, className="mr-2"))

    header_content.append(
        html.Span(brand_name, className="text-sm font-[500]  text-gray-900")
    )

    if subtitle:
        header_content.append(
            html.Span(subtitle, className="ml-2 text-sm text-gray-500")
        )

    return html.Nav(header_content, className="flex items-center")
