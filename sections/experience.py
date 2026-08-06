# sections/experience.py — Section 5: Professional Experience
import streamlit as st
from components.timeline import render_timeline
from utils.data import EXPERIENCE


def render_experience():
    st.markdown('<div id="experience"></div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="section-heading">Professional Experience</div>',
        unsafe_allow_html=True,
    )

    render_timeline(EXPERIENCE, item_type="experience")

    st.markdown("<hr style='border-color:#1E293B;margin:2rem 0;'>", unsafe_allow_html=True)
