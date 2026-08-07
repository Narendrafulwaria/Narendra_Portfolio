# sections/linkedin.py — Section 10: LinkedIn CTA
import streamlit as st
from utils.data import PERSONAL_INFO
from utils.styles import section_start, section_end


def render_linkedin():
    st.markdown('<div id="linkedin"></div>', unsafe_allow_html=True)
    section_start("blue")
    st.markdown('<div class="section-heading">Let\'s Connect</div>', unsafe_allow_html=True)

    st.markdown(
        """
        <div style="text-align:center;padding:2rem 0;">
            <div style="font-size:3rem;margin-bottom:1rem;">💼</div>
            <p style="color:#475569;font-size:1.1rem;margin-bottom:1.5rem;">
                Let's connect professionally
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    linkedin_url = PERSONAL_INFO.get("linkedin_url", "")

    st.markdown(
        f"""
        <div style="text-align:center;">
            <a href="{linkedin_url}" target="_blank" rel="noopener noreferrer"
               style="display:inline-block;padding:0.8rem 2rem;background:#0077B5;color:white;
                      text-decoration:none;border-radius:8px;font-weight:600;font-size:1rem;
                      transition:transform 0.2s ease,box-shadow 0.2s ease;">
               Connect on LinkedIn →
            </a>
        </div>
        """,
        unsafe_allow_html=True,
    )

    section_end()
    st.markdown("<hr style='border-color:#E2E8F0;margin:2rem 0;'>", unsafe_allow_html=True)
