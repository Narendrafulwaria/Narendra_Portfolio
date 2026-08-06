# Implementation Plan: Narendra Fulwaria – Portfolio Website

---

## Overview

This document breaks down the build into ordered phases and individual tasks.
Each task maps directly to a file or module defined in `architecture.md`.
Tasks must be completed in phase order — later phases depend on earlier ones.

---

## Phase 0: Project Setup & Configuration

### Task 0.1 — Initialize Project Structure
Create all directories and empty placeholder files as defined in the architecture.

**Files to create:**
```
narendra-portfolio/
├── app.py
├── requirements.txt
├── .gitignore
├── README.md
├── sections/          (15 empty .py files)
├── components/        (5 empty .py files)
├── utils/             (5 empty .py files)
├── assets/
│   ├── lottie/
│   └── spline/
└── .streamlit/
    ├── config.toml
    └── secrets.toml   (gitignored)
```

**Acceptance:** `python -m streamlit run app.py` runs without import errors.

---

### Task 0.2 — `requirements.txt`

Write pinned dependencies:
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

**Acceptance:** `pip install -r requirements.txt` completes without errors.

---

### Task 0.3 — `.streamlit/config.toml`
Configure the dark navy theme:
```toml
[theme]
primaryColor             = "#2563EB"
backgroundColor          = "#0F172A"
secondaryBackgroundColor = "#1E293B"
textColor                = "#F1F5F9"
font                     = "sans serif"
```

---

### Task 0.4 — `.gitignore`
```
.streamlit/secrets.toml
__pycache__/
*.pyc
.env
*.egg-info/
dist/
.DS_Store
```

---

### Task 0.5 — `.streamlit/secrets.toml` (local only, never committed)
```toml
GROQ_API_KEY = "your_groq_api_key_here"
```

---

## Phase 1: Static Data Layer

### Task 1.1 — `utils/data.py`

Define all portfolio content as Python constants. No hardcoding in section files.

**Data objects to define:**
- `PERSONAL_INFO` — name, tagline, location, phone, email, github_url, linkedin_url
- `SKILLS` — dict of category → list of skill strings
- `SKILL_PROFICIENCY` — dict of skill → integer (0–100)
- `PROJECTS` — list of dicts: title, description, tech (list), url
- `EXPERIENCE` — list of dicts: role, company, period, bullets (list)
- `EDUCATION` — list of dicts: degree, institution, year
- `CERTIFICATIONS` — list of dicts: name, issuer, status
- `ACHIEVEMENTS` — list of dicts: icon, value, label
- `BLOG_POSTS` — list of dicts: title, excerpt, date, url
- `RESUME_TEXT` — flat string of resume content (used by ATS scorer + chatbot system prompt)

**Acceptance:** `from utils.data import PERSONAL_INFO` works in any section file.

---

### Task 1.2 — `utils/styles.py`
Build a single function `inject_css()` that returns a large CSS string injected via `st.markdown(..., unsafe_allow_html=True)`.

**CSS to include:**
- Hide default Streamlit header/footer/hamburger menu
- Section anchor padding for smooth scroll
- Card styles: border-radius, box-shadow, hover lift effect
- Timeline styles: vertical line, dot markers
- Badge/chip styles for skill tags and tech tags
- Button override styles matching the blue primary color
- Responsive column gap adjustments

**Acceptance:** `inject_css()` called in `app.py` applies styles globally without breaking layout.

---

## Phase 2: Reusable Components

### Task 2.1 — `components/nav.py`

Build a sticky top navigation bar using `streamlit-option-menu`.

**Implementation details:**
- Use `option_menu()` in horizontal orientation
- Menu items: Home, About, Skills, Projects, Experience, Education, Certifications, GitHub, Blog, Chatbot, ATS Tool, Contact
- Icons from `bootstrap-icons` or `font-awesome` set
- Clicking a menu item scrolls to the corresponding section anchor (`st.markdown("<div id='section-id'>")`)
- Sticky via CSS `position: sticky; top: 0; z-index: 999`

**Acceptance:** Navigation bar renders at top; all menu items visible; clicking scrolls to correct section.

---

### Task 2.2 — `components/three_d_photo.py`
Build a 3D tilt card effect for the profile photo using `st.components.v1.html()`.

