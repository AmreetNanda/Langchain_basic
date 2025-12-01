import streamlit as st
from langchain_community.llms import Ollama
from langchain_core.prompts import PromptTemplate

st.title("Search Result")
input_text = st.text_input("Search the topic you want")

# Step 1: Prompts
first_prompt = PromptTemplate(
    input_variables=["name"],
    template="Tell me about {name}"
)

second_prompt = PromptTemplate(
    input_variables=["info"],
    template="When was {info} born?"
)

third_prompt = PromptTemplate(
    input_variables=["birth_info"],
    template="Mention 5 major events that happened in the lifetime of {birth_info}"
)

# Model
llm = Ollama(model="llama3", temperature=0.8)

# Step 2: Build Runnable Chain
chain = (
    {"name": lambda x: x["name"]}       
    | first_prompt                      
    | llm                               
    | (lambda x: {"info": x})          
    | second_prompt                     
    | llm                               
    | (lambda x: {"birth_info": x})     
    | third_prompt                      
    | llm                               
)

# Step 3: Run
if input_text:
    response = chain.invoke({"name": input_text})
    st.write(response)
