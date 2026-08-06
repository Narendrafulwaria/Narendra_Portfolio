# sections/projects.py — Section 4: Projects
import streamlit as st
from components.card import render_card
from utils.data import PROJECTS


def render_projects():
    st.markdown('<div id="projects"></div>', unsafe_allow_html=True)
    st.markdown('<div class="section-heading">Projects</div>', unsafe_allow_html=True)

    # ── 3-column responsive grid ───────────────────────────────────────
    cols_per_row = 3
    rows = [PROJECTS[i:i + cols_per_row] for i in range(0, len(PROJECTS), cols_per_row)]

    for row in rows:
        cols = st.columns(len(row), gap="medium")
        for col, project in zip(cols, row):
            with col:
                render_card(
                    title=project["title"],
                    description=project["description"],
                    tags=project.get("tech", []),
                    link=project.get("url"),
                    link_label="🔗 View on GitHub →",
                )

    st.markdown("<hr style='border-color:#1E293B;margin:2rem 0;'>", unsafe_allow_html=True)
