# sections/skills.py — Section 3: Technical Skills
import streamlit as st
from components.skill_chart import render_skill_chart
from utils.data import SKILLS

# One colour per skill category (cycles if more categories added)
_BADGE_COLORS = [
    ("rgba(37,99,235,0.15)",  "#93C5FD", "rgba(37,99,235,0.35)"),   # blue
    ("rgba(16,185,129,0.15)", "#6EE7B7", "rgba(16,185,129,0.35)"),  # green
    ("rgba(139,92,246,0.15)", "#C4B5FD", "rgba(139,92,246,0.35)"),  # purple
    ("rgba(245,158,11,0.15)", "#FCD34D", "rgba(245,158,11,0.35)"),  # yellow
    ("rgba(236,72,153,0.15)", "#F9A8D4", "rgba(236,72,153,0.35)"),  # pink
]


def render_skills():
    st.markdown('<div id="skills"></div>', unsafe_allow_html=True)
    st.markdown('<div class="section-heading">Technical Skills</div>', unsafe_allow_html=True)

    # ── Badge grid ─────────────────────────────────────────────────────
    for idx, (category, skill_list) in enumerate(SKILLS.items()):
        bg, color, border = _BADGE_COLORS[idx % len(_BADGE_COLORS)]

        badges_html = "".join(
            f'<span style="display:inline-block;padding:0.28rem 0.7rem;'
            f'background:{bg};border:1px solid {border};border-radius:999px;'
            f'color:{color};font-size:0.78rem;font-weight:600;'
            f'margin-right:0.4rem;margin-bottom:0.4rem;">{skill}</span>'
            for skill in skill_list
        )

        st.markdown(
            f'<div style="margin-bottom:0.75rem;">'
            f'  <div class="skill-category">{category}</div>'
            f'  <div class="badge-container">{badges_html}</div>'
            f'</div>',
            unsafe_allow_html=True,
        )

    st.markdown("<br>", unsafe_allow_html=True)

    # ── Skill chart (progress bars / radar) ───────────────────────────
    st.markdown(
        '<p style="color:#64748B;font-size:0.82rem;margin-bottom:0.5rem;">'
        'Proficiency levels are self-assessed estimates.</p>',
        unsafe_allow_html=True,
    )
    render_skill_chart()

    st.markdown("<hr style='border-color:#1E293B;margin:2rem 0;'>", unsafe_allow_html=True)
