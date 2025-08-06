from typing import Any

from dash import html, clientside_callback, Input, Output

from .logo import LogoSection
from .navigation import SidebarNavigation


def _register_section_callback(section_id: str):
    """Register a clientside callback for section toggle functionality."""
    toggle_id = f"{section_id}-toggle"
    content_id = f"{section_id}-content"
    chevron_id = f"{section_id}-chevron"
    
    try:
        clientside_callback(
            """
            function(n_clicks) {
                if (!n_clicks) return window.dash_clientside.no_update;
                
                const content = document.getElementById('""" + content_id + """');
                const chevron = document.getElementById('""" + chevron_id + """');
                
                if (content && chevron) {
                    const isHidden = content.classList.contains('hidden');
                    
                    if (isHidden) {
                        content.classList.remove('hidden');
                        content.classList.add('block');
                        chevron.className = chevron.className.replace('fa-chevron-right', 'fa-chevron-down');
                    } else {
                        content.classList.remove('block');
                        content.classList.add('hidden');
                        chevron.className = chevron.className.replace('fa-chevron-down', 'fa-chevron-right');
                    }
                }
                
                return window.dash_clientside.no_update;
            }
            """,
            Output(toggle_id, "n_clicks", allow_duplicate=True),
            Input(toggle_id, "n_clicks"),
            prevent_initial_call=True
        )
    except Exception:
        # Callback might already be registered, skip silently
        pass


def create_sidebar(
    brand_name: str,
    brand_initial: str,
    nav_items: list[dict[str, Any]],
    sections: list[dict[str, Any]],
) -> html.Div:
    """Create a reusable sidebar component.

    Args:
        brand_name: The brand/company name for the logo
        brand_initial: Initial letter for the logo
        nav_items: List of navigation items with icon, label, and optional active state
        sections: List of sections with title and items
    """
    # Create navigation instance
    nav = SidebarNavigation()

    # Convert nav_items config to actual nav items
    rendered_nav_items = []
    for item in nav_items:
        rendered_nav_items.append(
            nav.create_nav_item(
                item["icon"], item["label"], active=item.get("active", False)
            )
        )

    # Convert sections config to actual sections
    rendered_sections = []
    for section in sections:
        section_items = []
        section_id = f"sidebar-section-{section['title'].lower().replace(' ', '-')}"
        
        for item in section["items"]:
            if isinstance(item, str):
                # Plain text item
                section_items.append(item)
            elif item.get("type") == "nav_item":
                # Navigation item
                section_items.append(
                    html.Li(
                        nav.create_nav_item(
                            item["icon"],
                            item["label"],
                            active=item.get("active", False),
                        )
                    )
                )
            elif item.get("type") == "button":
                # Button item
                section_items.append(
                    html.Button(
                        [html.I(className=f"{item['icon']} mr-2"), item["label"]],
                        className="text-sm text-blue-600 hover:text-blue-700 px-3 py-2 w-full text-left",
                    )
                )

        rendered_sections.append(
            nav.create_section(
                section["title"], 
                section_items, 
                expanded=section.get("expanded", False),
                section_id=section_id
            )
        )
        
        # Register clientside callback for this section
        _register_section_callback(section_id)

    return html.Div(
        [
            # Logo section
            LogoSection(brand_name, brand_initial),
            # Navigation
            nav.render(rendered_nav_items, rendered_sections),
        ],
        className="bg-[#FBFBFB] dark:bg-[#16181C] w-64 h-screen border-r border-[#EEEFF1] dark:border-[#27282B] flex flex-col shrink-0",
    )
