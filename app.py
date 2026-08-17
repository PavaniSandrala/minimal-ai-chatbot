import streamlit as st
from langchain_groq import ChatGroq

# Page configuration
st.set_page_config(
    page_title="Minimal AI Chatbot",
    page_icon="🤖"
)

st.title("🤖 Minimal AI Chatbot")
st.caption("Powered by Groq + LangChain")

# Get API key from Streamlit Secrets
api_key = st.secrets["GROQ_API_KEY"]

# Create Groq model
llm = ChatGroq(
    api_key=api_key,
    model="llama-3.3-70b-versatile"
)

# Store chat messages
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
if prompt := st.chat_input("Type your message..."):

    # Display user message
    with st.chat_message("user"):
        st.markdown(prompt)

    st.session_state.messages.append({
        "role": "user",
        "content": prompt
    })

    # Get AI response
    with st.chat_message("assistant"):
        response = llm.invoke(st.session_state.messages)
        answer = response.content
        st.markdown(answer)

    st.session_state.messages.append({
        "role": "assistant",
        "content": answer
    })
if st.button("🗑️ New Chat"):
    st.session_state.messages = [
        SystemMessage(
            content="You are a helpful and friendly AI assistant."
        )
    ]
    st.rerun()

# Display previous messages
for message in st.session_state.messages:

    if isinstance(message, HumanMessage):
        with st.chat_message("user"):
            st.markdown(message.content)

    elif isinstance(message, AIMessage):
        with st.chat_message("assistant"):
            st.markdown(message.content)

# User input
user_input = st.chat_input("Type your message...")

if user_input:

    with st.chat_message("user"):
        st.markdown(user_input)

    st.session_state.messages.append(
        HumanMessage(content=user_input)
    )

    response = llm.invoke(st.session_state.messages)

    with st.chat_message("assistant"):
        st.markdown(response.content)

    st.session_state.messages.append(
        AIMessage(content=response.content)
    )

# New Chat button
if st.button("🗑️ New Chat"):
    st.session_state.messages = [
        SystemMessage(
            content="You are a helpful and friendly AI assistant."
        )
    ]
    st.rerun()

# Display previous messages
for message in st.session_state.messages:

    if isinstance(message, HumanMessage):
        with st.chat_message("user"):
            st.markdown(message.content)

    elif isinstance(message, AIMessage):
        with st.chat_message("assistant"):
            st.markdown(message.content)

# User input
user_input = st.chat_input("Type your message...")

if user_input:

    with st.chat_message("user"):
        st.markdown(user_input)

    st.session_state.messages.append(
        HumanMessage(content=user_input)
    )

    response = llm.invoke(st.session_state.messages)

    with st.chat_message("assistant"):
        st.markdown(response.content)

    st.session_state.messages.append(
        AIMessage(content=response.content)
    )