import os
import tempfile
import streamlit as st

from src.ingest import load_and_split_pdfs, build_vector_store
from src.llm import get_llm
from src.rag_pipeline import answer_question, render_answer_with_sources

st.set_page_config(page_title="RAG PDF Chatbot Pro", layout="wide")
st.title("RAG PDF Chatbot Pro")
st.caption("Upload one or more PDFs, ask questions, and get grounded answers with sources.")

if "messages" not in st.session_state:
    st.session_state.messages = []
if "vector_store" not in st.session_state:
    st.session_state.vector_store = None
if "llm" not in st.session_state:
    st.session_state.llm = None

with st.sidebar:
    st.header("Upload Documents")
    uploaded_files = st.file_uploader(
        "Choose PDF files",
        type=["pdf"],
        accept_multiple_files=True
    )

    if st.button("Process PDFs", use_container_width=True):
        if not uploaded_files:
            st.warning("Please upload at least one PDF.")
        else:
            saved_paths = []
            with st.spinner("Loading and indexing documents..."):
                for uploaded_file in uploaded_files:
                    suffix = os.path.splitext(uploaded_file.name)[1]
                    with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as tmp:
                        tmp.write(uploaded_file.read())
                        saved_paths.append(tmp.name)

                documents = load_and_split_pdfs(saved_paths)
                st.session_state.vector_store = build_vector_store(documents)
                st.session_state.llm = get_llm()

            st.success(f"Processed {len(uploaded_files)} PDF file(s).")

    st.divider()
    st.markdown("### Tips")
    st.markdown("- Upload small PDFs first for faster testing")
    st.markdown("- Ask specific questions")
    st.markdown("- Re-process after changing files")

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

user_question = st.chat_input("Ask a question about your uploaded PDFs")

if user_question:
    st.session_state.messages.append({"role": "user", "content": user_question})
    with st.chat_message("user"):
        st.markdown(user_question)

    if st.session_state.vector_store is None or st.session_state.llm is None:
        assistant_reply = "Please upload and process at least one PDF first."
    else:
        with st.spinner("Searching documents and generating answer..."):
            answer, docs = answer_question(
                st.session_state.vector_store,
                st.session_state.llm,
                user_question
            )
            assistant_reply = render_answer_with_sources(answer, docs)

    st.session_state.messages.append({"role": "assistant", "content": assistant_reply})
    with st.chat_message("assistant"):
        st.markdown(assistant_reply)
