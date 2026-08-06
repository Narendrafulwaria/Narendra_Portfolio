# components/timeline.py — Vertical timeline for experience and education
import streamlit as st


def render_timeline(items: list, item_type: str = "experience"):
    """
    Renders a vertical timeline.

    Args:
        items     : List of dicts from utils/data.py
                    Experience: {role, company, period, bullets}
                    Education:  {degree, institution, year}
        item_type : "experience" | "education"
    """
    if not items:
        st.info("No items to display.")
        return

    items_html = "".join(
        _experience_item(item) if item_type == "experience"
        else _education_item(item)
        for item in items
    )

    timeline_html = f"""
    <div class="timeline-container">
        {items_html}
    </div>
    """
    st.markdown(timeline_html, unsafe_allow_html=True)


# ---------------------------------------------------------------------------
# Item builders
# ---------------------------------------------------------------------------

def _experience_item(item: dict) -> str:
    role    = _e(item.get("role", ""))
    company = _e(item.get("company", ""))
    period  = _e(item.get("period", ""))
    bullets = item.get("bullets", [])

    bullets_html = "".join(
        f"<li>{_e(b)}</li>" for b in bullets
    )
    bullets_block = (
        f'<ul class="timeline-bullets">{bullets_html}</ul>'
        if bullets else ""
    )

    return f"""
    <div class="timeline-item">
        <div class="timeline-dot"></div>
        <div class="timeline-role">{role}</div>
        <div class="timeline-company">{company}</div>
        <span class="timeline-period">📅 {period}</span>
        {bullets_block}
    </div>
    """


def _education_item(item: dict) -> str:
    degree      = _e(item.get("degree", ""))
    institution = _e(item.get("institution", ""))
    year        = _e(item.get("year", ""))

    return f"""
    <div class="timeline-item">
        <div class="timeline-dot"></div>
        <div class="timeline-role">{degree}</div>
        <div class="timeline-company">{institution}</div>
        <span class="timeline-period">🎓 {year}</span>
    </div>
    """


def _e(text: str) -> str:
    """Minimal HTML escape."""
    return (
        str(text)
        .replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
        .replace('"', "&quot;")
    )