**Implementation details:**
- Inject a self-contained HTML/CSS/JS block
- CSS perspective transform on the wrapper div
- JavaScript `mousemove` event listener applies `rotateX` and `rotateY` transforms on hover
- Subtle shine/glare overlay layer on top of the image
- Smooth `transition: transform 0.1s ease` for fluid movement
- On `mouseleave`: reset transform to `rotateX(0) rotateY(0)`
- Image source: `assets/profile_placeholder.png` (base64 encoded or served as static file)

**Sample JS logic:**
```javascript
card.addEventListener('mousemove', (e) => {
    const rect = card.getBoundingClientRect();
    const x = e.clientX - rect.left - rect.width / 2;
    const y = e.clientY - rect.top - rect.height / 2;
    card.style.transform =
        `perspective(600px) rotateY(${x / 20}deg) rotateX(${-y / 20}deg)`;
});
card.addEventListener('mouseleave', () => {
    card.style.transform = 'perspective(600px) rotateY(0deg) rotateX(0deg)';
});
```

**Acceptance:** Profile image renders with visible 3D tilt on mouse hover.

---

### Task 2.3 — `components/card.py`

Build a reusable card renderer for both project cards and blog cards.

**Function signature:**
```python
def render_card(title, description, tags=[], link=None, link_label="View →", date=None)
```

**Implementation details:**
- Rendered via `st.markdown()` with inline HTML
- Card: white/dark rounded box, drop shadow, hover lift via CSS transition
- Tags rendered as colored badge chips (blue tint)
- Link renders as a styled anchor button at the bottom of the card
- Optional `date` field shown in muted text for blog cards

**Acceptance:** `render_card(...)` renders correctly for both project and blog use cases.

---

### Task 2.4 — `components/timeline.py`
Build a vertical timeline component for experience and education sections.

**Function signature:**
```python
def render_timeline(items: list[dict], item_type="experience")
```

**Implementation details:**
- Left vertical line with circular dot markers
- Each item: title/role (bold), subtitle/company (muted), period badge on the right
- For `item_type="experience"`: render bullet points below the header
- For `item_type="education"`: render single-line institution + year
- Implemented via `st.markdown()` with HTML/CSS

**Acceptance:** Timeline renders with correct vertical line and dot markers for all items.

---

### Task 2.5 — `components/skill_chart.py`
Build the animated skill visualization component.

**Implementation details:**
- Two views toggled via `st.radio()` or `st.selectbox()`: "Progress Bars" and "Radar Chart"
- **Progress bar view:** render each skill as a labeled bar using `st.markdown()` HTML with a CSS `width: {pct}%` filled bar — animated with `@keyframes fillBar` on load
- **Radar chart view:** use `plotly.graph_objects.Scatterpolar` to render a filled radar/spider chart
  - Categories: Python, SQL, Data Analytics, BI Tools, AI Automation, Business Operations
  - Values pulled from `SKILL_PROFICIENCY` in `data.py`
  - Dark background (`bgcolor='#0F172A'`), blue fill color
- Store selected view in `st.session_state["skill_view"]`

**Acceptance:** Both views render without errors; toggle switches between them correctly.

---

## Phase 3: Utility Modules

### Task 3.1 — `utils/github_api.py`

Fetch live GitHub stats for `Narendrafulwaria`.

**Function:**
```python
@st.cache_data(ttl=3600)
def fetch_github_stats(username: str) -> dict:
    ...
```

**Implementation details:**
- GET `https://api.github.com/users/{username}/repos?per_page=100`
- Parse response to extract:
  - `total_repos`: len of repo list
  - `total_stars`: sum of `stargazers_count`
  - `languages`: dict of language → count (skip `None`)
  - `top_repos`: top 5 by `stargazers_count`, each with name, description, url, language, stars
- Handle HTTP errors gracefully — return empty dict with error flag on failure
- `ttl=3600` caches for 1 hour to stay within 60 req/hr rate limit

**Acceptance:** Function returns correctly structured dict; cached on repeat calls.

---

### Task 3.2 — `utils/ats_scorer.py`
Build the offline ATS keyword match engine.

**Function:**
```python
def score_resume(job_description: str, resume_text: str) -> dict:
    ...
```

