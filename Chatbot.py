import openai
import streamlit as st
from streamlit_chat import message

with st.sidebar:
    openai_api_key = st.text_input('OpenAI API Key',key='chatbot_api_key')
    "[View the source code](https://github.com/streamlit/llm-examples/blob/main/Chatbot.py)"
    "[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/streamlit/llm-examples?quickstart=1)"

st.title("💬 Santander GPS")
#openai.api_key = st.secrets.openai_api_key
if "messages" not in st.session_state:
    st.session_state["messages"] = [{
        "role": "assistant",
        "avatar_style" = "shapes",
        "content": "Hola, soy un asistente que te ayuda a estructurar un problema. ¿Qué problema tienes?"}]

with st.form("chat_input", clear_on_submit=True):
    a, b = st.columns([4, 1])
    user_input = a.text_input(
        label="Tu mensaje:",
        placeholder="¿Qué te gustaría responder?",
        label_visibility="collapsed",
    )
    b.form_submit_button("Enviar", use_container_width=True)

for msg in st.session_state.messages:
    message(msg["content"], is_user=msg["role"] == "user")

if user_input and not openai_api_key:
    st.info("OpenAI API key")
    
if user_input and openai_api_key:
    openai.api_key = openai_api_key
    st.session_state.messages.append({"role": "user", "content": user_input})
    message(user_input, is_user=True, avatar_style="icons")
    response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=st.session_state.messages)
    msg = response.choices[0].message
    st.session_state.messages.append(msg)
    message(msg.content, avatar_style="shapes")
