# sections/achievements.py — Section 8: Key Achievements
import streamlit as st
from utils.data import ACHIEVEMENTS


def render_achievements():
    st.markdown('<div id="achievements"></div>', unsafe_allow_html=True)
    st.markdown('<div class="section-heading">Key Achievements</div>', unsafe_allow_html=True)

    cols = st.columns(len(ACHIEVEMENTS), gap="medium")

    for col, achievement in zip(cols, ACHIEVEMENTS):
        with col:
            icon   = achievement.get("icon",   "🏆")
            value  = achievement.get("value",  "")
            label  = achievement.get("label",  "")
            detail = achievement.get("detail", "")

            st.markdown(
                f"""
                <div class="achievement-card">
                    <div class="achievement-icon">{icon}</div>
                    <div class="achievement-value">{value}</div>
                    <div class="achievement-label">{label}</div>
                    <div class="achievement-detail">{detail}</div>
                </div>
                """,
                unsafe_allow_html=True,
            )

    st.markdown("<hr style='border-color:#1E293B;margin:2rem 0;'>", unsafe_allow_html=True)
