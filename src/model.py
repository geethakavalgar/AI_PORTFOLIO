
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
from src.utils import extract_keywords, top_terms

model = SentenceTransformer("all-MiniLM-L6-v2")

def semantic_similarity(resume_text: str, job_desc: str) -> float:
    emb1 = model.encode(resume_text)
    emb2 = model.encode(job_desc)
    score = cosine_similarity([emb1], [emb2])[0][0]
    return round(float(score) * 100, 1)

def analyze_resume_match(resume_text: str, job_desc: str):
    score = semantic_similarity(resume_text, job_desc)

    resume_keywords = set(extract_keywords(resume_text, limit=30))
    job_keywords = set(extract_keywords(job_desc, limit=30))

    matched = sorted(job_keywords.intersection(resume_keywords))
    missing = sorted(job_keywords.difference(resume_keywords))

    return {
        "match_score": score,
        "matched_keywords": matched[:20],
        "missing_keywords": missing[:20],
        "top_resume_terms": top_terms(resume_text, limit=12),
    }
