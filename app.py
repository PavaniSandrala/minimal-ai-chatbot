import streamlit as st
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage

st.set_page_config(
    page_title="Minimal AI Chatbot",
    page_icon="🤖"
)

st.title("🤖 Minimal AI Chatbot")
st.caption("Powered by Groq + LangChain")

# Create the AI model
llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0.7,
    api_key=st.secrets["GROQ_API_KEY"]
)

# Store conversation
if "messages" not in st.session_state:
    st.session_state.messages = [
        SystemMessage(
            content="You are a helpful and friendly AI assistant."
        )
    ]

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