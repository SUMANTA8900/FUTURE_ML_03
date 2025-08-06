import streamlit as st
import sys
import os

# Set import path for backend
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from backend.chatbot_engine import get_bot_response

# Page config
st.set_page_config(
    page_title="Customer Support Chatbot",
    page_icon="🤖",
    layout="centered",
    initial_sidebar_state="auto"
)

# 💅 Enhanced CSS Theme
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(135deg, #0f2027, #203a43, #2c5364);
        color: white;
        font-family: 'Segoe UI', sans-serif;
    }

    h1, h2, h3, h4, h5, h6 {
        color: #ffffff;
    }

    /* Button Chips */
    button[kind="secondary"] {
        background-color: rgba(255, 255, 255, 0.08) !important;
        color: white !important;
        border-radius: 16px !important;
        padding: 0.4em 1.2em !important;
        margin: 0.3em 0.5em !important;
        border: 1px solid #5e5e5e !important;
        transition: 0.2s ease-in-out;
    }

    button[kind="secondary"]:hover {
        background-color: #00c6ff !important;
        color: black !important;
        border: 1px solid #00c6ff !important;
        transform: scale(1.03);
    }

    /* Input box */
    .stTextInput>div>div>input {
        background-color: rgba(255, 255, 255, 0.1);
        border-radius: 8px;
        color: white;
    }

    /* Chat box styling */
    .stMarkdown {
        font-size: 1.1rem;
        padding: 1em;
        border-radius: 10px;
        background: rgba(255, 255, 255, 0.06);
        backdrop-filter: blur(6px);
        box-shadow: 0 0 10px rgba(0,0,0,0.2);
        margin-top: 10px;
    }

    /* Footer */
    footer {
        visibility: hidden;
    }

    .footer {
        text-align: center;
        padding: 2em 0;
        color: white;
        font-size: 0.9rem;
        opacity: 0.7;
    }
    </style>
""", unsafe_allow_html=True)

# Title
st.markdown("## 🤖 Customer Support Chatbot")
st.markdown("Ask a question or click on a suggestion below:")

# Suggested FAQs
suggested = [
    "How do I reset my password?",
    "What is your refund policy?",
    "How can I track my order?",
    "Do you offer international shipping?",
    "Hi", "Hello", "What are your working hours?"
]

# Render FAQ chips
cols = st.columns(3)
for i, q in enumerate(suggested):
    with cols[i % 3]:
        if st.button(q, key=q):
            st.session_state["query"] = q

# Input box
query = st.text_input("Ask a question...", value=st.session_state.get("query", ""), key="query_input")

# Response output
if query:
    response = get_bot_response(query)
    st.markdown(f"💬 **{response}**")

# Custom Footer
st.markdown("<div class='footer'>Made with ❤️ by Sumanta</div>", unsafe_allow_html=True)