**Implementation details:**
1. Lowercase and clean both input strings
2. Use `sklearn.feature_extraction.text.TfidfVectorizer` with `stop_words='english'`
3. Fit-transform on `[resume_text, job_description]`
4. Compute cosine similarity between the two vectors
5. Extract top N keywords from the JD vector (highest TF-IDF weights)
6. Split into `matched_keywords` (present in resume) and `missing_keywords` (absent)
7. Generate a `recommendation` string based on score range:
   - ≥80%: "Strong match — your profile aligns well with this role."
   - 60–79%: "Good match — consider highlighting your {top missing skill}."
   - <60%: "Partial match — add more keywords from the job description."
8. Return `{"score": int, "matched_keywords": list, "missing_keywords": list, "recommendation": str}`

**Acceptance:** Returns sensible score and keyword lists for a sample job description.

---

### Task 3.3 — `utils/chatbot_engine.py`
Build the Groq-powered chatbot engine.

**Functions:**
```python
def build_system_prompt() -> str:
def get_response(user_message: str, chat_history: list) -> str:
```

**Implementation details:**
- `build_system_prompt()`: reads `RESUME_TEXT` and `PERSONAL_INFO` from `data.py`, formats into the system prompt template
- `get_response()`:
  - Check `"GROQ_API_KEY" in st.secrets` — if missing, return static FAQ answer
  - Initialize `Groq(api_key=st.secrets["GROQ_API_KEY"])`
  - Call `client.chat.completions.create(model="llama3-8b-8192", messages=[system_msg, *history, user_msg])`
  - Return `response.choices[0].message.content`
  - Wrap in try/except — return error message string on API failure

**Static FAQ fallback:** dict of common questions → canned answers loaded from `data.py`

**Acceptance:** Returns a valid response string for a test question both with and without API key.

---

## Phase 4: Section Implementations

### Task 4.1 — `sections/hero.py`

**Layout:** Two-column — left: text + CTA buttons; right: 3D photo card.

**Content:**
- Full name as `<h1>` with gradient text effect (blue → cyan)
- Animated typewriter tagline: "Data Analyst | AI Automation | Business Analytics"
- Location badge with 📍 icon
- Three CTA buttons side by side:
  - "View Projects" → JS scroll to `#projects`
  - "Download Resume" → `st.download_button` linking `assets/resume.pdf`
  - "Contact Me" → JS scroll to `#contact`
- Lottie animation (hero_animation.json) as subtle background or beside text
- Right column: `render_3d_photo()` from `components/three_d_photo.py`

**Acceptance:** Hero section renders with name, tagline, buttons, and 3D photo.

---

### Task 4.2 — `sections/about.py`
**Layout:** Two-column — left: 3D photo; right: bio text.

**Content:**
- Section heading "About Me" with anchor `id="about"`
- Professional summary paragraph from `PERSONAL_INFO`
- Three trait pills: "🧠 Analytical Thinker", "🔧 Problem Solver", "📚 Self-Learner"
- Lottie animation (coding_animation.json) below bio text

**Acceptance:** Section renders with bio, traits, and 3D photo visible.

---

### Task 4.3 — `sections/skills.py`
**Content:**
- Section heading "Technical Skills" with anchor `id="skills"`
- Skill badge grid: loop over `SKILLS` dict, render category label + badges per skill
- Below badges: `render_skill_chart()` from `components/skill_chart.py` with view toggle

**Acceptance:** Skill badges display in grouped rows; radar chart and progress bars both render.

---

### Task 4.4 — `sections/projects.py`
**Content:**
- Section heading "Projects" with anchor `id="projects"`
- 3-column responsive grid (use `st.columns(3)` then wrap remainder)
- Loop over `PROJECTS` list, call `render_card(...)` for each
- Each card shows title, description, tech badges, "View on GitHub →" link

**Acceptance:** All 5 project cards render with correct GitHub links.

---

### Task 4.5 — `sections/experience.py`
**Content:**
- Section heading "Professional Experience" with anchor `id="experience"`
- Call `render_timeline(EXPERIENCE, item_type="experience")`

**Acceptance:** Timeline shows both experience entries with bullets.

---

### Task 4.6 — `sections/education.py`
**Content:**
- Section heading "Education" with anchor `id="education"`
- Call `render_timeline(EDUCATION, item_type="education")`

**Acceptance:** Timeline shows all 3 education entries.

---

