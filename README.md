# Multiple LangChain + Streamlit Projects
---
I have created 3 small demo application projects in this repository built using:
- LangChain (Runnables API)
- LLaMA 3 model
- Streamlit
- PromptTemplate from langchain_core

These projects serve as simple examples to demonstrate how LangChain can be used to build:
1. A Multi-Step Information Generator
2. A Financial Advisor Bot
3. A Language Translation Tool
Each mini-project is designed to be clear, beginner-friendly, and easy to extend.

## Requirements

- Python 3.12+
- Local Ollama server with LLaMA3 model
- GPU-enabled environment recommended for faster response

## Features
- Run LLaMA3 locally using Ollama
- Use LangChain's prompt templates and output parser
- Smooth Ul using Streamlit
- Real-time response generation

## Technologies Used:
- Streamlit, Python
- Models used: LLaMA3 

## Project Overview

### 1. Famous Person Information — Multi-Step Chain
**File**: famous_person.py
- This app demonstrates a multi-step chain using LangChain Runnables:
- Step 1: Describe the person
- Step 2: Identify when they were born
- Step 3: List key life events
This shows how to pass data between LLM calls using:
```bash
prompt | llm | mapping | prompt2 | llm 
```
#### Workflow:
```bash
1. User enters a famous person's name
2. LLM provides a short explanation
3. Output is passed to a second prompt
4. LLM returns date of birth
5. DOB is passed to the final prompt
6. LLM returns 5 major life events
```
#### Purpose:
```bash
• Demonstrates multi-step LLM pipelines
• Shows how to use PromptTemplate + Runnables
• Teaches how to chain prompts using lambda mappings
```
---
### 2. Financial Advisor Bot
**File**: financial_advisor.py
- This mini-app uses a single prompt template to simulate a simple financial advisor.
- User enters a financial concept (e.g., income tax, mutual funds, savings plan) and the LLM explains it in simple terms.
#### Workflow:
```bash
1. User types a financial topic
2. PromptTemplate inserts the topic
3. LLM returns a clear explanation
```
#### Purpose:
```bash
• Shows how to build a domain-specific assistant
• Simple LangChain Runnable pipeline-->   prompt | llm
```
---
## 3. Language Translation Tool
File: language_translator. py
This app performs text translation into a user-selected language using:
• selectbox of streamlit
• Ollama (Llama3 model)
#### Workflow:
```bash
1. User enters a sentence
2. User selects the target language (Kannada, Hindi, Tamil, Spanish, etc.)
3. PromptTemplate asks the LLM to translate the text
4. LLM returns the translation in an easy-to-understand format
```
#### Purpose:
```bash
• Demonstrates dynamic prompt variables
• Shows how to combine Streamlit widgets with LangChain
• Cl
```
---
## Project Structure

```bash
Langchain_basic/
│
├─ famous.py             
├─ financial.py  
├─ language_translation.py           
├─ README.md
└─ requirements.txt      # Python dependencies
```

## Installation

## 🛠 Installation

### 1. Clone the repo
```bash
git clone https://github.com/AmreetNanda/Langchain_basic.git
cd Langchain_basic
```
### 2. Requirements.txt
```bash
langchain
langchain_community
langchain-core
langchain-classic
gradio
ipykernel
streamlit
```
### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Run Streamlit app
```bash
1. streamlit run famous.py   
2. streamlit run financial.py  
3. streamlit run language_translation.py  
```
Open in your browser:
```
👉 http://localhost:8501/
👉 Enter the prompt in the text bex and hit enter.
👉 The model will then process the prompt entered and will generate the appropriate response accordingly.
```

## License

[MIT](https://choosealicense.com/licenses/mit/)
## Demo
### 1. Famous person Demo
https://github.com/user-attachments/assets/6f71992b-b37d-4a12-8161-529a68c87db1

### 2. Financial advice Demo
https://github.com/user-attachments/assets/7c99ca5d-1ff8-45c6-bf89-0f9bda23b108

### 3. Language Translation Demo
https://github.com/user-attachments/assets/c8e6ba1c-8a77-4a2e-8a04-dce1d64e6bc3
