# utils/ats_scorer.py — Offline ATS keyword match engine (pure Python, no sklearn)
import math
import re
import string
from collections import Counter

_STOP_WORDS = frozenset({
    "a", "an", "the", "and", "or", "but", "in", "on", "at", "to", "for",
    "of", "with", "by", "from", "as", "is", "was", "are", "were", "be",
    "been", "being", "have", "has", "had", "do", "does", "did", "will",
    "would", "could", "should", "may", "might", "must", "shall", "can",
    "this", "that", "these", "those", "i", "you", "he", "she", "it",
    "we", "they", "what", "which", "who", "whom", "whose", "when",
    "where", "why", "how", "all", "each", "every", "both", "few",
    "more", "most", "other", "some", "such", "no", "nor", "not",
    "only", "own", "same", "so", "than", "too", "very", "just",
})


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

    resume_terms = _extract_terms(clean_resume)
    jd_terms     = _extract_terms(clean_jd)

    if not resume_terms or not jd_terms:
        return _empty_result("Could not analyse text — please provide more content.")

    try:
        vectors, vocab = _tfidf_vectors([resume_terms, jd_terms])
    except ValueError:
        return _empty_result("Could not analyse text — please provide more content.")

    cosine_score = _cosine_similarity(vectors[0], vectors[1])

    resume_tokens = set(clean_resume.split())
    jd_tokens     = set(w for w in clean_jd.split() if len(w) > 2)
    if jd_tokens:
        overlap_score = len(resume_tokens & jd_tokens) / len(jd_tokens)
    else:
        overlap_score = 0.0

    blended = cosine_score * 0.5 + overlap_score * 0.5
    score   = int(round(min(blended * 130, 100)))

    jd_vector = vectors[1]
    jd_keywords = sorted(jd_vector, key=jd_vector.get, reverse=True)[:30]
    jd_keywords = [kw for kw in jd_keywords if jd_vector[kw] > 0]

    resume_words = set(clean_resume.split())
    matched_keywords = []
    missing_keywords = []

    for kw in jd_keywords:
        kw_words = set(kw.split())
        if kw_words.issubset(resume_words):
            matched_keywords.append(kw)
        else:
            missing_keywords.append(kw)

    matched_keywords = matched_keywords[:15]
    missing_keywords = missing_keywords[:15]
    recommendation = _generate_recommendation(score, missing_keywords)

    return {
        "score":            score,
        "matched_keywords": matched_keywords,
        "missing_keywords": missing_keywords,
        "recommendation":   recommendation,
    }


def _extract_terms(text: str) -> list[str]:
    """Unigrams and bigrams, excluding stop words."""
    tokens = [t for t in text.split() if t not in _STOP_WORDS and len(t) > 1]
    terms = list(tokens)
    terms.extend(f"{tokens[i]} {tokens[i + 1]}" for i in range(len(tokens) - 1))
    return terms


def _tfidf_vectors(doc_terms: list[list[str]], max_features: int = 5000) -> tuple[list[dict], list[str]]:
    """Build smoothed TF-IDF vectors for each document."""
    if not doc_terms or not any(doc_terms):
        raise ValueError("empty documents")

    df = Counter()
    doc_counts = []
    for terms in doc_terms:
        counts = Counter(terms)
        doc_counts.append(counts)
        for term in counts:
            df[term] += 1

    total_tf = Counter()
    for counts in doc_counts:
        total_tf.update(counts)

    vocab = [term for term, _ in total_tf.most_common(max_features)]
    vocab_set = set(vocab)
    n_docs = len(doc_terms)

    vectors = []
    for counts in doc_counts:
        total = sum(counts.values()) or 1
        vec = {}
        for term in vocab_set:
            if term not in counts:
                continue
            tf = counts[term] / total
            idf = math.log((n_docs + 1) / (df[term] + 1)) + 1
            vec[term] = tf * idf
        vectors.append(vec)

    return vectors, vocab


def _cosine_similarity(vec_a: dict, vec_b: dict) -> float:
    if not vec_a or not vec_b:
        return 0.0
    common = set(vec_a) & set(vec_b)
    if not common:
        return 0.0
    dot = sum(vec_a[k] * vec_b[k] for k in common)
    norm_a = math.sqrt(sum(v * v for v in vec_a.values()))
    norm_b = math.sqrt(sum(v * v for v in vec_b.values()))
    if norm_a == 0 or norm_b == 0:
        return 0.0
    return dot / (norm_a * norm_b)


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
    if score >= 60:
        base = "Good match — your background is relevant to this role."
        if top_missing:
            return f"{base} Consider adding or highlighting: {top_missing}."
        return base
    if score >= 40:
        base = "Partial match — some relevant skills are present but there are gaps."
        if top_missing:
            return (
                f"{base} Try incorporating these missing keywords: {top_missing}. "
                "Tailor your resume summary to mirror the job description language."
            )
        return base
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
