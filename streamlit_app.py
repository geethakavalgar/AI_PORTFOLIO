import streamlit as st
from src.utils import extract_text, normalize_text
from src.model import analyze_resume_match

st.set_page_config(page_title="AI Resume Matcher Pro", layout="wide")
st.title("AI Resume Matcher Pro")
st.caption("Compare a resume against a job description using semantic similarity and keyword analysis.")

with st.sidebar:
    st.header("How it works")
    st.markdown("""
    1. Upload a resume PDF  
    2. Paste a job description  
    3. Review match score, matched keywords, and missing keywords
    """)

resume_file = st.file_uploader("Upload Resume (PDF)", type=["pdf"])
job_desc = st.text_area("Paste Job Description", height=250, placeholder="Paste the full job description here...")

if st.button("Analyze Match", use_container_width=True):
    if not resume_file or not job_desc.strip():
        st.warning("Please upload a resume and paste a job description.")
    else:
        with st.spinner("Analyzing..."):
            resume_text = extract_text(resume_file)
            results = analyze_resume_match(resume_text, job_desc)

        score = results["match_score"]
        matched = results["matched_keywords"]
        missing = results["missing_keywords"]
        top_resume_terms = results["top_resume_terms"]

        st.subheader("Overall Match")
        st.progress(min(max(score / 100.0, 0), 1.0))
        st.metric("Match Score", f"{score:.1f}%")

        c1, c2 = st.columns(2)

        with c1:
            st.subheader("Matched Keywords")
            if matched:
                st.success(", ".join(matched))
            else:
                st.info("No strong keyword overlap found.")

        with c2:
            st.subheader("Missing Keywords")
            if missing:
                st.warning(", ".join(missing))
            else:
                st.success("No obvious missing keywords detected.")

        st.subheader("Top Resume Terms")
        if top_resume_terms:
            st.write(", ".join([f"{term} ({count})" for term, count in top_resume_terms]))
        else:
            st.write("Not enough text to extract top terms.")

        with st.expander("Resume Text Preview"):
            st.write(normalize_text(resume_text)[:4000])

        with st.expander("Job Description Preview"):
            st.write(normalize_text(job_desc)[:4000])
