# components/card.py — Reusable card renderer for project and blog cards
import streamlit as st


def render_card(
    title: str,
    description: str,
    tags: list = None,
    link: str = None,
    link_label: str = "View →",
    date: str = None,
):
    """
    Renders a styled portfolio card via st.markdown HTML.

    Args:
        title       : Card heading
        description : Body text
        tags        : List of tech/badge strings
        link        : URL for the action button (optional)
        link_label  : Label for the link button (default "View →")
        date        : Optional date string shown in muted text (for blog cards)
    """
    if tags is None:
        tags = []

    # Build badge HTML
    badges_html = ""
    if tags:
        badge_items = "".join(
            f'<span class="badge">{_escape(tag)}</span>' for tag in tags
        )
        badges_html = f'<div class="badge-container">{badge_items}</div>'

    # Build date HTML
    date_html = (
        f'<div class="card-date">📅 {_escape(date)}</div>' if date else ""
    )

    # Build link HTML
    link_html = ""
    if link:
        link_html = (
            f'<a class="card-link" href="{link}" target="_blank" '
            f'rel="noopener noreferrer">{_escape(link_label)}</a>'
        )

    card_html = f"""
    <div class="portfolio-card">
        <div class="card-title">{_escape(title)}</div>
        {date_html}
        <div class="card-description">{_escape(description)}</div>
        {badges_html}
        {link_html}
    </div>
    """

    st.markdown(card_html, unsafe_allow_html=True)


def render_card_row(cards: list[dict], columns: int = 3):
    """
    Renders a responsive grid of cards.

    Args:
        cards   : List of dicts, each matching render_card() kwargs
        columns : Number of columns (default 3)
    """
    cols = st.columns(columns)
    for idx, card_data in enumerate(cards):
        with cols[idx % columns]:
            render_card(**card_data)


# ---------------------------------------------------------------------------
# Helper
# ---------------------------------------------------------------------------

def _escape(text: str) -> str:
    """Minimal HTML escaping to prevent injection."""
    return (
        str(text)
        .replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
        .replace('"', "&quot;")
    )
