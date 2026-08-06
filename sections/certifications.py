# sections/certifications.py — Section 7: Certifications
import streamlit as st
from utils.data import CERTIFICATIONS


def render_certifications():
    st.markdown('<div id="certifications"></div>', unsafe_allow_html=True)
    st.markdown('<div class="section-heading">Certifications</div>', unsafe_allow_html=True)

    left, right = st.columns(2, gap="medium")
    half = (len(CERTIFICATIONS) + 1) // 2

    for col, chunk in zip([left, right], [CERTIFICATIONS[:half], CERTIFICATIONS[half:]]):
        with col:
            for cert in chunk:
                _render_cert_card(cert)

    st.markdown("<hr style='border-color:#1E293B;margin:2rem 0;'>", unsafe_allow_html=True)


def _render_cert_card(cert: dict):
    status       = cert.get("status", "Completed")
    is_progress  = status == "In Progress"
    badge_bg     = "rgba(245,158,11,0.15)" if is_progress else "rgba(16,185,129,0.15)"
    badge_color  = "#FCD34D"              if is_progress else "#6EE7B7"
    badge_border = "rgba(245,158,11,0.4)" if is_progress else "rgba(16,185,129,0.4)"

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
