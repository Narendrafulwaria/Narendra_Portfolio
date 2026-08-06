# sections/github_stats.py — Section 9: GitHub Live Stats Dashboard
import streamlit as st
import plotly.graph_objects as go
from utils.github_api import fetch_github_stats
from utils.data import PERSONAL_INFO


def render_github_stats():
    st.markdown('<div id="github"></div>', unsafe_allow_html=True)
    st.markdown('<div class="section-heading">GitHub</div>', unsafe_allow_html=True)

    username = "Narendrafulwaria"

    with st.spinner("Fetching GitHub stats..."):
        stats = fetch_github_stats(username)

    if stats.get("error"):
        _render_fallback(username, stats["error"])
        return

    # ── Metric cards ─────────────────────────────────────────────────────
    m1, m2, m3 = st.columns(3, gap="medium")

    with m1:
        st.metric("Total Repos", stats["total_repos"])

    with m2:
        st.metric("Total Stars", stats["total_stars"])

    with m3:
        top_lang = max(stats["languages"].items(), key=lambda x: x[1])[0] if stats["languages"] else "N/A"
        st.metric("Top Language", top_lang)

    st.markdown("<br>", unsafe_allow_html=True)

    # ── Language donut chart ─────────────────────────────────────────────
    if stats["languages"]:
        _render_language_chart(stats["languages"])

    # ── Top repos grid ───────────────────────────────────────────────────
    st.markdown('<p style="color:#94A3B8;font-size:0.9rem;margin-bottom:0.75rem;">Top Repositories</p>', unsafe_allow_html=True)

    repos_per_row = 3
    repo_rows = [stats["top_repos"][i:i + repos_per_row] for i in range(0, len(stats["top_repos"]), repos_per_row)]

    for row in repo_rows:
        cols = st.columns(len(row), gap="medium")
        for col, repo in zip(cols, row):
            with col:
                _render_repo_card(repo)

    st.markdown("<hr style='border-color:#1E293B;margin:2rem 0;'>", unsafe_allow_html=True)


def _render_language_chart(languages: dict):
    """Render a Plotly donut chart of language distribution."""
    labels = list(languages.keys())
    values = list(languages.values())

    fig = go.Figure(data=[go.Pie(
        labels=labels,
        values=values,
        hole=0.6,
        marker=dict(
            colors=["#2563EB", "#06B6D4", "#10B981", "#F59E0B", "#8B5CF6", "#EC4899"][:len(labels)],
            line=dict(color="#1E293B", width=2)
        ),
        textinfo="label+percent",
        textfont=dict(size=11, color="#CBD5E1"),
        hoverinfo="label+value",
    )])

    fig.update_layout(
        paper_bgcolor="#0F172A",
        plot_bgcolor="#0F172A",
        showlegend=False,
        margin=dict(t=20, b=20, l=20, r=20),
        height=280,
    )

    st.plotly_chart(fig, use_container_width=True, config={"displayModeBar": False})


def _render_repo_card(repo: dict):
    """Render a single repository card."""
    name = repo.get("name", "").replace("&", "&amp;").replace("<", "&lt;")
    desc = repo.get("description", "").replace("&", "&amp;").replace("<", "&lt;")
    lang = repo.get("language", "N/A")
    stars = repo.get("stars", 0)
    url = repo.get("url", "")

    st.markdown(
        f"""
        <div class="repo-card">
            <div class="repo-name">{name}</div>
            <div class="repo-description">{desc}</div>
            <div style="display:flex;gap:0.5rem;margin-top:0.5rem;align-items:center;">
                <span style="color:#64748B;font-size:0.75rem;">🔹 {lang}</span>
                <span style="color:#64748B;font-size:0.75rem;">⭐ {stars}</span>
            </div>
            <a href="{url}" target="_blank" rel="noopener noreferrer"
               style="display:inline-block;margin-top:0.6rem;color:#2563EB;font-size:0.8rem;text-decoration:none;font-weight:500;">
               View on GitHub →
            </a>
        </div>
        """,
        unsafe_allow_html=True,
    )


def _render_fallback(username: str, error: str):
    """Render fallback when GitHub API fails."""
    st.warning(f"Could not fetch GitHub stats: {error}")
    st.markdown(
        f"""
        <div style="text-align:center;padding:2rem;">
            <p style="color:#94A3B8;margin-bottom:1rem;">
                Visit the GitHub profile directly to see repositories.
            </p>
            <a href="https://github.com/{username}" target="_blank"
               style="display:inline-block;padding:0.6rem 1.2rem;background:#2563EB;color:white;text-decoration:none;border-radius:8px;font-weight:500;">
               🐙 View GitHub Profile
            </a>
        </div>
        """,
        unsafe_allow_html=True,
    )
