# sections/chatbot.py — Section 12: "Ask Narendra" AI Chatbot
import streamlit as st
from components.chatbot_robot import render_robot_panel
from utils.chatbot_engine import get_response
from utils.styles import section_start, section_end


def _init_chat_history() -> None:
    if "chat_history" not in st.session_state:
        st.session_state["chat_history"] = []


def _submit_prompt(prompt: str) -> None:
    prompt = prompt.strip()
    if not prompt:
        return

    st.session_state["chat_history"].append({"role": "user", "content": prompt})
    response = get_response(prompt, st.session_state["chat_history"])
    st.session_state["chat_history"].append({"role": "assistant", "content": response})


def _handle_question(question: str) -> None:
    _submit_prompt(question)
    st.rerun()


def render_chatbot():
    st.markdown('<div id="chatbot"></div>', unsafe_allow_html=True)
    section_start("bold")
    st.markdown('<div class="section-heading section-heading--bold">Ask Narendra 🤖</div>', unsafe_allow_html=True)

    _init_chat_history()

    robot_col, chat_col = st.columns([0.85, 2.15], gap="large")

    with robot_col:
        render_robot_panel(_handle_question)

    with chat_col:
        st.markdown(
            """
            <p class="chatbot-intro">
                Ask me anything about Narendra's skills, projects, experience, or availability.
            </p>
            """,
            unsafe_allow_html=True,
        )

        chat_box = st.container(height=320)
        with chat_box:
            if not st.session_state["chat_history"]:
                st.markdown(
                    """
                    <div class="chatbot-empty-state">
                        Your conversation will appear here. Type a question on the right
                        or click the robot to get started.
                    </div>
                    """,
                    unsafe_allow_html=True,
                )
            else:
                for message in st.session_state["chat_history"]:
                    with st.chat_message(message["role"]):
                        st.markdown(message["content"])

        ask_col, btn_col = st.columns([5, 1], gap="small", vertical_alignment="bottom")
        with ask_col:
            prompt = st.text_input(
                "Ask a question",
                placeholder="Type your question here...",
                key="chatbot_question_input",
                label_visibility="collapsed",
            )
        with btn_col:
            ask_clicked = st.button("Ask", key="chatbot_ask_btn", type="primary", width="stretch")

        if ask_clicked and prompt:
            _handle_question(prompt)

        if st.session_state["chat_history"]:
            if st.button("Clear Chat", key="clear_chat", width="content"):
                st.session_state["chat_history"] = []
                st.rerun()

    section_end()
    st.markdown("<hr style='border-color:#E2E8F0;margin:2rem 0;'>", unsafe_allow_html=True)
