import dash_iconify
from dash import dcc, html


def PrimaryButton(children, icon=None, onClick=None, className="", **kwargs):
    """Primary action button with Dashkit styling."""
    button_children = []

    if icon:
        # Check if icon already has a prefix (contains ':')
        icon_name = icon if ":" in icon else f"mynaui:{icon}"
        button_children.append(
            dash_iconify.DashIconify(
                icon=icon_name,
                width=16,
                className="mr-2 align-middle inline-block w-4 h-4 shrink-0",
            )
        )

    if isinstance(children, str):
        button_children.append(children)
    else:
        button_children.extend(children if isinstance(children, list) else [children])

    combined_className = f"inline-flex items-center px-4 py-1.5 border border-transparent text-sm font-medium rounded-md text-white bg-blue-600 hover:bg-blue-700 focus:outline-none focus:ring-1 focus:ring-blue-500 transition-colors duration-150 dark:bg-blue-500 dark:hover:bg-blue-600 p-1 {className}".strip()

    props = {
        "className": combined_className,
        "children": button_children,
        **{k: v for k, v in kwargs.items() if k != "className"},
    }

    if onClick:
        props["id"] = kwargs.get("id", "primary-button")

    return html.Button(**props)


def SecondaryButton(
    children, icon=None, dropdown=False, onClick=None, className="", **kwargs
):
    """Secondary/navigation button with Dashkit styling."""
    button_children = []

    if icon:
        # Check if icon already has a prefix (contains ':')
        icon_name = icon if ":" in icon else f"mynaui:{icon}"
        button_children.append(
            dash_iconify.DashIconify(
                icon=icon_name,
                width=16,
                className="mr-2 align-middle inline-block w-4 h-4 shrink-0",
            )
        )

    if isinstance(children, str):
        button_children.append(children)
    else:
        button_children.extend(children if isinstance(children, list) else [children])

    if dropdown:
        button_children.append(
            dash_iconify.DashIconify(
                icon="mynaui:chevron-down",
                width=16,
                className="ml-2 align-middle inline-block w-4 h-4 shrink-0",
            )
        )

    combined_className = f"inline-flex items-center px-3 py-1 border border-gray-200 text-sm font-medium rounded-md text-gray-700 bg-white hover:bg-gray-50 focus:outline-none focus:ring-1 focus:ring-blue-500 focus:border-blue-500 transition-colors duration-150 dark:bg-dashkit-surface dark:border-dashkit-border-alt dark:text-dashkit-text-invert dark:hover:bg-dashkit-surface {className}".strip()

    props = {
        "className": combined_className,
        "children": button_children,
        **{k: v for k, v in kwargs.items() if k != "className"},
    }

    if onClick:
        props["id"] = kwargs.get("id", "secondary-button")

    return html.Button(**props)


def IconButton(icon, children=None, active=False, onClick=None, className="", **kwargs):
    """Icon-based button for navigation items."""
    # Check if icon already has a prefix (contains ':')
    icon_name = icon if ":" in icon else f"mynaui:{icon}"
    button_children = [
        dash_iconify.DashIconify(
            icon=icon_name,
            width=16,
            className="mr-2 text-dashkit-icon-light dark:text-dashkit-icon-dark align-middle inline-block w-4 h-4 shrink-0",
        )
    ]

    if children:
        if isinstance(children, str):
            button_children.append(
                html.Span(children, className="opacity-100 transition-all duration-200")
            )
        else:
            button_children.extend(
                children if isinstance(children, list) else [children]
            )

    active_class = "bg-dashkit-hover-light dark:bg-dashkit-hover-dark" if active else ""
    base_className = f"sidebar-item flex items-center px-2 py-1 text-sm font-medium rounded-lg hover:bg-dashkit-hover-light transition-colors duration-150 dark:hover:bg-dashkit-hover-dark text-dashkit-text dark:text-dashkit-text-invert break-words truncate mb-px tracking-sidebar {active_class}"
    combined_className = f"{base_className} {className}".strip()

    href = kwargs.get("href", "#")

    # Use dcc.Link for internal navigation, html.A for external links
    if href.startswith(("http://", "https://", "mailto:", "tel:")):
        props = {
            "className": combined_className,
            "children": button_children,
            "href": href,
            **{k: v for k, v in kwargs.items() if k not in ["href", "className"]},
        }

        if onClick:
            props["id"] = kwargs.get("id", "icon-button")

        return html.A(**props)
    else:
        props = {
            "className": combined_className,
            "children": button_children,
            "href": href,
            **{k: v for k, v in kwargs.items() if k not in ["href", "className"]},
        }

        if onClick:
            props["id"] = kwargs.get("id", "icon-button")

        return dcc.Link(**props)