### Task 4.7 — `sections/certifications.py`
**Content:**
- Section heading "Certifications" with anchor `id="certifications"`
- Loop over `CERTIFICATIONS`, render each as a styled card with:
  - Certificate icon 🏅
  - Certification name (bold)
  - Issuer (muted)
  - Status badge: green "Completed" or yellow "In Progress"

**Acceptance:** All 5 certifications render with correct status badges.

---

### Task 4.8 — `sections/achievements.py`
**Content:**
- Section heading "Key Achievements" with anchor `id="achievements"`
- 4-column metric grid using `st.columns(4)`
- Each achievement: icon, value/headline, description label
- Use `st.metric()` or custom HTML stat cards

**Acceptance:** 4 achievement cards render in a single row.

---

### Task 4.9 — `sections/github_stats.py`

**Content:**
- Section heading "GitHub" with anchor `id="github"`
- Call `fetch_github_stats("Narendrafulwaria")` from `utils/github_api.py`
- Show loading spinner (`st.spinner`) while fetching
- On success:
  - 3 metric cards: Total Repos, Total Stars, Top Language
  - Plotly donut chart of language distribution
  - 5 repo cards in a 2–3 column grid (name, description, language badge, ⭐ count, link)
- On failure: show a static fallback with GitHub profile link

**Acceptance:** Stats and repo cards render with live data from GitHub API.

---

### Task 4.10 — `sections/linkedin.py`
**Content:**
- Section heading "Let's Connect" with anchor `id="linkedin"`
- Centered LinkedIn icon + CTA text: "Let's connect professionally"
- Large styled "Connect on LinkedIn →" button linking to LinkedIn profile URL
- URL sourced from `PERSONAL_INFO["linkedin_url"]` (placeholder until provided)

**Acceptance:** Section renders with button linking to correct URL.

---

### Task 4.11 — `sections/blog.py`
**Content:**
- Section heading "Blog & Insights" with anchor `id="blog"`
- Loop over `BLOG_POSTS` list, call `render_card(...)` with `date` field
- Show 3 placeholder blog cards with title, excerpt, date, and "Read More →" link
- Note at bottom: "More articles coming soon — follow on LinkedIn"

**Acceptance:** 3 blog cards render; links open in new tab.

---

### Task 4.12 — `sections/chatbot.py`
**Content:**
- Section heading "Ask Narendra 🤖" with anchor `id="chatbot"`
- Brief description: "Ask me anything about Narendra's skills, projects, or availability."
- Initialize `st.session_state["chat_history"]` to `[]` if not set
- Render existing chat history using `st.chat_message()` loop
- `st.chat_input("Ask a question...")` captures new input
- On new input:
  1. Append `{"role": "user", "content": message}` to history
  2. Call `get_response(message, history)` from `utils/chatbot_engine.py`
  3. Append assistant response to history
  4. Rerender (Streamlit reruns automatically)
- Show "Clear Chat" button to reset `chat_history`

**Acceptance:** Chat accepts input, gets a response, maintains history across multiple messages.

---

### Task 4.13 — `sections/ats_widget.py`
**Content:**
- Section heading "Resume ATS Match Tool 🎯" with anchor `id="ats"`
- Subtext: "Paste any job description to see how well Narendra's resume matches it."
- `st.text_area("Job Description", height=200)` for input
- "Analyze Match" button triggers `score_resume()` from `utils/ats_scorer.py`
- Store result in `st.session_state["ats_result"]`
- Display results:
  - Score as a large colored number (green ≥80, yellow 60–79, red <60) or `st.progress()` bar
  - Two columns: "✅ Matched Keywords" and "❌ Missing Keywords" as badge chips
  - Recommendation text in a styled info box
- "Clear" button resets the widget

**Acceptance:** Pasting a data analyst job description returns a score, keyword lists, and recommendation.

---

### Task 4.14 — `sections/contact.py`
**Content:**
- Section heading "Contact Me" with anchor `id="contact"`
- Lottie animation (contact_animation.json) beside form
- Contact details: 📍 Mumbai, 📞 9833607051, links to GitHub + LinkedIn
- `st.form("contact_form")` with:
  - `st.text_input("Your Name")`
  - `st.text_input("Your Email")`
  - `st.text_area("Message", height=150)`
  - `st.form_submit_button("Send Message")`
- On submit: basic validation (non-empty fields, valid email format)
- Submission action: construct `mailto:` URL and open via JS, or display a success message
  with instructions to email directly (no server-side storage)

