# utils/chatbot_engine.py — Groq-powered AI chatbot (llama3-8b-8192)
# Falls back to a static FAQ dict when GROQ_API_KEY is not configured.
import streamlit as st
from utils.data import PERSONAL_INFO, RESUME_TEXT, CHATBOT_FAQ

_MODEL = "llama3-8b-8192"

_SYSTEM_PROMPT_TEMPLATE = """You are a professional AI assistant representing {name}.
Your job is to answer visitor questions about {name}'s skills, projects, work experience,
certifications, and availability for new opportunities.

Rules:
- Only answer based on the resume context provided below.
- Be concise, friendly, and professional.
- If a question is not covered by the resume context, say so politely and suggest
  the visitor use the Contact section to reach out directly.
- Never make up information not present in the context.
- Respond in plain text, no markdown formatting.

Resume Context:
---
{resume_text}
---
"""


def build_system_prompt() -> str:
    """Build the chatbot system prompt from resume data."""
    return _SYSTEM_PROMPT_TEMPLATE.format(
        name=PERSONAL_INFO.get("name", "Narendra Fulwaria"),
        resume_text=RESUME_TEXT.strip(),
    )


def get_response(user_message: str, chat_history: list) -> str:
    """
    Get a chatbot response for user_message given the current chat_history.

    Args:
        user_message : The latest message from the visitor.
        chat_history : List of {"role": "user"|"assistant", "content": str} dicts.

    Returns:
        str — the assistant reply.
    """
    if not user_message.strip():
        return "Please type a question to get started."

    # ---- Try Groq API first ------------------------------------------
    if _has_groq_key():
        try:
            return _groq_response(user_message, chat_history)
        except Exception as exc:
            # Log to Streamlit and fall through to FAQ
            st.warning(f"Chatbot API error: {exc}. Falling back to FAQ mode.")

    # ---- Static FAQ fallback -----------------------------------------
    return _faq_response(user_message)


# ---------------------------------------------------------------------------
# Groq API
# ---------------------------------------------------------------------------

def _has_groq_key() -> bool:
    try:
        return bool(st.secrets.get("GROQ_API_KEY", ""))
    except Exception:
        return False


def _groq_response(user_message: str, chat_history: list) -> str:
    from groq import Groq  # imported lazily — only when key is present

    client = Groq(api_key=st.secrets["GROQ_API_KEY"])

    system_prompt = build_system_prompt()

    # Build messages list: system + history + new user message
    messages = [{"role": "system", "content": system_prompt}]

    # Include last 10 turns of history to stay within token limits
    for turn in chat_history[-10:]:
        role    = turn.get("role", "user")
        content = turn.get("content", "")
        if role in ("user", "assistant") and content:
            messages.append({"role": role, "content": content})

    messages.append({"role": "user", "content": user_message})

    response = client.chat.completions.create(
        model=_MODEL,
        messages=messages,
        max_tokens=512,
        temperature=0.5,
    )

    return response.choices[0].message.content.strip()


# ---------------------------------------------------------------------------
# Static FAQ fallback
# ---------------------------------------------------------------------------

_FAQ_KEYWORDS: dict[str, list[str]] = {
    "projects":       ["project", "built", "made", "created", "github", "workflow", "analyzer", "chatbot"],
    "skills":         ["skill", "know", "technology", "tech", "tools", "language", "python", "sql", "power bi", "tableau"],
    "experience":     ["experience", "work", "job", "career", "history", "manager", "supermart", "retail", "business"],
    "certifications": ["certif", "course", "degree", "qualif", "be10x", "iit", "masai"],
    "availability":   ["availab", "hire", "open", "looking", "opportun", "contact", "reach"],
}


def _faq_response(user_message: str) -> str:
    msg_lower = user_message.lower()

    for key, keywords in _FAQ_KEYWORDS.items():
        if any(kw in msg_lower for kw in keywords):
            return CHATBOT_FAQ.get(key, CHATBOT_FAQ["default"])

    return CHATBOT_FAQ["default"]
