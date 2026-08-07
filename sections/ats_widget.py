# sections/ats_widget.py — Section 13: Resume ATS Score Widget
import streamlit as st
from utils.ats_scorer import score_resume
from utils.data import RESUME_TEXT
from utils.styles import section_start, section_end


def render_ats_widget():
    st.markdown('<div id="ats"></div>', unsafe_allow_html=True)
    section_start("light")
    st.markdown('<div class="section-heading">Resume ATS Match Tool 🎯</div>', unsafe_allow_html=True)

    st.markdown(
        """
        <p style="color:#475569;font-size:0.95rem;margin-bottom:1.5rem;">
            Paste any job description to see how well Narendra's resume matches it.
        </p>
        """,
        unsafe_allow_html=True,
    )

    job_description = st.text_area(
        "Job Description",
        height=200,
        placeholder="Paste the job description here...",
        key="ats_jd_input",
    )

    col1, col2 = st.columns([1, 4], gap="small")

    with col1:
        analyze_clicked = st.button("Analyze Match", key="ats_analyze", width='stretch')

    with col2:
        if st.button("Clear", key="ats_clear", width='stretch'):
            st.session_state["ats_result"] = None
            st.rerun()

    if analyze_clicked and job_description.strip():
        with st.spinner("Analyzing match..."):
            result = score_resume(job_description, RESUME_TEXT)
            st.session_state["ats_result"] = result

    if st.session_state.get("ats_result"):
        result = st.session_state["ats_result"]
        score = result["score"]
        matched = result["matched_keywords"]
        missing = result["missing_keywords"]
        recommendation = result["recommendation"]

        score_color = "#16A34A" if score >= 80 else "#2563EB" if score >= 60 else "#DC2626"

        st.markdown(
            f"""
            <div style="text-align:center;margin:1.5rem 0;">
                <div style="font-size:0.9rem;color:#64748B;margin-bottom:0.5rem;">Match Score</div>
                <div style="font-size:3rem;font-weight:800;color:{score_color};">{score}%</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

        st.progress(score / 100)
        st.markdown("<br>", unsafe_allow_html=True)

        kw1, kw2 = st.columns(2, gap="medium")

        with kw1:
            st.markdown(
                '<p style="color:#166534;font-weight:600;font-size:0.9rem;margin-bottom:0.5rem;">✅ Matched Keywords</p>',
                unsafe_allow_html=True,
            )
            if matched:
                badges = "".join(
                    f'<span style="display:inline-block;padding:0.25rem 0.6rem;'
                    f'background:#DCFCE7;border:1px solid #86EFAC;'
                    f'border-radius:999px;color:#166534;font-size:0.75rem;margin-right:0.3rem;margin-bottom:0.3rem;">'
                    f'{kw.replace("&", "&amp;").replace("<", "&lt;")}</span>'
                    for kw in matched
                )
                st.markdown(f'<div>{badges}</div>', unsafe_allow_html=True)
            else:
                st.markdown('<p style="color:#64748B;font-size:0.85rem;">No matched keywords found.</p>', unsafe_allow_html=True)

        with kw2:
            st.markdown(
                '<p style="color:#DC2626;font-weight:600;font-size:0.9rem;margin-bottom:0.5rem;">❌ Missing Keywords</p>',
                unsafe_allow_html=True,
            )
            if missing:
                badges = "".join(
                    f'<span style="display:inline-block;padding:0.25rem 0.6rem;'
                    f'background:#FEE2E2;border:1px solid #FCA5A5;'
                    f'border-radius:999px;color:#B91C1C;font-size:0.75rem;margin-right:0.3rem;margin-bottom:0.3rem;">'
                    f'{kw.replace("&", "&amp;").replace("<", "&lt;")}</span>'
                    for kw in missing
                )
                st.markdown(f'<div>{badges}</div>', unsafe_allow_html=True)
            else:
                st.markdown('<p style="color:#64748B;font-size:0.85rem;">No missing keywords.</p>', unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown(
            f"""
            <div style="background:#EFF6FF;border:1px solid #BFDBFE;
                 border-radius:8px;padding:1rem;margin-top:1rem;">
                <p style="color:#1E40AF;font-size:0.9rem;line-height:1.6;">
                    💡 <strong>Recommendation:</strong> {recommendation.replace("&", "&amp;").replace("<", "&lt;")}
                </p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    section_end()
    st.markdown("<hr style='border-color:#E2E8F0;margin:2rem 0;'>", unsafe_allow_html=True)
