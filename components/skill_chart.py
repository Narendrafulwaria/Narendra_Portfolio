# components/skill_chart.py — Animated progress bars + Plotly radar chart
import streamlit as st
import plotly.graph_objects as go
from utils.data import SKILL_PROFICIENCY


def render_skill_chart():
    """
    Renders an animated skill visualization with two toggle views:
    - Progress Bars: animated CSS bar per skill
    - Radar Chart:   Plotly spider/polar chart
    Persists selected view in st.session_state["skill_view"].
    """
    if "skill_view" not in st.session_state:
        st.session_state["skill_view"] = "Progress Bars"

    view = st.radio(
        "View as:",
        options=["Progress Bars", "Radar Chart"],
        index=0 if st.session_state["skill_view"] == "Progress Bars" else 1,
        horizontal=True,
        key="skill_view_radio",
        label_visibility="collapsed",
    )
    st.session_state["skill_view"] = view

    st.markdown("<br>", unsafe_allow_html=True)

    if view == "Progress Bars":
        _render_progress_bars()
    else:
        _render_radar_chart()


# ---------------------------------------------------------------------------
# Progress bar view
# ---------------------------------------------------------------------------

def _render_progress_bars():
    bars_html = ""
    for skill, pct in SKILL_PROFICIENCY.items():
        pct = max(0, min(100, int(pct)))  # clamp 0–100
        bars_html += f"""
        <div class="skill-bar-wrapper">
            <div class="skill-bar-label">
                <span>{skill}</span>
                <span>{pct}%</span>
            </div>
            <div class="skill-bar-track">
                <div class="skill-bar-fill"
                     style="--fill-width:{pct}%; width:{pct}%">
                </div>
            </div>
        </div>
        """

    st.markdown(bars_html, unsafe_allow_html=True)


# ---------------------------------------------------------------------------
# Radar chart view
# ---------------------------------------------------------------------------

def _render_radar_chart():
    categories = list(SKILL_PROFICIENCY.keys())
    values     = list(SKILL_PROFICIENCY.values())

    # Close the polygon by repeating the first point
    cats_closed = categories + [categories[0]]
    vals_closed = values     + [values[0]]

    fig = go.Figure()

    # Filled area
    fig.add_trace(go.Scatterpolar(
        r=vals_closed,
        theta=cats_closed,
        fill="toself",
        fillcolor="rgba(37, 99, 235, 0.18)",
        line=dict(color="#2563EB", width=2),
        name="Proficiency",
        hovertemplate="<b>%{theta}</b><br>%{r}%<extra></extra>",
    ))

    # Data point markers
    fig.add_trace(go.Scatterpolar(
        r=values,
        theta=categories,
        mode="markers",
        marker=dict(color="#2563EB", size=8, symbol="circle"),
        showlegend=False,
        hovertemplate="<b>%{theta}</b><br>%{r}%<extra></extra>",
    ))

    fig.update_layout(
        polar=dict(
            bgcolor="#FFFFFF",
            radialaxis=dict(
                visible=True,
                range=[0, 100],
                tickfont=dict(color="#64748B", size=10),
                gridcolor="#E2E8F0",
                linecolor="#E2E8F0",
                tickvals=[20, 40, 60, 80, 100],
                ticktext=["20", "40", "60", "80", "100"],
            ),
            angularaxis=dict(
                tickfont=dict(color="#475569", size=12),
                gridcolor="#E2E8F0",
                linecolor="#E2E8F0",
            ),
        ),
        paper_bgcolor="#FFFFFF",
        plot_bgcolor="#FFFFFF",
        showlegend=False,
        margin=dict(t=40, b=40, l=60, r=60),
        height=420,
    )

    st.plotly_chart(fig, use_container_width=True, config={"displayModeBar": False})
