# sections/blog.py — Section 11: Blog / Insights
import streamlit as st
from components.card import render_card
from utils.data import BLOG_POSTS


def render_blog():
    st.markdown('<div id="blog"></div>', unsafe_allow_html=True)
    st.markdown('<div class="section-heading">Blog & Insights</div>', unsafe_allow_html=True)

    # ── Blog cards grid ───────────────────────────────────────────────────
    cols_per_row = 3
    rows = [BLOG_POSTS[i:i + cols_per_row] for i in range(0, len(BLOG_POSTS), cols_per_row)]

    for row in rows:
        cols = st.columns(len(row), gap="medium")
        for col, post in zip(cols, row):
            with col:
                render_card(
                    title=post["title"],
                    description=post["excerpt"],
                    link=post.get("url"),
                    link_label="Read More →",
                    date=post.get("date"),
                )

    # ── Note at bottom ────────────────────────────────────────────────────
    st.markdown(
        """
        <p style="color:#64748B;font-size:0.85rem;margin-top:1rem;text-align:center;">
            More articles coming soon — follow on LinkedIn
        </p>
        """,
        unsafe_allow_html=True,
    )

    st.markdown("<hr style='border-color:#1E293B;margin:2rem 0;'>", unsafe_allow_html=True)
