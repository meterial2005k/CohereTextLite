import os
import streamlit as st
import cohere

# 🔑 Get your API key from environment variable
COHERE_API_KEY = os.getenv("COHERE_API_KEY")

co = cohere.Client(COHERE_API_KEY)

st.set_page_config(page_title="Text Summarizer with Cohere", layout="centered")
st.title("📝 Text Summarizer")
st.markdown("Summarize long text using Cohere's AI")

input_text = st.text_area("Paste your text here:", height=300)

if st.button("Summarize") and input_text:
    with st.spinner("Summarizing..."):
        response = co.summarize(
            text=input_text,
            length='medium',
            format='paragraph',
            model='command'
        )
        summary = response.summary

    st.subheader("🧠 Summary:")
    st.success(summary)
