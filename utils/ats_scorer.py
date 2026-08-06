# utils/ats_scorer.py — Offline ATS keyword match engine
# No external API needed — runs entirely on scikit-learn TF-IDF + cosine similarity.
import re
import string

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def score_resume(job_description: str, resume_text: str) -> dict:
    """
    Score how well resume_text matches job_description.

    Returns:
        score              : int (0–100)
        matched_keywords   : list[str]  — top JD keywords found in resume
        missing_keywords   : list[str]  — top JD keywords NOT found in resume
        recommendation     : str
    """
    if not job_description.strip() or not resume_text.strip():
        return {
            "score": 0,
            "matched_keywords": [],
            "missing_keywords": [],
            "recommendation": "Please provide both a job description and resume text.",
        }

    clean_jd     = _clean(job_description)
    clean_resume = _clean(resume_text)

    # ---- 1. TF-IDF cosine similarity ------------------------------------
    vectorizer = TfidfVectorizer(stop_words="english", ngram_range=(1, 2), max_features=5000)
    try:
        tfidf_matrix = vectorizer.fit_transform([clean_resume, clean_jd])
    except ValueError:
        return _empty_result("Could not analyse text — please provide more content.")

    cosine_score = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])[0][0]

    # ---- 2. Keyword overlap score (Jaccard-style) -----------------------
    # Gives a more intuitive match % based on word overlap
    resume_tokens = set(clean_resume.split())
    jd_tokens     = set(w for w in clean_jd.split() if len(w) > 2)  # skip tiny words
    if jd_tokens:
        overlap_score = len(resume_tokens & jd_tokens) / len(jd_tokens)
    else:
        overlap_score = 0.0

    # Blend: 50% cosine + 50% overlap, scale to 0-100
    blended = (cosine_score * 0.5 + overlap_score * 0.5)
    score   = int(round(min(blended * 130, 100)))  # *130 to spread the range naturally

    # ---- 3. Extract top keywords from JD --------------------------------
    jd_vector     = tfidf_matrix[1].toarray()[0]
    feature_names = vectorizer.get_feature_names_out()

    # Get indices of top-weighted JD terms
    top_n        = 30
    top_indices  = jd_vector.argsort()[::-1][:top_n]
    jd_keywords  = [feature_names[i] for i in top_indices if jd_vector[i] > 0]

    # ---- 4. Split into matched / missing --------------------------------
    resume_words = set(clean_resume.split())

    matched_keywords = []
    missing_keywords = []

    for kw in jd_keywords:
        # Multi-word phrase: check if all words appear in resume
        kw_words = set(kw.split())
        if kw_words.issubset(resume_words):
            matched_keywords.append(kw)
        else:
            missing_keywords.append(kw)

    # Cap display lists
    matched_keywords = matched_keywords[:15]
    missing_keywords = missing_keywords[:15]

    # ---- 5. Recommendation ----------------------------------------------
    recommendation = _generate_recommendation(score, missing_keywords)

    return {
        "score":            score,
        "matched_keywords": matched_keywords,
        "missing_keywords": missing_keywords,
        "recommendation":   recommendation,
    }


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _clean(text: str) -> str:
    """Lowercase, strip punctuation, collapse whitespace."""
    text = text.lower()
    text = text.translate(str.maketrans("", "", string.punctuation))
    text = re.sub(r"\s+", " ", text).strip()
    return text


def _generate_recommendation(score: int, missing_keywords: list) -> str:
    top_missing = ", ".join(missing_keywords[:3]) if missing_keywords else None

    if score >= 80:
        return (
            "Strong match — your profile aligns well with this role. "
            "Make sure your resume highlights these skills prominently in the summary and experience sections."
        )
    elif score >= 60:
        base = "Good match — your background is relevant to this role."
        if top_missing:
            return f"{base} Consider adding or highlighting: {top_missing}."
        return base
    elif score >= 40:
        base = "Partial match — some relevant skills are present but there are gaps."
        if top_missing:
            return (
                f"{base} Try incorporating these missing keywords: {top_missing}. "
                "Tailor your resume summary to mirror the job description language."
            )
        return base
    else:
        return (
            "Low match — this role may require different skills or experience. "
            "Review the job description carefully and update your resume to reflect relevant keywords."
        )


def _empty_result(message: str) -> dict:
    return {
        "score":            0,
        "matched_keywords": [],
        "missing_keywords": [],
        "recommendation":   message,
    }
