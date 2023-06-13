import streamlit as st
from langchain import OpenAI
from langchain.chat_models import ChatOpenAI
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler

st.title('🦜🔗 Langchain Streaming App')

with st.sidebar:
  openai_api_key = st.text_input('OpenAI API Key')

def generate_response(input_text):
  llm = OpenAI(temperature=0.7, openai_api_key=openai_api_key)
  chat = ChatOpenAI(streaming=True, callbacks=[StreamingStdOutCallbackHandler()], temperature=0)
  resp = chat([HumanMessage(content="Write me a song about sparkling water.")])
  st.info(resp)

with st.form('my_form'):
  text = st.text_area('Enter text:', 'What are 3 key advice for learning how to code?')
  submitted = st.form_submit_button('Submit')
  if submitted:
    generate_response(text)
