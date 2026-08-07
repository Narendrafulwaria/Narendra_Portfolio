# sections/hero.py — Section 1: Hero / Landing
import os
import streamlit as st
from components.three_d_photo import render_3d_photo
from utils.data import PERSONAL_INFO


def render_hero():
    st.markdown('<div id="home"></div>', unsafe_allow_html=True)

    left, right = st.columns([1.45, 0.55], gap="large")

    with left:
        # ── Gradient name ──────────────────────────────────────────────
        st.markdown(
            f'<h1 class="gradient-text">{PERSONAL_INFO["name"]}</h1>',
            unsafe_allow_html=True,
        )

        # ── Animated typewriter tagline ────────────────────────────────
        st.markdown(
            """
            <style>
            .typewriter-wrap {
                font-size: 1.15rem;
                color: #475569;
                font-weight: 500;
                margin: 0.5rem 0 0.75rem;
                min-height: 1.8rem;
            }
            .typewriter {
                border-right: 2px solid #2563EB;
                white-space: nowrap;
                overflow: hidden;
                animation: typing 3.5s steps(45,end) forwards,
                           blink 0.75s step-end infinite;
            }
            @keyframes typing {
                from { width: 0 }
                to   { width: 100% }
            }
            @keyframes blink {
                50% { border-color: transparent }
            }
            </style>
            <div class="typewriter-wrap">
                <span class="typewriter">Data Analyst &nbsp;|&nbsp; AI Automation &nbsp;|&nbsp; Business Analytics</span>
            </div>
            """,
            unsafe_allow_html=True,
        )

        # ── Location badge ─────────────────────────────────────────────
        st.markdown(
            f'<p style="color:#64748B;font-size:0.9rem;margin-bottom:1.5rem;">'
            f'📍 {PERSONAL_INFO["location"]}</p>',
            unsafe_allow_html=True,
        )

        # ── Download Resume ────────────────────────────────────────────
        resume_path = "assets/resume.pdf"
        if os.path.exists(resume_path):
            with open(resume_path, "rb") as f:
                st.download_button(
                    label="📄 Download Resume",
                    data=f.read(),
                    file_name="Narendra_Fulwaria_Updated_Resume_v2.pdf",
                    mime="application/pdf",
                    key="hero_resume",
                    width="stretch",
                )
        else:
            st.button(
                "📄 Resume (soon)",
                disabled=True,
                width="stretch",
                key="hero_resume_placeholder",
            )

        # ── Social quick links ─────────────────────────────────────────
        st.markdown(
            f"""
            <div style="margin-top:1.25rem;display:flex;gap:1rem;">
                <a href="{PERSONAL_INFO['github_url']}" target="_blank"
                   style="color:#2563EB;font-size:0.88rem;text-decoration:none;">
                   🐙 GitHub
                </a>
                <a href="{PERSONAL_INFO['linkedin_url']}" target="_blank"
                   style="color:#2563EB;font-size:0.88rem;text-decoration:none;">
                   💼 LinkedIn
                </a>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with right:
        render_3d_photo(height=360)

    st.markdown("<hr style='border-color:#E2E8F0;margin:2rem 0;'>", unsafe_allow_html=True)
