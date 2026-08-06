# utils/github_api.py — Live GitHub stats via public REST API
import streamlit as st
import requests

_BASE_URL = "https://api.github.com"
_HEADERS  = {"Accept": "application/vnd.github+json"}


@st.cache_data(ttl=3600)
def fetch_github_stats(username: str) -> dict:
    """
    Fetch live GitHub stats for a public user.
    Cached for 1 hour (ttl=3600) to stay within the 60 req/hr unauthenticated limit.

    Returns dict with keys:
        total_repos  : int
        total_stars  : int
        languages    : dict {lang: count}
        top_repos    : list of dicts {name, description, url, language, stars}
        error        : str | None  — set if the API call failed
    """
    try:
        repos = _fetch_all_repos(username)
    except Exception as exc:
        return _empty_result(error=str(exc))

    if not repos:
        return _empty_result(error="No public repositories found.")

    # Aggregate stats
    total_stars = sum(r.get("stargazers_count", 0) for r in repos)

    # Language distribution (skip None entries)
    languages: dict[str, int] = {}
    for repo in repos:
        lang = repo.get("language")
        if lang:
            languages[lang] = languages.get(lang, 0) + 1

    # Sort by stars descending, take top 6
    sorted_repos = sorted(repos, key=lambda r: r.get("stargazers_count", 0), reverse=True)
    top_repos = [
        {
            "name":        r.get("name", ""),
            "description": r.get("description") or "No description provided.",
            "url":         r.get("html_url", ""),
            "language":    r.get("language") or "N/A",
            "stars":       r.get("stargazers_count", 0),
            "forks":       r.get("forks_count", 0),
        }
        for r in sorted_repos[:6]
    ]

    return {
        "total_repos": len(repos),
        "total_stars": total_stars,
        "languages":   languages,
        "top_repos":   top_repos,
        "error":       None,
    }


def _fetch_all_repos(username: str) -> list:
    """
    Paginate through all public repos for the user.
    GitHub returns max 100 per page; loop until no next page.
    """
    repos = []
    page  = 1
    while True:
        url  = f"{_BASE_URL}/users/{username}/repos"
        resp = requests.get(
            url,
            headers=_HEADERS,
            params={"per_page": 100, "page": page, "type": "public"},
            timeout=10,
        )

        if resp.status_code == 404:
            raise ValueError(f"GitHub user '{username}' not found.")
        if resp.status_code == 403:
            raise ValueError("GitHub API rate limit exceeded. Try again in an hour.")
        resp.raise_for_status()

        batch = resp.json()
        if not batch:
            break
        repos.extend(batch)
        # Stop if we got less than a full page — no more pages
        if len(batch) < 100:
            break
        page += 1

    return repos


def _empty_result(error: str = None) -> dict:
    return {
        "total_repos": 0,
        "total_stars": 0,
        "languages":   {},
        "top_repos":   [],
        "error":       error,
    }
