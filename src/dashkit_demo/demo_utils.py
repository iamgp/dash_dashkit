"""Demo-specific utility functions for the Dashkit components showcase."""

from typing import Any


def create_company_columns() -> list[dict[str, Any]]:
    """Create column configuration for the companies table matching Dashkit style."""
    return [
        {
            "data": "company_name",
            "title": "Company",
            "type": "text",
            "className": "dashkit-cell dashkit-primary-cell",
            "width": 200,
        },
        {
            "data": "categories",
            "title": "Categories",
            "type": "text",
            "className": "dashkit-cell dashkit-categories-cell",
            "width": 300,
        },
        {
            "data": "linkedin",
            "title": "LinkedIn",
            "type": "text",
            "className": "dashkit-cell dashkit-link-cell",
            "width": 120,
        },
        {
            "data": "last_interaction",
            "title": "Last interaction",
            "type": "text",
            "className": "dashkit-cell dashkit-center-cell",
            "width": 150,
        },
        {
            "data": "connection_strength",
            "title": "Connection strength",
            "type": "text",
            "className": "dashkit-cell dashkit-center-cell",
            "width": 150,
        },
        {
            "data": "twitter_followers",
            "title": "Twitter followers",
            "type": "numeric",
            "className": "dashkit-cell dashkit-right-cell",
            "width": 150,
        },
        {
            "data": "twitter_handle",
            "title": "Twitter",
            "type": "text",
            "className": "dashkit-cell dashkit-link-cell",
            "width": 120,
        },
    ]


def format_company_data(companies: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """Format company data for Handsontable with proper string representations."""
    formatted_data = []

    for company in companies:
        # Format company name with icon as string for Handsontable
        company_name = f"{company.get('icon', '')} {company.get('name', '')}"

        # Format categories as comma-separated string (we'll style with CSS)
        categories = company.get("categories", [])
        if categories and isinstance(categories[0], dict):
            category_names = [cat["name"] for cat in categories]
            categories_str = ", ".join(category_names)
        else:
            categories_str = ", ".join(categories)

        # LinkedIn and Twitter as simple strings
        linkedin = company.get("linkedin", "No contact")
        twitter_handle = company.get("twitter_handle", "")

        formatted_data.append(
            {
                "company_name": company_name,
                "categories": categories_str,
                "linkedin": linkedin,
                "last_interaction": company.get("last_interaction", "No communication"),
                "connection_strength": company.get("connection_strength", ""),
                "twitter_followers": company.get("twitter_followers", 0),
                "twitter_handle": twitter_handle,
            }
        )

    return formatted_data
