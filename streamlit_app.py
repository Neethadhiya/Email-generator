#pip install streamlit
import os
import streamlit as st
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
import os
load_dotenv()

os.environ["OPENAI_API_KEY"] = st.secrets["OPENAI_API_KEY"]
st.title("Email Generator 🐦")
st.subheader("🚀 Generate email on any subject")
gpt3_model = ChatOpenAI(model_name = "gpt-3.5-turbo-0125")

subject = st.text_input("Subject")
tone = st.text_input("Tone")
address_to = st.text_input("Address to")

if st.button("Generate"):
    prompt = f"Generate an email on {subject} with tone {tone} address to {address_to}."
    response = gpt3_model.invoke(prompt)
    st.write(response.content)

# python test.py