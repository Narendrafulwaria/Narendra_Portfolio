# sections/contact.py — Section 14: Contact Form
import os
import json
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
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
            name    = st.text_input("Your Name",  key="contact_name")
            email   = st.text_input("Your Email", key="contact_email")
            message = st.text_area("Message", height=150, key="contact_message")

            submitted = st.form_submit_button("Send Message", width='stretch')

            if submitted:
                # Basic validation
                if not name.strip() or not email.strip() or not message.strip():
                    st.error("Please fill in all fields.")
                elif "@" not in email or "." not in email:
                    st.error("Please enter a valid email address.")
                else:
                    success, error_msg = _send_email(name, email, message)
                    if success:
                        st.markdown(
                            """
                            <div style="background:rgba(16,185,129,0.1);border:1px solid rgba(16,185,129,0.3);
                                 border-radius:8px;padding:1rem;margin-top:1rem;">
                                <p style="color:#6EE7B7;font-size:0.9rem;line-height:1.6;">
                                    ✅ <strong>Message sent!</strong><br>
                                    Thank you for reaching out. Narendra will get back to you soon.
                                </p>
                            </div>
                            """,
                            unsafe_allow_html=True,
                        )
                    else:
                        st.error(f"Failed to send message: {error_msg}")

    st.markdown("<hr style='border-color:#1E293B;margin:2rem 0;'>", unsafe_allow_html=True)


def _send_email(sender_name: str, sender_email: str, message: str) -> tuple[bool, str]:
    """
    Send contact form email via Gmail SMTP using App Password from secrets.
    Returns (True, "") on success or (False, error_message) on failure.
    """
    try:
        gmail_user     = st.secrets.get("GMAIL_SENDER", "")
        gmail_password = st.secrets.get("GMAIL_APP_PASSWORD", "")
        recipient      = PERSONAL_INFO.get("email", "")

        if not gmail_user or not gmail_password:
            return False, "Email credentials not configured in secrets.toml"

        # Build the email
        msg = MIMEMultipart("alternative")
        msg["Subject"] = f"Portfolio Contact from {sender_name}"
        msg["From"]    = gmail_user
        msg["To"]      = recipient
        msg["Reply-To"] = sender_email

        body_text = (
            f"New message from your portfolio contact form\n"
            f"{'─' * 40}\n"
            f"Name:    {sender_name}\n"
            f"Email:   {sender_email}\n"
            f"{'─' * 40}\n\n"
            f"{message}\n"
        )

        body_html = f"""
        <html><body style="font-family:sans-serif;color:#1E293B;background:#F8FAFC;padding:2rem;">
          <div style="max-width:560px;margin:auto;background:white;border-radius:10px;
                      padding:2rem;border:1px solid #E2E8F0;">
            <h2 style="color:#2563EB;margin-bottom:0.25rem;">New Portfolio Message</h2>
            <p style="color:#64748B;font-size:0.85rem;margin-bottom:1.5rem;">
              Submitted via your portfolio contact form
            </p>
            <table style="width:100%;border-collapse:collapse;margin-bottom:1.5rem;">
              <tr>
                <td style="padding:0.5rem 0;color:#64748B;width:80px;font-size:0.9rem;">Name</td>
                <td style="padding:0.5rem 0;font-weight:600;">{sender_name}</td>
              </tr>
              <tr>
                <td style="padding:0.5rem 0;color:#64748B;font-size:0.9rem;">Email</td>
                <td style="padding:0.5rem 0;">
                  <a href="mailto:{sender_email}" style="color:#2563EB;">{sender_email}</a>
                </td>
              </tr>
            </table>
            <div style="background:#F1F5F9;border-radius:8px;padding:1rem;
                        font-size:0.95rem;line-height:1.7;white-space:pre-wrap;">{message}</div>
          </div>
        </body></html>
        """

        msg.attach(MIMEText(body_text, "plain"))
        msg.attach(MIMEText(body_html, "html"))

        # Send via Gmail SMTP
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(gmail_user, gmail_password)
            server.sendmail(gmail_user, recipient, msg.as_string())

        return True, ""

    except smtplib.SMTPAuthenticationError:
        return False, "Gmail authentication failed. Check your App Password in secrets.toml."
    except Exception as exc:
        return False, str(exc)


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
