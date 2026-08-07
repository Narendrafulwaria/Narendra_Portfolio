# sections/about.py — Section 2: About Me
import os
import json
import streamlit as st
from components.three_d_photo import render_3d_photo
from utils.data import PERSONAL_INFO
from utils.styles import section_start, section_end


def render_about():
    st.markdown('<div id="about"></div>', unsafe_allow_html=True)
    section_start("blue")
    st.markdown('<div class="section-heading">About Me</div>', unsafe_allow_html=True)

    left, right = st.columns([0.75, 1.25], gap="large")

    with left:
        render_3d_photo(height=300)

    with right:
        # ── Bio paragraph ──────────────────────────────────────────────
        st.markdown(
            f'<p style="color:#475569;font-size:0.95rem;line-height:1.8;margin-bottom:1.25rem;">'
            f'{PERSONAL_INFO["bio"]}</p>',
            unsafe_allow_html=True,
        )

        # ── Trait pills ────────────────────────────────────────────────
        traits_html = "".join(
            f'<span style="'
            f'display:inline-block;padding:0.35rem 0.9rem;'
            f'background:#EFF6FF;border:1px solid #BFDBFE;'
            f'border-radius:999px;color:#1D4ED8;font-size:0.85rem;font-weight:600;'
            f'margin-right:0.5rem;margin-bottom:0.5rem;">'
            f'{trait}</span>'
            for trait in PERSONAL_INFO.get("traits", [])
        )
        st.markdown(
            f'<div style="margin-bottom:1.25rem;">{traits_html}</div>',
            unsafe_allow_html=True,
        )

        # ── Quick stats row ────────────────────────────────────────────
        st.markdown(
            """
            <div style="display:flex;gap:1.5rem;flex-wrap:wrap;margin-top:0.5rem;">
                <div style="text-align:center;">
                    <div style="font-size:1.5rem;font-weight:800;color:#2563EB;">6+</div>
                    <div style="font-size:0.75rem;color:#64748B;">Years Experience</div>
                </div>
                <div style="text-align:center;">
                    <div style="font-size:1.5rem;font-weight:800;color:#2563EB;">5+</div>
                    <div style="font-size:0.75rem;color:#64748B;">AI Projects</div>
                </div>
                <div style="text-align:center;">
                    <div style="font-size:1.5rem;font-weight:800;color:#2563EB;">7</div>
                    <div style="font-size:0.75rem;color:#64748B;">Certifications</div>
                </div>
                <div style="text-align:center;">
                    <div style="font-size:1.5rem;font-weight:800;color:#2563EB;">75%</div>
                    <div style="font-size:0.75rem;color:#64748B;">Sales Growth</div>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

        resume_path = "assets/resume.pdf"
        if os.path.exists(resume_path):
            with open(resume_path, "rb") as f:
                st.download_button(
                    label="📄 Download Resume",
                    data=f.read(),
                    file_name="Narendra_Fulwaria_Updated_Resume_v2.pdf",
                    mime="application/pdf",
                    key="about_resume",
                    width="stretch",
                )
        else:
            st.button(
                "📄 Resume (soon)",
                disabled=True,
                width="stretch",
                key="about_resume_placeholder",
            )

        # ── Lottie animation (optional) ────────────────────────────────
        _try_lottie("assets/lottie/coding_animation.json")

    section_end()
    st.markdown("<hr style='border-color:#E2E8F0;margin:2rem 0;'>", unsafe_allow_html=True)


def _try_lottie(path: str):
    """Render a Lottie animation if the file exists and streamlit-lottie is available."""
    if not os.path.exists(path):
        return
    try:
        from streamlit_lottie import st_lottie
        with open(path) as f:
            anim = json.load(f)
        st_lottie(anim, height=120, key="about_lottie", speed=0.8)
    except Exception:
        pass  # silently skip if file missing or package unavailable
