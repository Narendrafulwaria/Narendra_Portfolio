import streamlit as st


def inject_css():
    """Inject all global custom CSS into the Streamlit app."""
    st.markdown(_CSS, unsafe_allow_html=True)


def section_start(variant: str = "light") -> None:
    """Open a visually distinct section panel."""
    variants = {
        "light": "section-block",
        "blue": "section-block section-block--blue",
        "bold": "section-block section-block--bold",
    }
    css_class = variants.get(variant, "section-block")
    st.markdown(f'<div class="{css_class}">', unsafe_allow_html=True)


def section_end() -> None:
    """Close a section panel opened with section_start."""
    st.markdown("</div>", unsafe_allow_html=True)


_CSS = """
<style>

/* ============================================================
   0. LIGHT THEME — WHITE, BLACK & BLUE
   ============================================================ */
:root {
    --bg-primary:     #FFFFFF;
    --bg-secondary:   #F8FAFC;
    --bg-blue-tint:   #EFF6FF;
    --bg-card:        #FFFFFF;
    --border:         #E2E8F0;
    --border-blue:    #BFDBFE;
    --text-primary:   #0F172A;
    --text-secondary: #1E293B;
    --text-muted:     #475569;
    --text-dim:       #64748B;
    --accent:         #2563EB;
    --accent-dark:    #1D4ED8;
    --accent-light:   #3B82F6;
    --accent-soft:    #93C5FD;
    --shadow:         rgba(15, 23, 42, 0.08);
    --shadow-blue:    rgba(37, 99, 235, 0.15);
}

#MainMenu { visibility: hidden; }
footer { visibility: hidden; }
header { visibility: hidden; }
.stDeployButton { display: none; }
[data-testid="stToolbar"] { display: none; }
[data-testid="stDecoration"] { display: none; }
[data-testid="stStatusWidget"] { display: none; }

.stApp {
    background: var(--bg-primary);
}

.block-container {
    padding-top: 0.75rem;
    padding-bottom: 2rem;
    max-width: min(96vw, 1560px);
}

@media (orientation: landscape) {
    .block-container {
        max-width: min(98vw, 1680px);
        padding-left: 2.5rem;
        padding-right: 2.5rem;
    }
}

@media (min-width: 1200px) {
    .block-container { max-width: min(97vw, 1720px); }
    [data-testid="column"] { gap: 1.35rem; }
}

html, body, [class*="css"] {
    font-family: 'Segoe UI', 'Inter', sans-serif;
    scroll-behavior: smooth;
    color: var(--text-secondary);
}

h1 { font-size: 2.8rem !important; font-weight: 800 !important; line-height: 1.2; color: var(--text-primary) !important; }
h2 { font-size: 2rem   !important; font-weight: 700 !important; color: var(--text-primary) !important; }
h3 { font-size: 1.4rem !important; font-weight: 600 !important; color: var(--text-primary) !important; }

.gradient-text {
    background: linear-gradient(135deg, #0F172A 0%, #2563EB 55%, #1D4ED8 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
}

#home, #about, #skills, #projects, #experience, #education,
#certifications, #github, #blog, #chatbot, #ats, #contact {
    scroll-margin-top: 80px;
}

.section-block {
    background: var(--bg-card);
    border: 1px solid var(--border);
    border-radius: 16px;
    padding: 1.5rem 1.75rem;
    margin: 0.5rem 0 1.25rem;
    box-shadow: 0 4px 18px var(--shadow);
}

.section-block--blue {
    background: linear-gradient(180deg, #FFFFFF 0%, var(--bg-blue-tint) 100%);
    border-color: var(--border-blue);
    box-shadow: 0 6px 22px var(--shadow-blue);
}

.section-block--bold {
    background: linear-gradient(135deg, #DBEAFE 0%, #BFDBFE 45%, #93C5FD 100%);
    border: 2px solid #2563EB;
    box-shadow: 0 12px 36px rgba(37, 99, 235, 0.28);
}

.section-heading {
    font-size: 1.8rem;
    font-weight: 700;
    color: var(--text-primary);
    border-left: 4px solid var(--accent);
    background: linear-gradient(90deg, var(--bg-blue-tint) 0%, transparent 100%);
    padding: 0.5rem 0 0.5rem 0.75rem;
    margin-bottom: 1.5rem;
    margin-top: 0.25rem;
    border-radius: 0 8px 8px 0;
}

.section-heading--bold {
    font-size: 2rem;
    font-weight: 800;
    color: #0F172A;
    border-left: 5px solid #1D4ED8;
    background: rgba(255, 255, 255, 0.72);
    box-shadow: 0 2px 10px rgba(37, 99, 235, 0.12);
}

.section-cta-row {
    display: flex;
    gap: 0.75rem;
    flex-wrap: wrap;
    margin-top: 1.25rem;
}

.section-cta-link {
    display: inline-flex;
    align-items: center;
    gap: 0.35rem;
    padding: 0.55rem 1.15rem;
    border-radius: 8px;
    font-size: 0.9rem;
    font-weight: 700;
    text-decoration: none;
    color: #1D4ED8;
    background: #FFFFFF;
    border: 2px solid #2563EB;
    transition: transform 0.15s ease, box-shadow 0.15s ease, background 0.15s ease;
}

.section-cta-link:hover {
    transform: translateY(-2px);
    box-shadow: 0 6px 16px rgba(37, 99, 235, 0.25);
    background: #EFF6FF;
}

.section-cta-link--primary {
    background: linear-gradient(135deg, #2563EB, #1D4ED8);
    color: #FFFFFF;
    border-color: #1D4ED8;
}

.section-cta-link--primary:hover {
    background: linear-gradient(135deg, #1D4ED8, #1E40AF);
    color: #FFFFFF;
}

.stat-link {
    text-decoration: none;
    color: inherit;
    display: block;
    padding: 0.35rem 0.5rem;
    border-radius: 10px;
    transition: background 0.15s ease, transform 0.15s ease;
}

.stat-link:hover {
    background: rgba(37, 99, 235, 0.1);
    transform: translateY(-2px);
}

.hero-cta-row {
    display: flex;
    gap: 0.5rem;
    flex-wrap: wrap;
    margin-bottom: 0.25rem;
}

.hero-cta-btn,
a.hero-cta-btn,
[data-testid="stMarkdown"] a.hero-cta-btn,
[data-testid="stMarkdownContainer"] a.hero-cta-btn {
    flex: 1;
    min-width: 0;
    width: 100%;
    min-height: 42px;
    display: inline-flex;
    align-items: center;
    justify-content: center;
    padding: 0.55rem 0.75rem;
    border-radius: 8px;
    font-size: 0.9rem;
    font-weight: 600;
    text-decoration: none !important;
    text-align: center;
    box-sizing: border-box;
    color: #FFFFFF !important;
    -webkit-text-fill-color: #FFFFFF !important;
    background: linear-gradient(135deg, #1E40AF, #2563EB);
    border: none;
    transition: opacity 0.15s ease, transform 0.1s ease;
}

.hero-cta-btn:hover,
a.hero-cta-btn:hover,
a.hero-cta-btn:visited,
a.hero-cta-btn:active,
a.hero-cta-btn:link {
    opacity: 0.92;
    transform: translateY(-1px);
    color: #FFFFFF !important;
    -webkit-text-fill-color: #FFFFFF !important;
    text-decoration: none !important;
}

.hero-cta-btn--outline {
    background: #FFFFFF;
    color: #1D4ED8;
    border: 2px solid #2563EB;
}

.hero-cta-btn--outline:hover {
    background: #EFF6FF;
    color: #1D4ED8;
}

.about-cta-row {
    margin-top: 1.5rem;
}

.cta-btn-row [data-testid="column"] {
    display: flex;
    flex-direction: column;
    justify-content: stretch;
}

.cta-btn-row .stDownloadButton,
.cta-btn-row .stButton {
    width: 100%;
}

.cta-btn-row .stDownloadButton > button,
.cta-btn-row .stButton > button {
    width: 100% !important;
    min-height: 42px !important;
}

.portfolio-card,
.repo-card {
    background: var(--bg-card);
    border: 1px solid var(--border-blue);
    border-radius: 12px;
    padding: 1.25rem 1.5rem;
    margin-bottom: 1rem;
    transition: transform 0.2s ease, box-shadow 0.2s ease, border-color 0.2s ease;
    height: 100%;
    box-shadow: 0 2px 10px var(--shadow);
}

.portfolio-card:hover,
.repo-card:hover {
    transform: translateY(-4px);
    box-shadow: 0 10px 28px var(--shadow-blue);
    border-color: var(--accent-light);
}

.card-title,
.repo-name {
    font-size: 1.1rem;
    font-weight: 700;
    color: var(--text-primary);
    margin-bottom: 0.4rem;
}

.card-description,
.repo-description {
    font-size: 0.9rem;
    color: var(--text-muted);
    line-height: 1.6;
    margin-bottom: 0.75rem;
}

.card-date {
    font-size: 0.78rem;
    color: var(--text-dim);
    margin-bottom: 0.5rem;
}

.card-link {
    display: inline-block;
    margin-top: 0.6rem;
    font-size: 0.85rem;
    font-weight: 600;
    color: var(--accent);
    text-decoration: none;
    transition: color 0.2s ease;
}

.card-link:hover { color: var(--accent-dark); text-decoration: underline; }

.badge-container {
    display: flex;
    flex-wrap: wrap;
    gap: 0.4rem;
    margin-top: 0.5rem;
}

.badge {
    display: inline-block;
    padding: 0.25rem 0.65rem;
    border-radius: 999px;
    font-size: 0.75rem;
    font-weight: 600;
    background: var(--bg-blue-tint);
    color: var(--accent-dark);
    border: 1px solid var(--border-blue);
}

.badge-green,
.badge-yellow,
.badge-purple {
    background: var(--bg-blue-tint);
    color: var(--accent-dark);
    border: 1px solid var(--border-blue);
}

.skill-category {
    font-size: 0.8rem;
    font-weight: 700;
    color: var(--accent-dark);
    text-transform: uppercase;
    letter-spacing: 0.08em;
    margin-top: 0.75rem;
    margin-bottom: 0.3rem;
}

.skill-bar-wrapper { margin-bottom: 0.9rem; }

.skill-bar-label {
    display: flex;
    justify-content: space-between;
    font-size: 0.88rem;
    color: var(--text-secondary);
    margin-bottom: 0.3rem;
    font-weight: 500;
}

.skill-bar-track {
    background: #E2E8F0;
    border-radius: 999px;
    height: 8px;
    overflow: hidden;
}

.skill-bar-fill {
    height: 100%;
    border-radius: 999px;
    background: linear-gradient(90deg, #2563EB, #3B82F6);
    animation: fillBar 1.2s ease forwards;
    width: 0%;
}

@keyframes fillBar {
    from { width: 0%; }
    to   { width: var(--fill-width); }
}

.timeline-container {
    position: relative;
    padding-left: 2rem;
    margin-top: 1rem;
}

.timeline-container::before {
    content: '';
    position: absolute;
    left: 0.45rem;
    top: 0;
    bottom: 0;
    width: 2px;
    background: linear-gradient(180deg, #2563EB, #BFDBFE);
}

.timeline-item { position: relative; margin-bottom: 2rem; }

.timeline-dot {
    position: absolute;
    left: -1.63rem;
    top: 0.3rem;
    width: 12px;
    height: 12px;
    border-radius: 50%;
    background: var(--accent);
    border: 2px solid var(--bg-primary);
    box-shadow: 0 0 0 3px rgba(37, 99, 235, 0.2);
}

.timeline-role {
    font-size: 1.05rem;
    font-weight: 700;
    color: var(--text-primary);
}

.timeline-company {
    font-size: 0.9rem;
    color: var(--accent);
    font-weight: 600;
    margin-bottom: 0.2rem;
}

.timeline-period {
    display: inline-block;
    font-size: 0.75rem;
    color: var(--text-muted);
    background: var(--bg-blue-tint);
    border: 1px solid var(--border-blue);
    border-radius: 999px;
    padding: 0.15rem 0.6rem;
    margin-bottom: 0.6rem;
}

.timeline-bullets { padding-left: 1.1rem; margin: 0; }

.timeline-bullets li {
    font-size: 0.88rem;
    color: var(--text-muted);
    margin-bottom: 0.3rem;
    line-height: 1.55;
}

.stButton > button {
    background: linear-gradient(135deg, #2563EB, #1D4ED8) !important;
    color: #FFFFFF !important;
    border: none !important;
    border-radius: 8px !important;
    padding: 0.5rem 1.4rem !important;
    font-weight: 600 !important;
    font-size: 0.9rem !important;
    transition: opacity 0.2s ease, transform 0.1s ease !important;
    cursor: pointer !important;
}

.stButton > button:hover {
    opacity: 0.92 !important;
    transform: translateY(-1px) !important;
}

.stDownloadButton > button {
    background: linear-gradient(135deg, #1E40AF, #2563EB) !important;
    color: #FFFFFF !important;
    border: none !important;
    border-radius: 8px !important;
    font-weight: 600 !important;
}

.achievement-card {
    background: var(--bg-card);
    border: 1px solid var(--border-blue);
    border-radius: 12px;
    padding: 1.25rem;
    text-align: center;
    transition: transform 0.2s ease, box-shadow 0.2s ease;
    box-shadow: 0 2px 10px var(--shadow);
}

.achievement-card:hover {
    transform: translateY(-3px);
    box-shadow: 0 8px 24px var(--shadow-blue);
    border-color: var(--accent-light);
}

.achievement-icon  { font-size: 2rem; margin-bottom: 0.4rem; }
.achievement-value { font-size: 1.8rem; font-weight: 800; color: var(--accent); }
.achievement-label { font-size: 0.85rem; color: var(--text-muted); font-weight: 500; margin-top: 0.2rem; }
.achievement-detail { font-size: 0.75rem; color: var(--text-dim); margin-top: 0.3rem; line-height: 1.4; }

.cert-card {
    background: var(--bg-card);
    border: 1px solid var(--border-blue);
    border-radius: 10px;
    padding: 1rem 1.25rem;
    margin-bottom: 0.75rem;
    display: flex;
    align-items: flex-start;
    gap: 0.75rem;
    transition: border-color 0.2s ease, box-shadow 0.2s ease;
    height: 100%;
    box-shadow: 0 2px 8px var(--shadow);
}

.cert-card:hover {
    border-color: var(--accent-light);
    box-shadow: 0 6px 18px var(--shadow-blue);
}

.cert-icon  { font-size: 1.5rem; flex-shrink: 0; }
.cert-name  { font-size: 0.95rem; font-weight: 600; color: var(--text-primary); }
.cert-issuer { font-size: 0.8rem; color: var(--text-dim); margin-top: 0.1rem; }

.contact-info-row {
    display: flex;
    align-items: center;
    gap: 0.6rem;
    font-size: 0.9rem;
    color: var(--text-muted);
    margin-bottom: 0.6rem;
}

.contact-info-row a {
    color: var(--accent);
    text-decoration: none;
    font-weight: 500;
}

.contact-info-row a:hover { color: var(--accent-dark); }

[data-testid="column"] { gap: 1rem; }

@media (max-width: 768px) {
    .block-container { padding-left: 1rem; padding-right: 1rem; }
    h1 { font-size: 2rem !important; }
    .portfolio-card { padding: 1rem; }
    .timeline-container { padding-left: 1.5rem; }
    .section-block { padding: 1rem 1.1rem; }
}

.ats-score-display {
    text-align: center;
    padding: 1.5rem;
    border-radius: 12px;
    background: var(--bg-blue-tint);
    border: 1px solid var(--border-blue);
    margin-bottom: 1rem;
}

.ats-score-number { font-size: 3.5rem; font-weight: 900; line-height: 1; }
.ats-score-high   { color: #16A34A; }
.ats-score-medium { color: #2563EB; }
.ats-score-low    { color: #DC2626; }

.ats-keyword-box {
    background: var(--bg-card);
    border: 1px solid var(--border-blue);
    border-radius: 10px;
    padding: 1rem;
}

.ats-keyword-title {
    font-size: 0.85rem;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.06em;
    margin-bottom: 0.6rem;
    color: var(--text-muted);
}

.chatbot-intro {
    background: rgba(255, 255, 255, 0.88);
    border-left: 4px solid var(--accent-dark);
    border-radius: 0 8px 8px 0;
    padding: 0.75rem 1rem;
    color: #1E293B;
    font-size: 0.9rem;
    font-weight: 500;
    margin-bottom: 1rem;
}

.section-block--bold .chatbot-intro {
    background: rgba(255, 255, 255, 0.92);
    border-left-width: 5px;
    color: #0F172A;
    font-weight: 600;
}

.chatbot-empty-state {
    color: #334155;
    font-size: 0.9rem;
    font-weight: 500;
    text-align: center;
    padding: 2.5rem 1rem;
    border: 2px dashed #2563EB;
    border-radius: 12px;
    background: rgba(255, 255, 255, 0.9);
}

.section-block--bold .contact-lead {
    color: #0F172A !important;
    font-weight: 600 !important;
}

.section-block--bold .contact-detail {
    color: #1E293B !important;
    font-weight: 600 !important;
}

.section-block--bold .contact-social-link {
    color: #1D4ED8 !important;
    font-weight: 700 !important;
}

.robot-panel {
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 0.75rem;
    padding: 1rem 0.5rem;
}

.robot-avatar {
    position: relative;
    width: 150px;
    height: 190px;
    margin: 0 auto 0.5rem;
    animation: robot-float 3s ease-in-out infinite;
}

@keyframes robot-float {
    0%, 100% { transform: translateY(0); }
    50% { transform: translateY(-8px); }
}

.robot-antenna {
    position: absolute;
    top: 0;
    left: 50%;
    transform: translateX(-50%);
    width: 4px;
    height: 22px;
    background: #94A3B8;
    border-radius: 2px;
}

.robot-antenna::after {
    content: "";
    position: absolute;
    top: -8px;
    left: 50%;
    transform: translateX(-50%);
    width: 10px;
    height: 10px;
    background: var(--accent);
    border-radius: 50%;
    box-shadow: 0 0 12px rgba(37, 99, 235, 0.5);
    animation: robot-blink-light 1.5s ease-in-out infinite;
}

@keyframes robot-blink-light {
    0%, 100% { opacity: 1; }
    50% { opacity: 0.4; }
}

.robot-head {
    position: absolute;
    top: 24px;
    left: 50%;
    transform: translateX(-50%);
    width: 88px;
    height: 72px;
    background: linear-gradient(145deg, #E2E8F0, #CBD5E1);
    border: 2px solid var(--border-blue);
    border-radius: 18px;
    box-shadow: 0 8px 24px var(--shadow-blue);
}

.robot-eye {
    position: absolute;
    top: 22px;
    width: 14px;
    height: 14px;
    background: var(--accent);
    border-radius: 50%;
    box-shadow: 0 0 8px rgba(37, 99, 235, 0.5);
    animation: robot-blink 4s ease-in-out infinite;
}

.robot-eye.left  { left: 18px; }
.robot-eye.right { right: 18px; }

@keyframes robot-blink {
    0%, 92%, 100% { transform: scaleY(1); }
    95% { transform: scaleY(0.1); }
}

.robot-mouth {
    position: absolute;
    bottom: 14px;
    left: 50%;
    transform: translateX(-50%);
    width: 28px;
    height: 8px;
    border: 2px solid var(--text-muted);
    border-top: none;
    border-radius: 0 0 12px 12px;
}

.robot-neck {
    position: absolute;
    top: 94px;
    left: 50%;
    transform: translateX(-50%);
    width: 24px;
    height: 12px;
    background: #94A3B8;
    border-radius: 4px;
}

.robot-body {
    position: absolute;
    top: 104px;
    left: 50%;
    transform: translateX(-50%);
    width: 100px;
    height: 72px;
    background: linear-gradient(160deg, #1E40AF, #2563EB);
    border: 2px solid var(--accent-dark);
    border-radius: 16px;
}

.robot-core {
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    width: 28px;
    height: 28px;
    background: radial-gradient(circle, #FFFFFF 0%, #93C5FD 70%);
    border-radius: 50%;
    box-shadow: 0 0 16px rgba(37, 99, 235, 0.6);
    animation: robot-pulse 2s ease-in-out infinite;
}

@keyframes robot-pulse {
    0%, 100% { transform: translate(-50%, -50%) scale(1); }
    50% { transform: translate(-50%, -50%) scale(1.15); }
}

.robot-light {
    position: absolute;
    bottom: 10px;
    left: 50%;
    transform: translateX(-50%);
    width: 40px;
    height: 4px;
    background: #93C5FD;
    border-radius: 2px;
    opacity: 0.9;
}

.robot-arm {
    position: absolute;
    top: 112px;
    width: 16px;
    height: 48px;
    background: #CBD5E1;
    border: 2px solid #94A3B8;
    border-radius: 8px;
}

.robot-arm.left {
    left: 8px;
    transform: rotate(18deg);
    transform-origin: top center;
    animation: robot-wave-left 2.5s ease-in-out infinite;
}

.robot-arm.right {
    right: 8px;
    transform: rotate(-18deg);
    transform-origin: top center;
    animation: robot-wave-right 2.5s ease-in-out infinite;
}

@keyframes robot-wave-left {
    0%, 100% { transform: rotate(18deg); }
    50% { transform: rotate(28deg); }
}

@keyframes robot-wave-right {
    0%, 100% { transform: rotate(-18deg); }
    50% { transform: rotate(-28deg); }
}

.robot-speech-bubble {
    background: var(--bg-card);
    border: 1px solid var(--border-blue);
    border-radius: 14px;
    padding: 0.65rem 0.9rem;
    color: var(--text-secondary);
    font-size: 0.82rem;
    text-align: center;
    max-width: 220px;
    position: relative;
}

.robot-speech-bubble::before {
    content: "";
    position: absolute;
    top: -8px;
    left: 50%;
    transform: translateX(-50%);
    border-left: 8px solid transparent;
    border-right: 8px solid transparent;
    border-bottom: 8px solid var(--border-blue);
}

.robot-quick-label {
    color: var(--text-dim);
    font-size: 0.78rem;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 0.05em;
    margin: 0.5rem 0 0.25rem;
    text-align: center;
}

div[data-testid="column"]:has(.robot-panel) button[kind="primary"] {
    background: linear-gradient(135deg, #2563EB, #1D4ED8) !important;
    border: none !important;
    font-weight: 600 !important;
    color: #FFFFFF !important;
}

div[data-testid="column"]:has(.robot-panel) button:not([kind="primary"]) {
    background: var(--bg-card) !important;
    border: 1px solid var(--border-blue) !important;
    color: var(--text-secondary) !important;
    font-size: 0.82rem !important;
    text-align: left !important;
}

div[data-testid="column"]:has(.robot-panel) button:not([kind="primary"]):hover {
    border-color: var(--accent) !important;
    color: var(--accent-dark) !important;
}

::-webkit-scrollbar       { width: 6px; }
::-webkit-scrollbar-track { background: #F1F5F9; }
::-webkit-scrollbar-thumb { background: #CBD5E1; border-radius: 3px; }
::-webkit-scrollbar-thumb:hover { background: #2563EB; }

hr { border-color: var(--border) !important; }

[data-testid="stMetric"] {
    background: var(--bg-blue-tint);
    border: 1px solid var(--border-blue);
    border-radius: 10px;
    padding: 0.75rem 1rem;
}

[data-testid="stMetricValue"] {
    color: var(--accent) !important;
}

[data-testid="stMetricLabel"] {
    color: var(--text-muted) !important;
}

</style>
"""
