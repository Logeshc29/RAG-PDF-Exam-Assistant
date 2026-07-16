import streamlit as st

st.title("RAG PDF Exam Assistant")

uploaded_file = st.file_uploader(
    "Upload PDF",
    type=["pdf"]
)

if uploaded_file:
    st.success("PDF Uploaded Successfully")

question = st.text_input(
    "Ask a Question"
)

if st.button("Submit"):
    st.write(
        "Answer generated from PDF"
    )
