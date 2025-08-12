from dash import html


def PrimaryButton(children, icon=None, onClick=None, className="", **kwargs):
    """Primary action button with Dashkit styling."""
    button_children = []

    if icon:
        button_children.append(html.I(className=f"{icon} mr-2"))

    if isinstance(children, str):
        button_children.append(children)
    else:
        button_children.extend(children if isinstance(children, list) else [children])

    # Combine base class with any additional classes
    combined_className = f"primary-button {className} p-1".strip()

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
        button_children.append(html.I(className=f"{icon} mr-2"))

    if isinstance(children, str):
        button_children.append(children)
    else:
        button_children.extend(children if isinstance(children, list) else [children])

    if dropdown:
        button_children.append(html.I(className="fas fa-chevron-down ml-2"))

    # Combine base class with any additional classes
    combined_className = f"nav-button {className}".strip()

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
    button_children = [html.I(className=f"{icon} mr-2")]

    if children:
        if isinstance(children, str):
            button_children.append(html.Span(children))
        else:
            button_children.extend(
                children if isinstance(children, list) else [children]
            )

    # Combine base classes with any additional classes
    base_className = f"sidebar-item {'active' if active else ''}"
    combined_className = f"{base_className} {className}".strip()

    props = {
        "className": combined_className,
        "children": button_children,
        "href": kwargs.get("href", "#"),
        **{k: v for k, v in kwargs.items() if k not in ["href", "className"]},
    }

    if onClick:
        props["id"] = kwargs.get("id", "icon-button")

    return html.A(**props)
