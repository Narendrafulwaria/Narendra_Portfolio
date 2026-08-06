# sections/ats_widget.py — Section 13: Resume ATS Score Widget
import streamlit as st
from utils.ats_scorer import score_resume
from utils.data import RESUME_TEXT


def render_ats_widget():
    st.markdown('<div id="ats"></div>', unsafe_allow_html=True)
    st.markdown('<div class="section-heading">Resume ATS Match Tool 🎯</div>', unsafe_allow_html=True)

    st.markdown(
        """
        <p style="color:#94A3B8;font-size:0.95rem;margin-bottom:1.5rem;">
            Paste any job description to see how well Narendra's resume matches it.
        </p>
        """,
        unsafe_allow_html=True,
    )

    # ── Job description input ─────────────────────────────────────────────
    job_description = st.text_area(
        "Job Description",
        height=200,
        placeholder="Paste the job description here...",
        key="ats_jd_input",
    )

    # ── Analyze button ─────────────────────────────────────────────────────
    col1, col2 = st.columns([1, 4], gap="small")

    with col1:
        analyze_clicked = st.button("Analyze Match", key="ats_analyze", use_container_width=True)

    with col2:
        if st.button("Clear", key="ats_clear", use_container_width=True):
            st.session_state["ats_result"] = None
            st.rerun()

    # ── Perform analysis ───────────────────────────────────────────────────
    if analyze_clicked and job_description.strip():
        with st.spinner("Analyzing match..."):
            result = score_resume(job_description, RESUME_TEXT)
            st.session_state["ats_result"] = result

    # ── Display results ───────────────────────────────────────────────────
    if st.session_state.get("ats_result"):
        result = st.session_state["ats_result"]
        score = result["score"]
        matched = result["matched_keywords"]
        missing = result["missing_keywords"]
        recommendation = result["recommendation"]

        # Score display with color
        score_color = "#10B981" if score >= 80 else "#F59E0B" if score >= 60 else "#EF4444"

        st.markdown(
            f"""
            <div style="text-align:center;margin:1.5rem 0;">
                <div style="font-size:0.9rem;color:#64748B;margin-bottom:0.5rem;">Match Score</div>
                <div style="font-size:3rem;font-weight:800;color:{score_color};">{score}%</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

        # Progress bar
        st.progress(score / 100)

        st.markdown("<br>", unsafe_allow_html=True)

        # Keywords columns
        kw1, kw2 = st.columns(2, gap="medium")

        with kw1:
            st.markdown(
                '<p style="color:#10B981;font-weight:600;font-size:0.9rem;margin-bottom:0.5rem;">✅ Matched Keywords</p>',
                unsafe_allow_html=True,
            )
            if matched:
                badges = "".join(
                    f'<span style="display:inline-block;padding:0.25rem 0.6rem;'
                    f'background:rgba(16,185,129,0.15);border:1px solid rgba(16,185,129,0.35);'
                    f'border-radius:999px;color:#6EE7B7;font-size:0.75rem;margin-right:0.3rem;margin-bottom:0.3rem;">'
                    f'{kw.replace("&", "&amp;").replace("<", "&lt;")}</span>'
                    for kw in matched
                )
                st.markdown(f'<div>{badges}</div>', unsafe_allow_html=True)
            else:
                st.markdown('<p style="color:#64748B;font-size:0.85rem;">No matched keywords found.</p>', unsafe_allow_html=True)

        with kw2:
            st.markdown(
                '<p style="color:#EF4444;font-weight:600;font-size:0.9rem;margin-bottom:0.5rem;">❌ Missing Keywords</p>',
                unsafe_allow_html=True,
            )
            if missing:
                badges = "".join(
                    f'<span style="display:inline-block;padding:0.25rem 0.6rem;'
                    f'background:rgba(239,68,68,0.15);border:1px solid rgba(239,68,68,0.35);'
                    f'border-radius:999px;color:#FCA5A5;font-size:0.75rem;margin-right:0.3rem;margin-bottom:0.3rem;">'
                    f'{kw.replace("&", "&amp;").replace("<", "&lt;")}</span>'
                    for kw in missing
                )
                st.markdown(f'<div>{badges}</div>', unsafe_allow_html=True)
            else:
                st.markdown('<p style="color:#64748B;font-size:0.85rem;">No missing keywords.</p>', unsafe_allow_html=True)

        # Recommendation
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown(
            f"""
            <div style="background:rgba(37,99,235,0.1);border:1px solid rgba(37,99,235,0.3);
                 border-radius:8px;padding:1rem;margin-top:1rem;">
                <p style="color:#93C5FD;font-size:0.9rem;line-height:1.6;">
                    💡 <strong>Recommendation:</strong> {recommendation.replace("&", "&amp;").replace("<", "&lt;")}
                </p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.markdown("<hr style='border-color:#1E293B;margin:2rem 0;'>", unsafe_allow_html=True)