**Acceptance:** Form renders, validates input, and shows success state on submission.

---

### Task 4.15 — `sections/footer.py`
**Content:**
- Horizontal divider
- Centered: "© 2025 Narendra Madanlal Fulwaria. All rights reserved."
- Quick nav links row: Home | About | Projects | Contact
- Social icon row: GitHub 🐙 | LinkedIn 💼
- Built-with note: "Built with Python & Streamlit"

**Acceptance:** Footer renders at bottom with correct links.

---

## Phase 5: Entry Point Assembly

### Task 5.1 — `app.py`
Wire everything together in the correct render order.

```python
import streamlit as st
from utils.styles import inject_css
from components.nav import render_nav
from sections.hero import render_hero
from sections.about import render_about
# ... all imports

st.set_page_config(
    page_title="Narendra Fulwaria | Portfolio",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="collapsed"
)

inject_css()

# Initialize session state
if "chat_history" not in st.session_state:
    st.session_state["chat_history"] = []
if "ats_result" not in st.session_state:
    st.session_state["ats_result"] = None
if "skill_view" not in st.session_state:
    st.session_state["skill_view"] = "progress"

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
```

**Acceptance:** Full app renders top-to-bottom without errors; all 15 sections visible.

---

## Phase 6: Assets

### Task 6.1 — Download Lottie JSON Files
Download 3 Lottie animation JSON files from [lottiefiles.com](https://lottiefiles.com) and save to `assets/lottie/`:
- `hero_animation.json` — suggested search: "data analytics" or "tech hero"
- `coding_animation.json` — suggested search: "coding" or "programming"
- `contact_animation.json` — suggested search: "contact" or "message"

**Acceptance:** All 3 JSON files present in `assets/lottie/`; no 404 errors when loaded.

---

### Task 6.2 — Profile Photo Placeholder
- Save a placeholder square image as `assets/profile_placeholder.png`
- Minimum size: 400×400px
- Replace with real photo when provided by Narendra

---

### Task 6.3 — Resume PDF
- Save Narendra's resume PDF as `assets/resume.pdf`
- Must be accessible via `st.download_button(data=open("assets/resume.pdf","rb").read(), ...)`

---

## Phase 7: Deployment

### Task 7.1 — GitHub Repository Setup
1. Create a new **public** GitHub repository: `narendra-portfolio`
2. Push all files to `main` branch
3. Ensure `.streamlit/secrets.toml` is in `.gitignore` and **not** pushed

---

### Task 7.2 — Streamlit Community Cloud Deployment
1. Sign in at [share.streamlit.io](https://share.streamlit.io) with GitHub account
2. Click "New app"
3. Select repo: `Narendrafulwaria/narendra-portfolio`
4. Set main file path: `app.py`
5. Under "Advanced settings → Secrets", add:
   ```toml
   GROQ_API_KEY = "your_actual_groq_api_key"
   ```
6. Click "Deploy"
7. App goes live at `https://narendrafulwaria.streamlit.app`

---

### Task 7.3 — Post-Deployment Verification
- [ ] All 15 sections visible and scroll correctly
- [ ] 3D photo card tilt effect works
- [ ] GitHub stats load with real data
- [ ] Skill radar chart and progress bars render
- [ ] Chatbot responds to "What projects has Narendra built?"
- [ ] ATS Widget returns a score for a sample job description
- [ ] Resume PDF downloads successfully
- [ ] Contact form submits without errors
- [ ] All GitHub project links open correctly
- [ ] Site loads on mobile without broken layout

---

## Implementation Order Summary

| Phase | Tasks | Depends On |
|-------|-------|------------|
| 0 — Setup | 0.1 – 0.5 | Nothing |
| 1 — Data Layer | 1.1 – 1.2 | Phase 0 |
| 2 — Components | 2.1 – 2.5 | Phase 1 |
| 3 — Utilities | 3.1 – 3.3 | Phase 1 |
| 4 — Sections | 4.1 – 4.15 | Phases 2 + 3 |
| 5 — Assembly | 5.1 | Phase 4 |
| 6 — Assets | 6.1 – 6.3 | Phase 0 |
| 7 — Deployment | 7.1 – 7.3 | Phases 5 + 6 |

Total tasks: **31**
