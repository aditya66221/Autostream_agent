import streamlit as st
from agent import Agent

# Title
st.title("🎥 AutoStream AI Assistant")

# Initialize bot
if "bot" not in st.session_state:
    st.session_state.bot = Agent()

# Chat history
if "chat" not in st.session_state:
    st.session_state.chat = []

# Input box
user_input = st.text_input("You:")

# When user enters input
if user_input:
    response = st.session_state.bot.handle_input(user_input)

    st.session_state.chat.append(("You", user_input))
    st.session_state.chat.append(("Bot", response))

# Display chat
for sender, msg in st.session_state.chat:
    if sender == "You":
        st.markdown(f"**🧑 You:** {msg}")
    else:
        st.markdown(f"**🤖 Bot:** {msg}")