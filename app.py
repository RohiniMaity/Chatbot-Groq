import streamlit as st
import os
import groq as Groq
import random
from langchain.chains import ConversationChain
from langchain.chains.conversation.memory import ConversationBufferWindowMemory
from langchain_groq import ChatGroq
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

groq_api_key = os.environ["GROQ_API_KEY"]

def main():
    st.title("Groq Chat App")
    #Add customization option to sidebar
    st. sidebar.title("Select an LLM")
    model = st.sidebar.selectbox(        #select model
        'Select a Model',
        ('mixtral-8x7b-32768', 'llama3-8b-8192')
    )

    conversational_memory_length = st.sidebar.slider('Conversational memory length:', 1, 10, value=5)
    memory = ConversationBufferWindowMemory(k=conversational_memory_length, return_messages=True)
    user_question = st.text_area("Ask a question ...")

    #session state variable
    if 'chat_history' not in st.session_state:
        st.session_state.chat_history = []   #empty list
    else:
        for message in st.session_state.chat_history:
            memory.save_context({'input':message['human']}, {'output':message['AI']})
    
    groq_chat = ChatGroq(               #llm
        groq_api_key=groq_api_key,
        model_name=model
    )

    conversation = ConversationChain(    # can be made to pipeline for RAG
        llm=groq_chat,
        memory=memory,
        verbose=True
    )

    if user_question:
        response = conversation.predict(input=user_question)
        message = {'human': user_question, 'AI': response}
        st.session_state.chat_history.append(message)
        st.write("You:", user_question)
        st.write("AI:", response)

if __name__ == "__main__":
    main()