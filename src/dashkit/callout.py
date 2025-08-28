from typing import Any, Literal

from dash import html
from dash_iconify import DashIconify


def Callout(
    children: Any,
    variant: Literal["note", "tip", "important", "warning", "caution"] = "note",
    className: str = "",
    **kwargs: Any,
) -> html.Div:
    """
    Callout component for displaying important information with different styling variants.

    Args:
        children: Content to display inside the callout
        variant: The type of callout (note, tip, important, warning, caution)
        className: Additional CSS classes
        **kwargs: Additional props passed to the outer div
    """
    # Icon and styling configurations for each variant - using MynaUI icons
    variant_config = {
        "note": {
            "icon": "mynaui:info-circle",
            "title": "Note",
            "border_color": "border-l-4 border-l-blue-500",
            "icon_color": "text-blue-500",
            "title_color": "text-blue-500 font-semibold",
        },
        "tip": {
            "icon": "mynaui:danger-circle",
            "title": "Tip",
            "border_color": "border-l-4 border-l-green-500",
            "icon_color": "text-green-500",
            "title_color": "text-green-500 font-semibold",
        },
        "important": {
            "icon": "mynaui:bookmark",
            "title": "Important",
            "border_color": "border-l-4 border-l-purple-500",
            "icon_color": "text-purple-500",
            "title_color": "text-purple-500 font-semibold",
        },
        "warning": {
            "icon": "mynaui:danger-diamond",
            "title": "Warning",
            "border_color": "border-l-4 border-l-amber-500",
            "icon_color": "text-amber-600",
            "title_color": "text-amber-600 font-semibold",
        },
        "caution": {
            "icon": "mynaui:danger-hexagon",
            "title": "Caution",
            "border_color": "border-l-4 border-l-red-500",
            "icon_color": "text-red-500",
            "title_color": "text-red-500 font-semibold",
        },
    }

    config = variant_config[variant]

    # Base callout styling - exactly matching reference image (no background, just left border)
    base_classes = f"pl-4 py-1 {config['border_color']}"
    combined_classes = f"{base_classes} {className}".strip()

    return html.Div(
        [
            # Header with icon and title on same line
            html.Div(
                [
                    DashIconify(
                        icon=config["icon"],
                        className=f"{config['icon_color']} mr-2",
                        width=18,
                        height=18,
                        style={"strokeWidth": 3},
                    ),
                    html.Span(config["title"], className=config["title_color"]),
                ],
                className="flex items-center mb-3",
            ),
            # Content with proper text styling
            html.Div(
                children, className="text-gray-700 dark:text-gray-300 leading-relaxed"
            ),
        ],
        className=combined_classes,
        **kwargs,
    )


def NoteCallout(children: Any, className: str = "", **kwargs: Any) -> html.Div:
    """Note callout - useful information that users should know."""
    return Callout(children, variant="note", className=className, **kwargs)


def TipCallout(children: Any, className: str = "", **kwargs: Any) -> html.Div:
    """Tip callout - helpful advice for doing things better or more easily."""
    return Callout(children, variant="tip", className=className, **kwargs)


def ImportantCallout(children: Any, className: str = "", **kwargs: Any) -> html.Div:
    """Important callout - key information users need to know to achieve their goal."""
    return Callout(children, variant="important", className=className, **kwargs)


def WarningCallout(children: Any, className: str = "", **kwargs: Any) -> html.Div:
    """Warning callout - urgent info that needs immediate user attention to avoid problems."""
    return Callout(children, variant="warning", className=className, **kwargs)


def CautionCallout(children: Any, className: str = "", **kwargs: Any) -> html.Div:
    """Caution callout - advises about risks or negative outcomes of certain actions."""
    return Callout(children, variant="caution", className=className, **kwargs)
