# Architecture: Narendra Fulwaria – Portfolio Website

---

## 1. System Overview

The portfolio is a **single-page Streamlit web application** written entirely in Python. It is hosted on **Streamlit Community Cloud** and auto-deploys from a GitHub repository on every push to the `main` branch. There is no separate backend server, database, or build pipeline — Streamlit serves both the UI and all dynamic logic (API calls, AI chatbot, ATS scoring).

```
┌─────────────────────────────────────────────────────┐
│                  Visitor's Browser                  │
└──────────────────────┬──────────────────────────────┘
                       │  HTTPS
┌──────────────────────▼──────────────────────────────┐
│           Streamlit Community Cloud                  │
│         (Auto-deployed from GitHub main)             │
│                                                     │
│   ┌─────────────────────────────────────────────┐   │
│   │           app.py  (Entry Point)             │   │
│   │                                             │   │
│   │  ┌──────────┐  ┌──────────┐  ┌──────────┐  │   │
│   │  │ sections/│  │components│  │  utils/  │  │   │
│   │  │ (15 UI   │  │(reusable │  │(helpers, │  │   │
│   │  │ sections)│  │ widgets) │  │ data,    │  │   │
│   │  └──────────┘  └──────────┘  │ API)     │  │   │
│   │                               └──────────┘  │   │
│   └─────────────────────────────────────────────┘   │
└──────────────────────┬──────────────────────────────┘
                       │
         ┌─────────────┼──────────────┐
         │             │              │
┌────────▼──────┐ ┌────▼──────┐ ┌────▼────────────┐
│  GitHub       │ │ Groq API  │ │  Static Assets  │
│  REST API     │ │(Chatbot — │ │  (PDF, images,  │
│ (public repos │ │ LLaMA 3)  │ │   Lottie JSON)  │
│  stats, langs)│ └───────────┘ └─────────────────┘
└───────────────┘
```

---

## 2. Project Folder Structure

```
narendra-portfolio/
│
├── app.py                        # Main entry point — renders all sections in order
│
├── sections/                     # One file per portfolio section
│   ├── hero.py                   # Section 1: Hero / Landing
│   ├── about.py                  # Section 2: About Me
│   ├── skills.py                 # Section 3: Technical Skills + Charts
│   ├── projects.py               # Section 4: Projects Cards
│   ├── experience.py             # Section 5: Professional Experience Timeline
│   ├── education.py              # Section 6: Education Timeline
│   ├── certifications.py         # Section 7: Certifications
│   ├── achievements.py           # Section 8: Key Achievements
│   ├── github_stats.py           # Section 9: GitHub Live Stats Dashboard
│   ├── linkedin.py               # Section 10: LinkedIn CTA
│   ├── blog.py                   # Section 11: Blog / Insights
│   ├── chatbot.py                # Section 12: "Ask Narendra" AI Chatbot
│   ├── ats_widget.py             # Section 13: Resume ATS Score Widget
│   ├── contact.py                # Section 14: Contact Form
│   └── footer.py                 # Section 15: Footer
│
├── components/                   # Reusable UI components
│   ├── card.py                   # Generic project / blog card renderer
│   ├── timeline.py               # Vertical timeline renderer (experience, education)
│   ├── skill_chart.py            # Radar chart + progress bar toggle component
│   ├── three_d_photo.py          # 3D profile photo card (CSS/Spline embed)
│   └── nav.py                    # Top navigation bar (streamlit-option-menu)
│
├── utils/                        # Business logic and helpers
│   ├── github_api.py             # GitHub REST API calls (repos, stars, languages)
│   ├── ats_scorer.py             # Keyword extraction + cosine similarity scoring
│   ├── chatbot_engine.py         # OpenAI/Gemini API wrapper + resume system prompt
│   ├── data.py                   # All static content (resume data as Python dicts)
│   └── styles.py                 # Custom CSS injected via st.markdown()
│
├── assets/
│   ├── profile_placeholder.png   # Profile photo (replaced with real photo)
│   ├── resume.pdf                # Downloadable resume PDF
│   ├── lottie/                   # Lottie JSON animation files
│   │   ├── hero_animation.json
│   │   ├── coding_animation.json
│   │   └── contact_animation.json
│   └── spline/                   # Spline 3D scene embed URL or exported file
│
├── .streamlit/
│   ├── config.toml               # Streamlit theme configuration (colors, fonts)
│   └── secrets.toml              # API keys (gitignored — set in Streamlit Cloud UI)
│
├── requirements.txt              # All Python dependencies (pinned versions)
├── .gitignore                    # Excludes secrets.toml, __pycache__, .env
└── README.md                     # Repo description + deployment instructions
```

