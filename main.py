import streamlit as st
import openai
import os

st.title("Patient FAQ Chatbot")

openai.api_key = os.getenv("OPENAI_API_KEY")

context = st.text_area("Paste patient handbook or FAQ content")
query = st.text_input("Ask a patient question")

if context and query:
    prompt = f"Based on the following document, answer the patient's question clearly:\n\nDocument:\n{context}\n\nQuestion:\n{query}"
    with st.spinner("Generating answer..."):
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        st.success(response.choices[0].message["content"])
