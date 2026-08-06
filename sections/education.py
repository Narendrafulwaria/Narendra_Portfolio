# sections/education.py — Section 6: Education
import streamlit as st
from components.timeline import render_timeline
from utils.data import EDUCATION


def render_education():
    st.markdown('<div id="education"></div>', unsafe_allow_html=True)
    st.markdown('<div class="section-heading">Education</div>', unsafe_allow_html=True)

    render_timeline(EDUCATION, item_type="education")

    st.markdown("<hr style='border-color:#1E293B;margin:2rem 0;'>", unsafe_allow_html=True)