---

## 3. Module Responsibilities

### 3.1 `app.py` — Entry Point
- Calls `st.set_page_config()` for title, favicon, and layout
- Injects global CSS via `utils/styles.py`
- Renders the navigation bar (`components/nav.py`)
- Imports and calls each section function in order (1–15)
- Manages session state keys used across sections (chat history, ATS results)

### 3.2 `sections/` — UI Sections

| File | Responsibility |
|------|---------------|
| `hero.py` | Renders name, tagline, location, 3D photo, CTA buttons |
| `about.py` | Bio text, 3D photo card, personality traits |
| `skills.py` | Skill badges + calls `skill_chart.py` for radar/progress toggle |
| `projects.py` | Loops over project data, renders project cards with GitHub links |
| `experience.py` | Calls `timeline.py` with experience data |
| `education.py` | Calls `timeline.py` with education data |
| `certifications.py` | Badge grid layout for certifications |
| `achievements.py` | Metric stat cards (icon + number + label) |
| `github_stats.py` | Calls `github_api.py`, renders charts and repo cards |
| `linkedin.py` | LinkedIn CTA button and card |
| `blog.py` | Renders blog cards with placeholders |
| `chatbot.py` | Chat UI, calls `chatbot_engine.py`, manages session chat history |
| `ats_widget.py` | Job description input, calls `ats_scorer.py`, renders results |
| `contact.py` | Contact form with validation, social links |
| `footer.py` | Copyright, nav links, social icons |

### 3.3 `utils/data.py` — Static Content Store
All portfolio content is stored as Python dictionaries and lists here — not hardcoded inside section files. This makes content updates a single-file change.

```python
# Example structure
PERSONAL_INFO = { "name": "...", "tagline": "...", "location": "...", ... }
SKILLS = { "Programming": [...], "Analytics": [...], ... }
SKILL_PROFICIENCY = { "Python": 75, "SQL": 80, ... }
PROJECTS = [ { "title": "...", "description": "...", "tech": [...], "url": "..." }, ... ]
EXPERIENCE = [ { "role": "...", "company": "...", "period": "...", "bullets": [...] }, ... ]
EDUCATION = [ { "degree": "...", "institution": "...", "year": "..." }, ... ]
CERTIFICATIONS = [ { "name": "...", "issuer": "...", "status": "..." }, ... ]
BLOG_POSTS = [ { "title": "...", "excerpt": "...", "date": "...", "url": "..." }, ... ]
```

### 3.4 `utils/github_api.py` — GitHub Live Stats
- Uses `requests` to call `https://api.github.com/users/Narendrafulwaria/repos`
- Extracts: repo count, total stars, language distribution, recent repos
- Returns structured dict consumed by `github_stats.py`
- Caches response with `@st.cache_data(ttl=3600)` to avoid rate limiting (60 req/hr unauthenticated)

### 3.5 `utils/ats_scorer.py` — ATS Score Engine
```
Input:  job_description (str)
        resume_text (str)  ← loaded from data.py as a flat string

Process:
  1. Tokenize + clean both texts (lowercase, remove stopwords)
  2. Extract keywords using TF-IDF (sklearn TfidfVectorizer)
  3. Compute cosine similarity → match percentage
  4. Identify matched keywords (intersection)
  5. Identify missing keywords (in JD but not in resume)

Output: {
  "score": 78,
  "matched_keywords": [...],
  "missing_keywords": [...],
  "recommendation": "..."
}
```

