# sections/contact.py — Section 14: Contact Form
import os
import json
import streamlit as st
from utils.data import PERSONAL_INFO


def render_contact():
    st.markdown('<div id="contact"></div>', unsafe_allow_html=True)
    st.markdown('<div class="section-heading">Contact Me</div>', unsafe_allow_html=True)

    left, right = st.columns([1, 1], gap="large")

    with left:
        # ── Contact details ───────────────────────────────────────────────
        st.markdown(
            """
            <div style="margin-bottom:1.5rem;">
                <p style="color:#94A3B8;font-size:0.95rem;margin-bottom:0.75rem;">
                    Feel free to reach out for collaborations, opportunities, or just to say hello!
                </p>
            </div>
            """,
            unsafe_allow_html=True,
        )

        st.markdown(
            f"""
            <div style="display:flex;flex-direction:column;gap:0.75rem;">
                <div style="display:flex;align-items:center;gap:0.75rem;">
                    <span style="font-size:1.2rem;">📍</span>
                    <span style="color:#CBD5E1;font-size:0.95rem;">{PERSONAL_INFO.get("location", "")}</span>
                </div>
                <div style="display:flex;align-items:center;gap:0.75rem;">
                    <span style="font-size:1.2rem;">📞</span>
                    <span style="color:#CBD5E1;font-size:0.95rem;">{PERSONAL_INFO.get("phone", "")}</span>
                </div>
                <div style="display:flex;align-items:center;gap:0.75rem;">
                    <span style="font-size:1.2rem;">📧</span>
                    <span style="color:#CBD5E1;font-size:0.95rem;">{PERSONAL_INFO.get("email", "")}</span>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

        st.markdown("<br>", unsafe_allow_html=True)

        # Social links
        st.markdown(
            f"""
            <div style="display:flex;gap:1rem;">
                <a href="{PERSONAL_INFO.get('github_url', '')}" target="_blank"
                   style="color:#94A3B8;font-size:0.9rem;text-decoration:none;">
                   🐙 GitHub
                </a>
                <a href="{PERSONAL_INFO.get('linkedin_url', '')}" target="_blank"
                   style="color:#94A3B8;font-size:0.9rem;text-decoration:none;">
                   💼 LinkedIn
                </a>
            </div>
            """,
            unsafe_allow_html=True,
        )

        # ── Lottie animation (optional) ───────────────────────────────────
        _try_lottie("assets/lottie/contact_animation.json")

    with right:
        # ── Contact form ───────────────────────────────────────────────────
        with st.form("contact_form", clear_on_submit=True):
            name = st.text_input("Your Name", key="contact_name")
            email = st.text_input("Your Email", key="contact_email")
            message = st.text_area("Message", height=150, key="contact_message")

            submitted = st.form_submit_button("Send Message", use_container_width=True)

            if submitted:
                # Basic validation
                if not name.strip() or not email.strip() or not message.strip():
                    st.error("Please fill in all fields.")
                elif "@" not in email or "." not in email:
                    st.error("Please enter a valid email address.")
                else:
                    # Construct mailto link
                    subject = f"Portfolio Contact from {name}"
                    body = f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}"
                    mailto_link = f"mailto:{PERSONAL_INFO.get('email', '')}?subject={subject}&body={body}"

                    st.markdown(
                        f"""
                        <div style="background:rgba(16,185,129,0.1);border:1px solid rgba(16,185,129,0.3);
                             border-radius:8px;padding:1rem;margin-top:1rem;">
                            <p style="color:#6EE7B7;font-size:0.9rem;line-height:1.6;">
                                ✅ <strong>Message ready!</strong><br>
                                Click the button below to open your email client:
                            </p>
                            <a href="{mailto_link}" target="_blank"
                               style="display:inline-block;margin-top:0.5rem;padding:0.6rem 1.2rem;
                                      background:#10B981;color:white;text-decoration:none;
                                      border-radius:6px;font-weight:500;font-size:0.9rem;">
                               📧 Open Email Client
                            </a>
                        </div>
                        """,
                        unsafe_allow_html=True,
                    )

    st.markdown("<hr style='border-color:#1E293B;margin:2rem 0;'>", unsafe_allow_html=True)


def _try_lottie(path: str):
    """Render a Lottie animation if the file exists and streamlit-lottie is available."""
    if not os.path.exists(path):
        return
    try:
        from streamlit_lottie import st_lottie
        with open(path) as f:
            anim = json.load(f)
        st_lottie(anim, height=140, key="contact_lottie", speed=0.8)
    except Exception:
        pass  # silently skip if file missing or package unavailable
