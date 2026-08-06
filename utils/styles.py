import streamlit as st


def inject_css():
    """Inject all global custom CSS into the Streamlit app."""
    st.markdown(_CSS, unsafe_allow_html=True)


_CSS = """
<style>

/* ============================================================
   1. HIDE DEFAULT STREAMLIT CHROME
   ============================================================ */
#MainMenu { visibility: hidden; }
footer { visibility: hidden; }
header { visibility: hidden; }
.stDeployButton { display: none; }
[data-testid="stToolbar"] { display: none; }
[data-testid="stDecoration"] { display: none; }
[data-testid="stStatusWidget"] { display: none; }

/* Remove default top padding Streamlit adds */
.block-container {
    padding-top: 1rem;
    padding-bottom: 2rem;
    max-width: 1100px;
}

/* ============================================================
   2. GLOBAL TYPOGRAPHY & BODY
   ============================================================ */
html, body, [class*="css"] {
    font-family: 'Segoe UI', 'Inter', sans-serif;
    scroll-behavior: smooth;
}

h1 { font-size: 2.8rem !important; font-weight: 800 !important; line-height: 1.2; }
h2 { font-size: 2rem   !important; font-weight: 700 !important; }
h3 { font-size: 1.4rem !important; font-weight: 600 !important; }

/* Gradient text for hero name */
.gradient-text {
    background: linear-gradient(135deg, #2563EB 0%, #06B6D4 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
}

/* ============================================================
   3. SECTION ANCHORS — smooth-scroll offset
   ============================================================ */
.section-anchor {
    display: block;
    position: relative;
    top: -80px;
    visibility: hidden;
}

/* Section heading divider style */
.section-heading {
    font-size: 1.8rem;
    font-weight: 700;
    color: #F1F5F9;
    border-left: 4px solid #2563EB;
    padding-left: 0.75rem;
    margin-bottom: 1.5rem;
    margin-top: 0.5rem;
}

/* ============================================================
   4. CARD STYLES
   ============================================================ */
.portfolio-card {
    background: #1E293B;
    border: 1px solid #334155;
    border-radius: 12px;
    padding: 1.25rem 1.5rem;
    margin-bottom: 1rem;
    transition: transform 0.2s ease, box-shadow 0.2s ease, border-color 0.2s ease;
    height: 100%;
}

.portfolio-card:hover {
    transform: translateY(-4px);
    box-shadow: 0 8px 30px rgba(37, 99, 235, 0.25);
    border-color: #2563EB;
}

.card-title {
    font-size: 1.1rem;
    font-weight: 700;
    color: #F1F5F9;
    margin-bottom: 0.4rem;
}

.card-description {
    font-size: 0.9rem;
    color: #94A3B8;
    line-height: 1.6;
    margin-bottom: 0.75rem;
}

.card-date {
    font-size: 0.78rem;
    color: #64748B;
    margin-bottom: 0.5rem;
}

.card-link {
    display: inline-block;
    margin-top: 0.6rem;
    font-size: 0.85rem;
    font-weight: 600;
    color: #2563EB;
    text-decoration: none;
    transition: color 0.2s ease;
}

.card-link:hover { color: #06B6D4; text-decoration: underline; }

/* ============================================================
   5. BADGE / CHIP STYLES
   ============================================================ */
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
    background: rgba(37, 99, 235, 0.15);
    color: #93C5FD;
    border: 1px solid rgba(37, 99, 235, 0.35);
}

.badge-green {
    background: rgba(16, 185, 129, 0.15);
    color: #6EE7B7;
    border: 1px solid rgba(16, 185, 129, 0.35);
}

.badge-yellow {
    background: rgba(245, 158, 11, 0.15);
    color: #FCD34D;
    border: 1px solid rgba(245, 158, 11, 0.35);
}

.badge-purple {
    background: rgba(139, 92, 246, 0.15);
    color: #C4B5FD;
    border: 1px solid rgba(139, 92, 246, 0.35);
}

/* Skill category label */
.skill-category {
    font-size: 0.8rem;
    font-weight: 700;
    color: #64748B;
    text-transform: uppercase;
    letter-spacing: 0.08em;
    margin-top: 0.75rem;
    margin-bottom: 0.3rem;
}

/* ============================================================
   6. PROGRESS BAR STYLES (skill bars)
   ============================================================ */
.skill-bar-wrapper {
    margin-bottom: 0.9rem;
}

.skill-bar-label {
    display: flex;
    justify-content: space-between;
    font-size: 0.88rem;
    color: #CBD5E1;
    margin-bottom: 0.3rem;
    font-weight: 500;
}

.skill-bar-track {
    background: #334155;
    border-radius: 999px;
    height: 8px;
    overflow: hidden;
}

.skill-bar-fill {
    height: 100%;
    border-radius: 999px;
    background: linear-gradient(90deg, #2563EB, #06B6D4);
    animation: fillBar 1.2s ease forwards;
    width: 0%;
}

@keyframes fillBar {
    from { width: 0%; }
    to   { width: var(--fill-width); }
}

/* ============================================================
   7. TIMELINE STYLES
   ============================================================ */
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
    background: linear-gradient(180deg, #2563EB, #1E293B);
}

.timeline-item {
    position: relative;
    margin-bottom: 2rem;
}

.timeline-dot {
    position: absolute;
    left: -1.63rem;
    top: 0.3rem;
    width: 12px;
    height: 12px;
    border-radius: 50%;
    background: #2563EB;
    border: 2px solid #0F172A;
    box-shadow: 0 0 0 3px rgba(37, 99, 235, 0.3);
}

.timeline-role {
    font-size: 1.05rem;
    font-weight: 700;
    color: #F1F5F9;
}

.timeline-company {
    font-size: 0.9rem;
    color: #2563EB;
    font-weight: 600;
    margin-bottom: 0.2rem;
}

.timeline-period {
    display: inline-block;
    font-size: 0.75rem;
    color: #94A3B8;
    background: #1E293B;
    border: 1px solid #334155;
    border-radius: 999px;
    padding: 0.15rem 0.6rem;
    margin-bottom: 0.6rem;
}

.timeline-bullets {
    padding-left: 1.1rem;
    margin: 0;
}

.timeline-bullets li {
    font-size: 0.88rem;
    color: #94A3B8;
    margin-bottom: 0.3rem;
    line-height: 1.55;
}

/* ============================================================
   8. BUTTON OVERRIDES
   ============================================================ */
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
    opacity: 0.9 !important;
    transform: translateY(-1px) !important;
}

/* Download button — cyan accent */
.stDownloadButton > button {
    background: linear-gradient(135deg, #0891B2, #06B6D4) !important;
    color: #FFFFFF !important;
    border: none !important;
    border-radius: 8px !important;
    font-weight: 600 !important;
}

/* ============================================================
   9. METRIC / ACHIEVEMENT CARDS
   ============================================================ */
.achievement-card {
    background: #1E293B;
    border: 1px solid #334155;
    border-radius: 12px;
    padding: 1.25rem;
    text-align: center;
    transition: transform 0.2s ease, box-shadow 0.2s ease;
}

.achievement-card:hover {
    transform: translateY(-3px);
    box-shadow: 0 6px 24px rgba(37, 99, 235, 0.2);
}

.achievement-icon  { font-size: 2rem; margin-bottom: 0.4rem; }
.achievement-value { font-size: 1.8rem; font-weight: 800; color: #2563EB; }
.achievement-label { font-size: 0.85rem; color: #94A3B8; font-weight: 500; margin-top: 0.2rem; }
.achievement-detail { font-size: 0.75rem; color: #64748B; margin-top: 0.3rem; line-height: 1.4; }

/* ============================================================
   10. CERT BADGE CARD
   ============================================================ */
.cert-card {
    background: #1E293B;
    border: 1px solid #334155;
    border-radius: 10px;
    padding: 1rem 1.25rem;
    margin-bottom: 0.75rem;
    display: flex;
    align-items: flex-start;
    gap: 0.75rem;
    transition: border-color 0.2s ease;
}

.cert-card:hover { border-color: #2563EB; }
.cert-icon  { font-size: 1.5rem; flex-shrink: 0; }
.cert-name  { font-size: 0.95rem; font-weight: 600; color: #F1F5F9; }
.cert-issuer { font-size: 0.8rem; color: #64748B; margin-top: 0.1rem; }

/* ============================================================
   11. CONTACT SECTION
   ============================================================ */
.contact-info-row {
    display: flex;
    align-items: center;
    gap: 0.6rem;
    font-size: 0.9rem;
    color: #94A3B8;
    margin-bottom: 0.6rem;
}

.contact-info-row a {
    color: #2563EB;
    text-decoration: none;
    font-weight: 500;
}

.contact-info-row a:hover { color: #06B6D4; }

/* ============================================================
   12. FOOTER
   ============================================================ */
.footer-container {
    text-align: center;
    padding: 2rem 0 1rem;
    border-top: 1px solid #1E293B;
    margin-top: 2rem;
    color: #64748B;
    font-size: 0.82rem;
}

.footer-links {
    display: flex;
    justify-content: center;
    gap: 1.5rem;
    margin: 0.75rem 0;
}

.footer-links a {
    color: #94A3B8;
    text-decoration: none;
    font-size: 0.82rem;
    transition: color 0.2s ease;
}

.footer-links a:hover { color: #2563EB; }

/* ============================================================
   13. RESPONSIVE COLUMN GAPS
   ============================================================ */
[data-testid="column"] { gap: 1rem; }

@media (max-width: 768px) {
    .block-container { padding-left: 1rem; padding-right: 1rem; }
    h1 { font-size: 2rem !important; }
    .portfolio-card { padding: 1rem; }
    .timeline-container { padding-left: 1.5rem; }
}

/* ============================================================
   14. ATS WIDGET
   ============================================================ */
.ats-score-display {
    text-align: center;
    padding: 1.5rem;
    border-radius: 12px;
    background: #1E293B;
    border: 1px solid #334155;
    margin-bottom: 1rem;
}

.ats-score-number {
    font-size: 3.5rem;
    font-weight: 900;
    line-height: 1;
}

.ats-score-high   { color: #10B981; }
.ats-score-medium { color: #F59E0B; }
.ats-score-low    { color: #EF4444; }

.ats-keyword-box {
    background: #1E293B;
    border: 1px solid #334155;
    border-radius: 10px;
    padding: 1rem;
}

.ats-keyword-title {
    font-size: 0.85rem;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.06em;
    margin-bottom: 0.6rem;
    color: #94A3B8;
}

/* ============================================================
   15. CHATBOT SECTION
   ============================================================ */
.chatbot-intro {
    background: #1E293B;
    border-left: 4px solid #2563EB;
    border-radius: 0 8px 8px 0;
    padding: 0.75rem 1rem;
    color: #94A3B8;
    font-size: 0.88rem;
    margin-bottom: 1rem;
}

/* ============================================================
   16. SCROLLBAR STYLING
   ============================================================ */
::-webkit-scrollbar       { width: 6px; }
::-webkit-scrollbar-track { background: #0F172A; }
::-webkit-scrollbar-thumb { background: #334155; border-radius: 3px; }
::-webkit-scrollbar-thumb:hover { background: #2563EB; }

</style>
"""
