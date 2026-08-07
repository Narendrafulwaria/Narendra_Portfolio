# sections/education.py — Section 6: Education
import streamlit as st
from components.timeline import render_timeline
from utils.data import EDUCATION
from utils.styles import section_start, section_end


def render_education():
    st.markdown('<div id="education"></div>', unsafe_allow_html=True)
    section_start("blue")
    st.markdown('<div class="section-heading">Education</div>', unsafe_allow_html=True)

    render_timeline(EDUCATION, item_type="education")

    section_end()
    st.markdown("<hr style='border-color:#E2E8F0;margin:2rem 0;'>", unsafe_allow_html=True)
