# components/chatbot_robot.py — Interactive robot avatar for the Ask Narendra chatbot
import streamlit as st


SUGGESTED_QUESTIONS = [
    "What are Narendra's key skills?",
    "Tell me about his projects.",
    "What is his work experience?",
    "Is he open to new opportunities?",
]


def render_robot_panel(on_question) -> None:
    """
    Render the left-side robot panel with a clickable avatar and quick questions.

    Args:
        on_question: Callable invoked with the selected question string.
    """
    st.markdown(
        """
        <div class="robot-panel">
            <div class="robot-avatar" aria-hidden="true">
                <div class="robot-antenna"></div>
                <div class="robot-head">
                    <div class="robot-eye left"></div>
                    <div class="robot-eye right"></div>
                    <div class="robot-mouth"></div>
                </div>
                <div class="robot-neck"></div>
                <div class="robot-body">
                    <div class="robot-core"></div>
                    <div class="robot-light"></div>
                </div>
                <div class="robot-arm left"></div>
                <div class="robot-arm right"></div>
            </div>
            <div class="robot-speech-bubble">Hi! Click me or pick a question below.</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    if st.button("Ask Narendra's AI", key="robot_avatar_click", type="primary", width="stretch"):
        on_question("Hi! Can you introduce Narendra?")

    st.markdown(
        '<p class="robot-quick-label">Quick questions</p>',
        unsafe_allow_html=True,
    )

    for i, question in enumerate(SUGGESTED_QUESTIONS):
        if st.button(question, key=f"chatbot_suggest_{i}", width="stretch"):
            on_question(question)
