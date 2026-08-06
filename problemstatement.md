# Problem Statement: Narendra Fulwaria – Personal Portfolio Website

## Overview

Design and develop a modern, responsive personal portfolio website for **Narendra Madanlal Fulwaria**, an Electronics & Telecommunication Engineering graduate transitioning into Data Analytics, Business Analytics, AI Automation, and Generative AI. The website must professionally showcase his skills, projects, experience, and career journey to potential employers and collaborators in the tech and analytics space.

---

## Goals

- Present Narendra's professional identity in a clean, modern, and ATS-friendly web format.
- Highlight his unique blend of 6+ years of business operations experience with newly acquired technical and AI skills.
- Make it easy for recruiters and hiring managers to explore his work, contact him, and view his GitHub projects.
- Establish a strong personal brand aligned with Data Analytics, AI Automation, and Generative AI roles.

---

## Target Audience

- Recruiters and hiring managers in Data Analytics, Business Analytics, and AI/Automation domains.
- Potential collaborators or clients interested in AI workflow automation.
- Technical peers reviewing his GitHub projects and code portfolio.

---

## Deployment

- **Platform:** [Streamlit](https://streamlit.io/) — the portfolio will be built as a Streamlit web app and deployed via **Streamlit Community Cloud**, connected to Narendra's GitHub repository.
- **Repository:** [github.com/Narendrafulwaria](https://github.com/Narendrafulwaria) — the portfolio source code will live in a dedicated GitHub repo, and Streamlit will auto-deploy on every push to the main branch.
- **No separate backend needed** — Streamlit handles both the UI and any dynamic logic (e.g., contact form, GitHub API calls).

---

## Required Sections

### 1. Hero / Landing Section
- Full name: **Narendra Madanlal Fulwaria**
- Designation / tagline (e.g., "Data Analyst | AI Automation Enthusiast | Business Analytics")
- Location: Mumbai, Maharashtra
- **3D Profile Photo** — rendered using a 3D avatar or a CSS/Three.js-powered 3D card effect around the profile image (e.g., tilt-on-hover 3D card, or a Spline-rendered 3D avatar). Placeholder used until real photo is provided.
- Call-to-action buttons: **View Projects**, **Download Resume**, **Contact Me**
- Subtle animated background or gradient to make a strong first impression

### 2. About Me
- Brief professional bio summarizing his background:
  - Electronics & Telecommunication Engineering graduate
  - 6+ years of business operations and retail management
  - Currently transitioning into Data Analytics, AI Automation, and Generative AI
- **3D animated profile photo card** (tilt/parallax effect on hover, rendered with CSS transforms or a Spline embed)
- Highlight key personality traits: analytical thinker, problem solver, self-learner

### 3. Technical Skills — Animated Skill Visualization
Organized into visual skill cards or grouped badges:
- **Programming:** Python, SQL, MySQL
- **Analytics:** Pandas, NumPy, Data Cleaning, Data Visualization
- **BI Tools:** Excel, Tableau, Power BI
- **Automation:** n8n, Webhooks, AI Workflow Automation
- **Other:** GitHub, Business Analytics, Inventory Analytics, CRM, Team Management

**Animated Skill Progress Bars / Radar Chart:**
- Each skill category rendered as an **animated progress bar** (fills on page load with smooth CSS/JS animation)
- A **radar/spider chart** (using Plotly) showing proficiency across key domains: Python, SQL, Data Analytics, BI Tools, AI Automation, Business Operations
- Proficiency levels assigned per skill (e.g., Python: 75%, SQL: 80%, Power BI: 70%, n8n Automation: 85%, Business Ops: 95%)
- Toggle between progress bar view and radar chart view

### 4. Projects
Each project displayed as an interactive card with:
- Project title
- Short description
- Technologies used (tags/badges)
- GitHub repository link (opens in new tab)

**Projects to include:**
1. **AI Resume Analyzer Workflow** – n8n, webhooks, database integration; automated resume parsing and ATS analysis.
2. **Leave Management Automation System** – Telegram, Google Sheets, Gmail integration; automated leave request processing.
3. **AI Leave Management Chatbot** – Chatbot-based HR automation for employee leave applications.
4. **Python Analytics Portfolio** – Data structures, business analytics, inventory management, analytical problem solving.
5. **SQL Analytics Portfolio** – Joins, subqueries, CTEs, aggregations, window functions for business reporting.

### 5. Professional Experience
Timeline or card-based layout:
- **Business Operations Manager | Bhawani Supermart | 2020 – Present**
  - Scaled a family-owned retail grocery business from inception
  - Increased daily customer footfall from 250 to 400
  - Achieved ~75% growth in daily sales
  - Managed procurement, inventory, merchandising
  - Led a team of 5 employees
  - Implemented data-driven pricing and stock optimization strategies

- **Fresh Fruits & Vegetables Operations | 2023 – Present**
  - Established and managed a dedicated department
  - Tracked shelf life, spoilage rates, and inventory turnover
  - Optimized procurement costs and visual merchandising

### 6. Education
Vertical timeline or clean card layout:
- **B.E. (Electronics & Telecommunication)** – Ramrao Adik Institute of Technology, Mumbai University (2019)
- **HSC** – Swami Vivekanand High School (2015)
- **SSC** – Adarsha Vidyalaya School (2013)

### 7. Certifications
Badge-style or list layout:
- AI Fundamentals & Ecosystem Mastery – Be10X
- AI Product Building, Storytelling & Marketing – Be10X
- AI Agents & Autonomous Systems – Be10X
- Career Readiness Using AI – Be10X
- Data Analytics with AI & Generative AI – IIT Roorkee & Masai *(In Progress)*

### 8. Key Achievements
Highlighted metrics and milestones in a visually distinct section (icon + stat cards):
- Transitioned from business operations into Data Analytics and AI
- Built multiple GitHub projects in analytics, automation, and SQL
- Managed retail operations for 6+ years end-to-end
- Led growth initiatives improving customer acquisition and revenue

### 9. GitHub Section — Live Stats Dashboard
- Embedded GitHub profile link: [github.com/Narendrafulwaria](https://github.com/Narendrafulwaria)
- **Live GitHub Stats Dashboard** — auto-fetch data via the GitHub REST API (no auth required for public repos):
  - Total public repositories
  - Total stars received across all repos
  - Top programming languages used (displayed as a donut/bar chart using Plotly or Altair)
  - Most recent commit activity
- Display top repositories as interactive cards with description, language badge, and star count
- Data refreshes on each page load (live, not static snapshot)

### 10. LinkedIn Section
- Prominent LinkedIn button/card linking to his LinkedIn profile
- Short CTA: "Let's connect professionally"

### 11. Blog / Insights Section
- A dedicated section for short write-ups, learnings, and thought pieces
- **Content ideas:**
  - "What I learned building an AI Resume Analyzer"
  - "How n8n changed the way I think about automation"
  - "From Retail Manager to Data Analyst – My Transition Story"
- Each blog entry displayed as a card with title, short excerpt, date, and a "Read More" link
- Links can point to **LinkedIn articles** or **Medium posts** (external) or be rendered inline within Streamlit
- Placeholder cards shown initially; content added incrementally by Narendra

### 12. Interactive AI Chatbot — "Ask Narendra"
- An AI-powered chatbot embedded in the portfolio sidebar or a dedicated chat section
- Trained on Narendra's resume content — visitors can ask questions like:
  - "What projects has Narendra built?"
  - "What are his technical skills?"
  - "Is he available for hire?"
  - "What certifications does he have?"
- Powered by **OpenAI API (GPT-4o-mini)** or **Google Gemini API** with a system prompt built from resume content
- API key stored as a **Streamlit secret** (`st.secrets`) — not hardcoded
- Fallback: if no API key is configured, display a static FAQ section instead
- Chat history maintained within the session

### 13. Resume ATS Score Widget — Live Demo
- An interactive widget that **demonstrates the AI Resume Analyzer project in action**
- User flow:
  1. Visitor pastes a job description into a text area
  2. Clicks "Analyze Match"
  3. The widget scores how well Narendra's resume matches that job description
  4. Displays: match percentage, matched keywords, missing keywords, and a short recommendation
- Powered by keyword extraction + cosine similarity (using `sklearn` or `spacy`) — no external API needed for basic version; optionally enhanced with OpenAI for richer recommendations
- Clearly labeled as a **live demo of the AI Resume Analyzer project**
- Showcases Narendra's own project directly on his portfolio

### 14. Contact Section
- Contact form with fields: Name, Email, Message
- Direct email display
- Phone: 9833607051
- Location: Mumbai, Maharashtra
- Social links: GitHub, LinkedIn

### 15. Footer
- Copyright notice
- Quick navigation links
- Social media icons

---

## Technical Requirements

### Tech Stack
- **Python + Streamlit** — primary framework for building and deploying the portfolio
- **Streamlit Community Cloud** — deployment platform, auto-deploys from GitHub on push
- **HTML/CSS inside Streamlit** — via `st.markdown()` with `unsafe_allow_html=True` for custom styling
- **streamlit-extras**, **streamlit-lottie**, **streamlit-option-menu** — for enhanced UI components
- **Plotly / Altair** — for radar chart, skill progress visualization, and GitHub language charts
- **requests** — for live GitHub REST API calls
- **scikit-learn / spacy** — for ATS score keyword matching and cosine similarity
- **openai / google-generativeai** — for the "Ask Narendra" AI chatbot (key stored in `st.secrets`)
- **3D Profile Photo:** Implemented via an embedded Spline 3D scene (`spline.design`) or CSS 3D card tilt effect using `st.components.v1.html()`

### Design Requirements
- Clean, modern, professional aesthetic
- Color palette aligned with tech/analytics branding (e.g., deep blues, whites, accent colors)
- Smooth scroll behavior between sections
- Subtle animations on scroll (Lottie animations via `streamlit-lottie`)
- Consistent typography
- Dark/light mode toggle (optional but preferred)

### Performance & Accessibility
- Fast loading (optimized assets)
- Semantic structure within Streamlit layout
- Alt text on all images
- Meta tags for SEO (via `st.set_page_config`)

---

## Constraints & Assumptions

- Deployed on **Streamlit Community Cloud** connected to a GitHub repository
- LinkedIn URL to be added by Narendra (placeholder used during development)
- **3D profile photo** — a Spline-embedded 3D avatar or CSS 3D tilt card; actual photo provided by Narendra separately
- All GitHub project links are already available from the resume
- No paid hosting required — Streamlit Community Cloud is free for public repos
- **"Ask Narendra" chatbot** requires an OpenAI or Gemini API key stored in Streamlit secrets; a static FAQ fallback is shown if no key is configured
- **ATS Score Widget** uses offline keyword matching by default (no API key needed); OpenAI enhancement is optional
- **Blog section** uses placeholder cards initially; Narendra to provide actual article links over time
- **GitHub Stats Dashboard** uses public GitHub REST API (no token needed for public repos; rate-limited to 60 req/hr unauthenticated)

---

## Success Criteria

- [ ] All 15 sections implemented and fully responsive within Streamlit
- [ ] 3D profile photo effect working in Hero and About sections
- [ ] All 5 GitHub project links correctly linked
- [ ] Live GitHub Stats Dashboard fetching real data from GitHub API
- [ ] Animated skill progress bars and radar chart rendering correctly
- [ ] Blog / Insights section live with placeholder cards
- [ ] "Ask Narendra" AI chatbot responding correctly to resume-based questions
- [ ] Resume ATS Score Widget returning match score and keyword breakdown
- [ ] Deployed live on Streamlit Community Cloud via GitHub
- [ ] Lottie or CSS animations functional
- [ ] Contact form accessible and usable
- [ ] Resume download button works (PDF linked)
- [ ] API key for chatbot stored in Streamlit secrets (not hardcoded)
- [ ] Passes basic accessibility checks (contrast, keyboard navigation, alt text)