### 3.6 `utils/chatbot_engine.py` — AI Chatbot
- Loads resume content from `data.py` and constructs a system prompt
- Calls **Groq API** using the `groq` Python SDK with model `llama3-8b-8192` (fast, free tier available)
- Groq provides ultra-low latency inference — ideal for a responsive chat experience in Streamlit
- API key (`GROQ_API_KEY`) stored in `st.secrets` — never hardcoded
- Falls back to a static FAQ dict if no API key is configured
- Maintains conversation history in `st.session_state["chat_history"]`

**Groq API call pattern:**
```python
from groq import Groq

client = Groq(api_key=st.secrets["GROQ_API_KEY"])

response = client.chat.completions.create(
    model="llama3-8b-8192",
    messages=[
        {"role": "system", "content": system_prompt},
        *st.session_state["chat_history"]
    ]
)
reply = response.choices[0].message.content
```

**System Prompt Template:**
```
You are a professional AI assistant representing Narendra Madanlal Fulwaria.
Answer questions about his skills, projects, experience, and availability.
Only answer based on the provided resume context. Be concise and professional.

Resume Context:
{resume_text}
```

### 3.7 `components/three_d_photo.py` — 3D Profile Photo
- Renders a CSS 3D tilt card effect using `st.components.v1.html()`
- The card contains the profile image with a perspective transform on mouse hover
- Optionally replaced with a Spline 3D scene embed (`<iframe>` from spline.design)

### 3.8 `.streamlit/config.toml` — Theme
```toml
[theme]
primaryColor        = "#2563EB"   # Blue accent
backgroundColor     = "#0F172A"   # Dark navy background
secondaryBackgroundColor = "#1E293B"
textColor           = "#F1F5F9"
font                = "sans serif"
```

---

## 4. Data Flow Diagrams

### 4.1 Page Load Flow
```
Browser Request
      │
      ▼
app.py (st.set_page_config + CSS inject)
      │
      ├──► nav.py (render navigation)
      │
      ├──► hero.py ──► three_d_photo.py
      ├──► about.py ──► three_d_photo.py
      ├──► skills.py ──► skill_chart.py (Plotly radar + progress bars)
      ├──► projects.py ──► card.py (×5 project cards)
      ├──► experience.py ──► timeline.py
      ├──► education.py ──► timeline.py
      ├──► certifications.py
      ├──► achievements.py
      ├──► github_stats.py ──► github_api.py ──► GitHub REST API
      │                    └──► Plotly donut chart
      ├──► linkedin.py
      ├──► blog.py ──► card.py (×3 placeholder blog cards)
      ├──► chatbot.py (loads session state)
      ├──► ats_widget.py (loads resume text from data.py)
      ├──► contact.py
      └──► footer.py
```

### 4.2 Chatbot Interaction Flow
```
User types message
        │
        ▼
chatbot.py appends to st.session_state["chat_history"]
        │
        ▼
chatbot_engine.py
        │
        ├── st.secrets has GROQ_API_KEY?
        │       YES ──► Call Groq API (llama3-8b-8192) with system prompt + history
        │       NO  ──► Return static FAQ response
        │
        ▼
Response appended to chat_history
        │
        ▼
st.chat_message() re-renders full conversation
```

### 4.3 ATS Widget Flow
```
Visitor pastes job description
        │
        ▼
ats_widget.py → ats_scorer.py
        │
        ├── TF-IDF vectorize JD + resume_text
        ├── Compute cosine similarity
        ├── Extract matched / missing keywords
        └── Generate recommendation string
        │
        ▼
Display: score gauge + keyword chips + recommendation text
```

### 4.4 GitHub Stats Flow
```
github_stats.py loads
        │
        ▼
github_api.py (cached, TTL=1hr)
        │
        ▼
GET https://api.github.com/users/Narendrafulwaria/repos
        │
        ├── Parse: repo names, stars, languages, descriptions
        ├── Aggregate: total stars, language counts
        └── Sort: top 5 repos by stars
        │
        ▼
Plotly donut chart (language distribution)
Repo cards (name, description, language badge, star count)
Metric cards (total repos, total stars)
```

---

## 5. State Management

