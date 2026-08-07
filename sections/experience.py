# sections/experience.py — Section 5: Professional Experience
import streamlit as st
from components.timeline import render_timeline
from utils.data import EXPERIENCE
from utils.styles import section_start, section_end


def render_experience():
    st.markdown('<div id="experience"></div>', unsafe_allow_html=True)
    section_start("light")
    st.markdown(
        '<div class="section-heading">Professional Experience</div>',
        unsafe_allow_html=True,
    )

    render_timeline(EXPERIENCE, item_type="experience")

    section_end()
    st.markdown("<hr style='border-color:#E2E8F0;margin:2rem 0;'>", unsafe_allow_html=True)
