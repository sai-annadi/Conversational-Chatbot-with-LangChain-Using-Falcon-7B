import streamlit as st
from langchain import HuggingFaceHub
from langchain import PromptTemplate, LLMChain
import os
from dotenv import load_dotenv
import asyncio

# Load environment variables
load_dotenv()

# App title
st.set_page_config(page_title="Falcon 7B Chatbot")

# Hugging Face Hub Credentials (from .env file)
HUGGINGFACEHUB_API_TOKEN = os.getenv("HUGGINGFACE_API_TOKEN")
repo_id = "tiiuae/falcon-7b-instruct"
llm = HuggingFaceHub(huggingfacehub_api_token=HUGGINGFACEHUB_API_TOKEN, 
                     repo_id=repo_id, 
                     model_kwargs={"temperature": 0.1})

template = """You are an intelligent chatbot. Help the following question with brilliant answers.
Question: {question}
Answer:"""
prompt_template = PromptTemplate(template=template, input_variables=["question"])
llm_chain = LLMChain(prompt=prompt_template, llm=llm, verbose=True)

if "messages" not in st.session_state.keys():
    st.session_state.messages = [{"role": "assistant", "content": "How may I assist you today?"}]

# Display or clear chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

def clear_chat_history():
    st.session_state.messages = [{"role": "assistant", "content": "How may I assist you today?"}]

# Sidebar elements
with st.sidebar:
    st.title('Falcon 7B Chatbot')
    st.subheader('Model')
    selected_model = st.sidebar.selectbox('Choose a Falcon model', ['Falcon-7b'], key='selected_model')
    st.button('Clear Chat History', on_click=clear_chat_history)

# Function for generating LLM response with context
async def generate_response(prompt_input):
    response= await llm_chain.acall(prompt_input)
    answer_text = response["text"].split("\n")[-1]
    return answer_text

# User-provided prompt
prompt = st.chat_input()
if prompt:
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)

    if st.session_state.messages[-1]["role"] != "assistant":
        with st.chat_message("assistant"):
            thinking_message = st.text("Thinking...")
            # Use asyncio to await the asynchronous function
            response = asyncio.run(generate_response(prompt))
            st.session_state.messages.append({"role": "assistant", "content": response})
            thinking_message.text("")  # Clear the "Thinking..." message
            st.write(response)  # Now display the response
