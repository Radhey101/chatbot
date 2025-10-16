import streamlit as st
from openai import OpenAI

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

# Streamlit Page Config
st.set_page_config(page_title="Vertual Assistance Chatbot", page_icon="💬", layout="centered")

st.title("💬 Vertual Assistance Chatbot")

# Initialize session state for conversation
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "assistant", "content": "Hello 👋! I'm your Vertual assistant. How can I help you today?"}]

# Display chat messages
for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.chat_message("user").markdown(msg["content"])
    else:
        st.chat_message("assistant").markdown(msg["content"])

# Chat input box
user_input = st.chat_input("Type your message...")

if user_input:
    # Add user message to history
    st.session_state.messages.append({"role": "user", "content": user_input})
    st.chat_message("user").markdown(user_input)

    # Get chatbot response
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = client.chat.completions.create(
                model="gpt-4o",  # You can change to "gpt-4o" if available
                messages=st.session_state.messages
            )
            reply = response.choices[0].message.content
            st.markdown(reply)

    # Add bot reply to chat history
    st.session_state.messages.append({"role": "assistant", "content": reply})