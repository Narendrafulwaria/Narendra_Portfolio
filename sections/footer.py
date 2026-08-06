# sections/footer.py — Section 15: Footer
import streamlit as st
from utils.data import PERSONAL_INFO


def render_footer():
    st.markdown("<hr style='border-color:#1E293B;margin:2rem 0;'>", unsafe_allow_html=True)

    st.markdown(
        """
        <div style="text-align:center;padding:2rem 0;">
            <p style="color:#64748B;font-size:0.9rem;margin-bottom:1rem;">
                © 2025 Narendra Madanlal Fulwaria. All rights reserved.
            </p>
        """,
        unsafe_allow_html=True,
    )

    # Quick nav links
    st.markdown(
        """
        <div style="display:flex;justify-content:center;gap:1.5rem;margin-bottom:1rem;flex-wrap:wrap;">
            <a href="#home" style="color:#94A3B8;font-size:0.85rem;text-decoration:none;">Home</a>
            <a href="#about" style="color:#94A3B8;font-size:0.85rem;text-decoration:none;">About</a>
            <a href="#projects" style="color:#94A3B8;font-size:0.85rem;text-decoration:none;">Projects</a>
            <a href="#contact" style="color:#94A3B8;font-size:0.85rem;text-decoration:none;">Contact</a>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # Social icons
    st.markdown(
        f"""
        <div style="display:flex;justify-content:center;gap:1.5rem;margin-bottom:1rem;">
            <a href="{PERSONAL_INFO.get('github_url', '')}" target="_blank"
               style="color:#94A3B8;font-size:1.2rem;text-decoration:none;">
               🐙
            </a>
            <a href="{PERSONAL_INFO.get('linkedin_url', '')}" target="_blank"
               style="color:#94A3B8;font-size:1.2rem;text-decoration:none;">
               💼
            </a>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # Built-with note
    st.markdown(
        """
        <p style="color:#475569;font-size:0.8rem;">
            Built with Python & Streamlit
        </p>
        """,
        unsafe_allow_html=True,
    )
