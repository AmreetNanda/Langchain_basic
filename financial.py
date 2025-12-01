import os
os.environ["LANGCHAIN_TRACING_V2"] = "false" 

from langchain_community.llms import Ollama
from langchain_core.prompts import PromptTemplate
import streamlit as st

st.title("Financial Advice")
input_text = st.text_input("Enter what do you want to know about finance...")

# Prompt Template
demo_template = """I want you to act as a financial advisor. 
Explain the basics of {financial_concept} in an easy way."""
prompt = PromptTemplate(
    input_variables=['financial_concept'], 
    template=demo_template
)

llm = Ollama(model="llama3", temperature=0.5)

# Runnable chain
chain = (prompt | llm)

if input_text:
    response = chain.invoke({"financial_concept": input_text})
    st.write(response)
