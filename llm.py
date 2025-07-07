import getpass
import os
import streamlit as st
from langchain.chat_models import init_chat_model 
from langchain_core.prompts import load_prompt


GOOGLE_API_KEY = st.secrets["GOOGLE_API_KEY"]

if not os.environ.get("GOOGLE_API_KEY"):
  os.environ["GOOGLE_API_KEY"] = GOOGLE_API_KEY

model = init_chat_model("gemini-2.0-flash", model_provider="google_genai")


st.header('Research Tool')

paper_input = st.selectbox('Select Research Paper Name', ['Select...', 'Attention Is All You Need', 'BERT- Pre-training of Deep Bidirectional Transformers', 'GPT-3: Language Models are Few-Shot Learners', 'Diffusion Models b\Beat GANs on Image Synthesis'])

style_input = st.selectbox('Select Explanation style', ['Beginner-Friendly', 'Technical', 'Code-Oriented', 'Mathematical'])

length_imput = st.selectbox('Select explanation length', ['Short (1-2 paragraphs)', 'Medium (3-5 paragraphs)', 'Long (detailed explanation)'])

template = load_prompt('template.json')

if st.button('Summarize'):
  chain = template | model
  result = chain.invoke({
    'paper_input': paper_input,
    'style_input': style_input,
    'length_input': length_imput
  })
  # result = model.invoke(promt)
  st.write(result.content)