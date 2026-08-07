# sections/skills.py — Section 3: Technical Skills
import streamlit as st
from components.skill_chart import render_skill_chart
from utils.data import SKILLS
from utils.styles import section_start, section_end

_BADGE_COLORS = [
    ("#EFF6FF", "#1D4ED8", "#BFDBFE"),
    ("#DBEAFE", "#1E40AF", "#93C5FD"),
    ("#E0F2FE", "#0369A1", "#7DD3FC"),
    ("#F0F9FF", "#0C4A6E", "#BAE6FD"),
    ("#EFF6FF", "#2563EB", "#BFDBFE"),
]


def render_skills():
    st.markdown('<div id="skills"></div>', unsafe_allow_html=True)
    section_start("light")
    st.markdown('<div class="section-heading">Technical Skills</div>', unsafe_allow_html=True)

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

    st.markdown(
        '<p style="color:#64748B;font-size:0.82rem;margin-bottom:0.5rem;">'
        'Proficiency levels are self-assessed estimates.</p>',
        unsafe_allow_html=True,
    )
    render_skill_chart()

    section_end()
    st.markdown("<hr style='border-color:#E2E8F0;margin:2rem 0;'>", unsafe_allow_html=True)
