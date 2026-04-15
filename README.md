# AI Resume Matcher Pro

An AI-powered application that compares a resume against a job description using semantic similarity and keyword overlap analysis.

## Features
- Upload a resume in PDF format
- Paste a job description
- Compute a semantic match score using Sentence Transformers
- Identify matched keywords and missing keywords
- Show top resume terms
- Interactive Streamlit UI for running and reviewing the analysis

## Tech Stack
- Python
- Streamlit (for building and executing the interactive app)
- Sentence Transformers
- scikit-learn
- PyMuPDF
- PyTorch / Torchvision

## Project Structure
```bash
ai_resume_matcher_pro/
├── streamlit_app.py
├── src/
│   ├── __init__.py
│   ├── utils.py
│   └── model.py
├── requirements.txt
└── README.md
```

## How to Run
```bash
pip install -r requirements.txt
streamlit run streamlit_app.py
```

## Output
After uploading a resume and pasting a job description, the app displays:

- **Overall Match Score** as a percentage
- **Matched Keywords** found in both the resume and job description
- **Missing Keywords** that appear in the job description but not strongly in the resume
- **Top Resume Terms** based on resume text frequency
- **Resume Text Preview** and **Job Description Preview** for quick validation

### Sample Output
```text
Match Score: 78.4%

Matched Keywords:
python, machine-learning, streamlit, nlp, api

Missing Keywords:
docker, kubernetes, aws, monitoring

Top Resume Terms:
python (8), ai (6), ml (5), streamlit (4), api (3)
```
### Screenshot
![App Screenshot](output/resume-matcher-demo_1.png)
![App Screenshot](output/resume-matcher-demo_2.png)

## What It Demonstrates
- NLP-based resume analysis
- Embedding-based semantic similarity
- Keyword extraction and gap analysis
- User-facing AI application development with Streamlit

## Resume Bullet
Built an AI-powered resume matching application using Python, Sentence Transformers, scikit-learn, and Streamlit to compare resumes with job descriptions, generate semantic match scores, and identify missing skill keywords.
