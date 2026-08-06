# sections/chatbot.py — Section 12: "Ask Narendra" AI Chatbot
import streamlit as st
from utils.chatbot_engine import get_response


def render_chatbot():
    st.markdown('<div id="chatbot"></div>', unsafe_allow_html=True)
    st.markdown('<div class="section-heading">Ask Narendra 🤖</div>', unsafe_allow_html=True)

    st.markdown(
        """
        <p style="color:#94A3B8;font-size:0.95rem;margin-bottom:1.5rem;">
            Ask me anything about Narendra's skills, projects, or availability.
        </p>
        """,
        unsafe_allow_html=True,
    )

    # ── Initialize chat history ───────────────────────────────────────────
    if "chat_history" not in st.session_state:
        st.session_state["chat_history"] = []

    # ── Render chat history ────────────────────────────────────────────────
    for message in st.session_state["chat_history"]:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # ── Chat input ─────────────────────────────────────────────────────────
    if prompt := st.chat_input("Ask a question..."):
        # Add user message to history
        st.session_state["chat_history"].append({"role": "user", "content": prompt})

        # Display user message
        with st.chat_message("user"):
            st.markdown(prompt)

        # Get assistant response
        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                response = get_response(prompt, st.session_state["chat_history"])
                st.markdown(response)

        # Add assistant response to history
        st.session_state["chat_history"].append({"role": "assistant", "content": response})

    # ── Clear chat button ───────────────────────────────────────────────────
    if st.session_state["chat_history"]:
        if st.button("Clear Chat", key="clear_chat", width='content'):
            st.session_state["chat_history"] = []
            st.rerun()

    st.markdown("<hr style='border-color:#1E293B;margin:2rem 0;'>", unsafe_allow_html=True)