Streamlit re-renders the entire app on each interaction. Session state is used to persist data across rerenders:

| Key | Type | Used By | Purpose |
|-----|------|---------|---------|
| `chat_history` | `list[dict]` | `chatbot.py` | Stores full conversation with roles + content |
| `ats_result` | `dict` | `ats_widget.py` | Caches last ATS score result |
| `skill_view` | `str` | `skills.py` | Tracks whether user selected "progress" or "radar" view |
| `github_data` | `dict` | `github_stats.py` | Cached GitHub API response (via `st.cache_data`) |

---

## 6. External Dependencies

### Python Packages (`requirements.txt`)
```
streamlit==1.35.0
streamlit-option-menu==0.3.12
streamlit-lottie==0.0.5
streamlit-extras==0.4.2
plotly==5.22.0
requests==2.32.3
scikit-learn==1.5.0
groq==0.9.0
Pillow==10.3.0
```

### External Services

| Service | Purpose | Auth Required | Rate Limit |
|---------|---------|--------------|------------|
| GitHub REST API | Live repo stats | No (public) | 60 req/hr |
| Groq API | AI Chatbot (LLaMA 3) | Yes (`GROQ_API_KEY` in st.secrets) | Free tier: 30 req/min |
| Spline.design | 3D profile photo embed | No (public URL) | None |
| Lottie Files | Animation JSON files | No (local files) | None |

---

## 7. Security Considerations

- **API keys** are never hardcoded — `GROQ_API_KEY` stored in `.streamlit/secrets.toml` locally and in the Streamlit Cloud secrets manager for production
- `secrets.toml` is listed in `.gitignore` — never committed to GitHub
- **Contact form** does not persist data server-side (no database); submissions handled via `mailto:` link or `smtplib` with credentials in secrets
- **GitHub API** uses unauthenticated public endpoints only — no token needed, no write access
- **ATS Widget** runs entirely offline (no external calls); user-pasted job descriptions are not stored or transmitted

---

## 8. Deployment Pipeline

```
Local Development
      │
      │  git push origin main
      ▼
GitHub Repository (Narendrafulwaria/narendra-portfolio)
      │
      │  Streamlit Cloud watches main branch
      ▼
Streamlit Community Cloud
      │
      ├── Installs requirements.txt
      ├── Reads secrets from Streamlit Cloud dashboard
      └── Serves app at: https://narendrafulwaria.streamlit.app
```

**Steps to deploy:**
1. Push code to a public GitHub repo
2. Sign in at [share.streamlit.io](https://share.streamlit.io) with GitHub account
3. Click "New app" → select repo → set `app.py` as entry point
4. Add `GROQ_API_KEY` under "Advanced settings → Secrets"
5. Click Deploy — live in ~2 minutes

---

## 9. Section-to-File Mapping Summary

| Section | File | Key Libraries |
|---------|------|--------------|
| 1. Hero | `sections/hero.py` | Streamlit, CSS, `three_d_photo.py` |
| 2. About | `sections/about.py` | Streamlit, CSS, `three_d_photo.py` |
| 3. Skills | `sections/skills.py` | Plotly, CSS animations |
| 4. Projects | `sections/projects.py` | Streamlit, `card.py` |
| 5. Experience | `sections/experience.py` | `timeline.py` |
| 6. Education | `sections/education.py` | `timeline.py` |
| 7. Certifications | `sections/certifications.py` | Streamlit |
| 8. Achievements | `sections/achievements.py` | Streamlit metrics |
| 9. GitHub Stats | `sections/github_stats.py` | requests, Plotly, `github_api.py` |
| 10. LinkedIn | `sections/linkedin.py` | Streamlit, CSS |
| 11. Blog | `sections/blog.py` | `card.py` |
| 12. AI Chatbot | `sections/chatbot.py` | groq, `chatbot_engine.py` |
| 13. ATS Widget | `sections/ats_widget.py` | scikit-learn, `ats_scorer.py` |
| 14. Contact | `sections/contact.py` | Streamlit forms |
| 15. Footer | `sections/footer.py` | Streamlit, CSS |
