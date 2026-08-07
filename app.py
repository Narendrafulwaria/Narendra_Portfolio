# app.py — Entry point for Narendra Fulwaria's portfolio website
import streamlit as st

# ── Page configuration ─────────────────────────────────────────────────────
st.set_page_config(
    page_title="Narendra Fulwaria | Portfolio",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ── Imports ───────────────────────────────────────────────────────────────
from utils.styles import inject_css
from components.nav import render_nav, scroll_to_section
from sections.hero import render_hero
from sections.about import render_about
from sections.skills import render_skills
from sections.projects import render_projects
from sections.experience import render_experience
from sections.education import render_education
from sections.certifications import render_certifications
from sections.achievements import render_achievements
from sections.github_stats import render_github_stats
from sections.linkedin import render_linkedin
from sections.blog import render_blog
from sections.chatbot import render_chatbot
from sections.ats_widget import render_ats_widget
from sections.contact import render_contact
from sections.footer import render_footer

# ── Inject custom CSS ─────────────────────────────────────────────────────
inject_css()

# ── Initialize session state ───────────────────────────────────────────────
if "chat_history" not in st.session_state:
    st.session_state["chat_history"] = []
if "ats_result" not in st.session_state:
    st.session_state["ats_result"] = None
if "skill_view" not in st.session_state:
    st.session_state["skill_view"] = "progress"

# ── Render all sections in order ───────────────────────────────────────────
render_nav()
render_hero()
render_about()
render_skills()
render_projects()
render_experience()
render_education()
render_certifications()
render_achievements()
render_github_stats()
render_linkedin()
render_blog()
render_chatbot()
render_ats_widget()
render_contact()
render_footer()

if st.session_state.get("nav_scroll_to"):
    scroll_to_section(st.session_state["nav_scroll_to"])
    st.session_state["nav_scroll_to"] = None
