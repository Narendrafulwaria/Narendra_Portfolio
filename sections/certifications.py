# sections/certifications.py — Section 7: Certifications
import streamlit as st
from utils.data import CERTIFICATIONS
from utils.styles import section_start, section_end


def render_certifications():
    st.markdown('<div id="certifications"></div>', unsafe_allow_html=True)
    section_start("light")
    st.markdown('<div class="section-heading">Certifications</div>', unsafe_allow_html=True)

    cols_per_row = 3
    rows = [CERTIFICATIONS[i:i + cols_per_row] for i in range(0, len(CERTIFICATIONS), cols_per_row)]

    for row in rows:
        cols = st.columns(len(row), gap="medium")
        for col, cert in zip(cols, row):
            with col:
                _render_cert_card(cert)

    section_end()
    st.markdown("<hr style='border-color:#E2E8F0;margin:2rem 0;'>", unsafe_allow_html=True)


def _render_cert_card(cert: dict):
    status       = cert.get("status", "Completed")
    is_progress  = status == "In Progress"
    badge_bg     = "#FEF3C7" if is_progress else "#DCFCE7"
    badge_color  = "#B45309" if is_progress else "#166534"
    badge_border = "#FCD34D" if is_progress else "#86EFAC"

    name   = cert.get("name", "").replace("&", "&amp;").replace("<", "&lt;")
    issuer = cert.get("issuer", "").replace("&", "&amp;").replace("<", "&lt;")

    st.markdown(
        f"""
        <div class="cert-card">
            <div class="cert-icon">🏅</div>
            <div>
                <div class="cert-name">{name}</div>
                <div class="cert-issuer">{issuer}</div>
                <span style="
                    display:inline-block;margin-top:0.4rem;
                    padding:0.18rem 0.55rem;border-radius:999px;font-size:0.72rem;
                    font-weight:600;background:{badge_bg};
                    color:{badge_color};border:1px solid {badge_border};">
                    {"⏳ " if is_progress else "✅ "}{status}
                </span>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )
