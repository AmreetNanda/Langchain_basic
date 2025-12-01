import os
os.environ["LANGCHAIN_TRACING_V2"] = "false" 

from langchain_community.llms import Ollama
from langchain_core.prompts import PromptTemplate
import streamlit as st

st.title("Language Translation")
input_text = st.text_input("Enter the sentence to be translated")

language = ["Hindi","Odia","Kannada","Tamil","Telegu","German","French","Spanish"]
target_language = st.selectbox("Select the target language",language)

# Prompt Template
demo_template = """In an easy way translate the following sentence {sentence} into {target_sentence}."""
prompt = PromptTemplate(
    input_variables=['sentence','target_sentence'], 
    template=demo_template
)

llm = Ollama(model="llama3", temperature=0.5)

# Runnable chain
chain = (prompt | llm)

if input_text:
    response = chain.invoke({"sentence": input_text, "target_sentence":target_language})
    st.write(response)