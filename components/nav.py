# components/nav.py — Sticky top navigation bar using streamlit-option-menu
import streamlit as st
from streamlit_option_menu import option_menu


NAV_ITEMS = [
    ("Home",            "house-fill",           "home"),
    ("About",           "person-fill",          "about"),
    ("Skills",          "lightning-charge-fill", "skills"),
    ("Projects",        "folder2-open",         "projects"),
    ("Experience",      "briefcase-fill",       "experience"),
    ("Education",       "mortarboard-fill",     "education"),
    ("Certifications",  "patch-check-fill",     "certifications"),
    ("GitHub",          "github",               "github"),
    ("Blog",            "journal-text",         "blog"),
    ("Ask Narendra",    "robot",                "chatbot"),
    ("ATS Tool",        "file-earmark-check",   "ats"),
    ("Contact",         "envelope-fill",        "contact"),
]

_LABELS = [item[0] for item in NAV_ITEMS]
_ICONS  = [item[1] for item in NAV_ITEMS]
_IDS    = [item[2] for item in NAV_ITEMS]


def render_nav() -> str:
    """
    Renders the sticky horizontal navigation bar.
    Returns the anchor id of the selected section (e.g. 'about').
    """
    # Sticky wrapper via HTML
    st.markdown(
        """
        <style>
        div[data-testid="stHorizontalBlock"]:has(.nav-option-menu) {
            position: sticky;
            top: 0;
            z-index: 999;
            background: #0F172A;
            padding: 0.25rem 0;
            border-bottom: 1px solid #1E293B;
        }
        /* Shrink option-menu font for compact fit */
        .nav-option-menu .nav-link {
            font-size: 0.75rem !important;
            padding: 0.4rem 0.6rem !important;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    with st.container():
        selected_label = option_menu(
            menu_title=None,
            options=_LABELS,
            icons=_ICONS,
            default_index=0,
            orientation="horizontal",
            key="nav_option_menu",
            styles={
                "container": {
                    "padding": "0",
                    "background-color": "#0F172A",
                    "class": "nav-option-menu",
                },
                "icon":           {"color": "#2563EB",  "font-size": "0.85rem"},
                "nav-link":       {
                    "color": "#94A3B8",
                    "font-size": "0.78rem",
                    "text-align": "center",
                    "padding": "0.4rem 0.5rem",
                    "--hover-color": "#1E293B",
                },
                "nav-link-selected": {
                    "background-color": "#1E3A8A",
                    "color": "#F1F5F9",
                    "font-weight": "600",
                },
            },
        )

    # Map selected label → anchor id and inject scroll JS
    idx = _LABELS.index(selected_label) if selected_label in _LABELS else 0
    anchor_id = _IDS[idx]

    if selected_label != "Home":
        st.markdown(
            f"""
            <script>
                const el = document.getElementById('{anchor_id}');
                if (el) {{ el.scrollIntoView({{behavior: 'smooth', block: 'start'}}); }}
            </script>
            """,
            unsafe_allow_html=True,
        )

    return anchor_id
