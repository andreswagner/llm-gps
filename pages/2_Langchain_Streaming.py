import streamlit as st
from langchain import OpenAI

from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain.chat_models import ChatOpenAI
from langchain import PromptTemplate, LLMChain
from langchain.prompts.chat import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    AIMessagePromptTemplate,
    HumanMessagePromptTemplate,
)
from langchain.schema import (
    AIMessage,
    HumanMessage,
    SystemMessage
)

st.title('🦜🔗 Langchain Streaming App')

template="Eres un asistente que aplica el método socrático para estructurar los problemas que te comentan"
system_message_prompt = SystemMessagePromptTemplate.from_template(template)
example_human = HumanMessagePromptTemplate.from_template("Hi")
example_ai = AIMessagePromptTemplate.from_template("Hmmm, estructuremos esto por parte: 1. 2. 3.")
human_template="{text}"
human_message_prompt = HumanMessagePromptTemplate.from_template(human_template)

with st.sidebar:
    openai_api_key = st.text_input('OpenAI API Key')

def generate_response(input_text):
    chat = ChatOpenAI(temperature=0.7, openai_api_key=openai_api_key)
    chat_prompt = ChatPromptTemplate.from_messages(
        [system_message_prompt, example_human, example_ai, human_message_prompt])
    chain = LLMChain(llm=chat, prompt=chat_prompt)
    st.info(chain.run(input_text))

with st.form('my_form'):
    text = st.text_area('Ingresa tu problema:', 'Necesito darle acceso al Banco a unos consultores')
    submitted = st.form_submit_button('Enviar')
    if submitted:
        generate_response(text)
