from typing import Any

from dash import dcc, html

from .buttons import PrimaryButton, SecondaryButton
from .logo import BrandHeader
from .navigation import FilterBar, TopNavigationBar


def create_header(
    page_title: str,
    page_icon: str,
    search_placeholder: str = "Search...",
    actions: list[dict[str, Any]] | None = None,
    filter_items: list[dict[str, Any]] | None = None,
) -> html.Div:
    """Create a reusable header with two-tier structure.

    Args:
        page_title: Title for the current page
        page_icon: Icon for the current page (emoji or font-awesome class)
        search_placeholder: Placeholder text for search input
        actions: List of action buttons with type, label, and optional styling
        filter_items: List of filter items with labels and optional active state
    """
    # Create navigation instances
    top_nav = TopNavigationBar()
    filter_bar = FilterBar()

    # Top tier content
    left_content = BrandHeader(page_title, page_icon)

    center_content = None
    # html.Div(
    #     [
    #         html.I(
    #             className="fas fa-search absolute left-3 top-1/2 transform -translate-y-1/2 text-gray-400"
    #         ),
    #         dcc.Input(
    #             placeholder=search_placeholder,
    #             className="pl-10 pr-2 py-1 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent w-64",
    #         ),
    #     ],
    #     className="relative",
    # )

    # Build right content from actions
    right_content = []
    if actions:
        for action in actions:
            if action["type"] == "primary":
                right_content.append(
                    PrimaryButton(
                        action["label"],
                        icon=action.get("icon"),
                        className=action.get("className", ""),
                    )
                )
            elif action["type"] == "secondary":
                right_content.append(
                    SecondaryButton(
                        action["label"],
                        icon=action.get("icon"),
                        dropdown=action.get("dropdown", False),
                        className=action.get("className", ""),
                    )
                )

    # Build filter content from filter_items
    filter_content = []
    if filter_items:
        for item in filter_items:
            filter_content.append(
                SecondaryButton(
                    item["label"],
                    icon=item.get("icon"),
                    dropdown=item.get("dropdown", False),
                    className=item.get("className", ""),
                )
            )

    return html.Div(
        [
            # Top tier
            top_nav.render(left_content, center_content, right_content),
            # Bottom tier (only render if filter_items provided)
            filter_bar.render(filter_content) if filter_items else None,
        ]
    )
