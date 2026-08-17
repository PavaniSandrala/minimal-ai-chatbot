import streamlit as st
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage, AIMessage

# Page configuration
st.set_page_config(
    page_title="Minimal AI Chatbot",
    page_icon="🤖"
)

# Title
st.title("🤖 Minimal AI Chatbot")
st.caption("Powered by Groq + LangChain")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# New Chat button
if st.button("🆕 New Chat"):
    st.session_state.messages = []
    st.rerun()

# API key
api_key = st.secrets["GROQ_API_KEY"]

# Groq model
llm = ChatGroq(
    api_key=api_key,
    model="openai/gpt-oss-20b",
    temperature=0.7
)

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User input
if prompt := st.chat_input("Type your message..."):

    # Display user message
    with st.chat_message("user"):
        st.markdown(prompt)

    # Save user message
    st.session_state.messages.append({
        "role": "user",
        "content": prompt
    })

    # Convert chat history to LangChain messages
    chat_messages = []

    for message in st.session_state.messages:
        if message["role"] == "user":
            chat_messages.append(
                HumanMessage(content=message["content"])
            )
        elif message["role"] == "assistant":
            chat_messages.append(
                AIMessage(content=message["content"])
            )

    # Generate AI response
    with st.chat_message("assistant"):
        response = llm.invoke(chat_messages)
        answer = response.content
        st.markdown(answer)

    # Save AI response
    st.session_state.messages.append({
        "role": "assistant",
        "content": answer
    })