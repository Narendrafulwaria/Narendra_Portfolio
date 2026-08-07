# components/nav.py — Sticky top navigation bar using streamlit-option-menu
import streamlit as st
import streamlit.components.v1 as components
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


def scroll_to_section(anchor_id: str) -> None:
    """Scroll the main page to a section anchor (components run in an iframe)."""
    components.html(
        f"""
        <script>
            const target = window.parent.document.getElementById("{anchor_id}");
            if (target) {{
                target.scrollIntoView({{ behavior: "smooth", block: "start" }});
            }}
        </script>
        """,
        height=0,
    )


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
            background: #FFFFFF;
            padding: 0.25rem 0;
            border-bottom: 1px solid #BFDBFE;
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

    if "nav_selected" not in st.session_state:
        st.session_state["nav_selected"] = _LABELS[0]
    if "nav_scroll_to" not in st.session_state:
        st.session_state["nav_scroll_to"] = None

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
                    "background-color": "#FFFFFF",
                    "class": "nav-option-menu",
                },
                "icon":           {"color": "#2563EB",  "font-size": "0.85rem"},
                "nav-link":       {
                    "color": "#475569",
                    "font-size": "0.78rem",
                    "text-align": "center",
                    "padding": "0.4rem 0.5rem",
                    "--hover-color": "#EFF6FF",
                },
                "nav-link-selected": {
                    "background-color": "#2563EB",
                    "color": "#FFFFFF",
                    "font-weight": "600",
                },
            },
        )

    idx = _LABELS.index(selected_label) if selected_label in _LABELS else 0
    anchor_id = _IDS[idx]

    if selected_label != st.session_state["nav_selected"]:
        st.session_state["nav_selected"] = selected_label
        st.session_state["nav_scroll_to"] = anchor_id

    return anchor_id
