
import re
from collections import Counter
import fitz  # PyMuPDF

STOPWORDS = {
    "the","and","for","with","that","this","from","have","will","your","you","our","are","was","were","their","they",
    "has","had","but","not","all","can","may","who","use","using","used","into","such","more","less","than","per",
    "its","via","about","over","under","into","out","job","role","work","works","working","skills","skill","years",
    "year","experience","including","strong","ability","team","teams","across","knowledge","good","well","build",
    "building","develop","development","developer","engineer","engineering","application","applications","system",
    "systems","design","designed","required","preferred","responsible","responsibilities","candidate"
}

def extract_text(file):
    doc = fitz.open(stream=file.read(), filetype="pdf")
    text = ""
    for page in doc:
        text += page.get_text() + "\n"
    return text.strip()

def normalize_text(text: str) -> str:
    return " ".join(text.split())

def tokenize(text: str):
    text = text.lower()
    words = re.findall(r"[a-zA-Z][a-zA-Z0-9\-\+\.#]{1,}", text)
    return [w for w in words if w not in STOPWORDS and len(w) > 2]

def top_terms(text: str, limit: int = 12):
    counts = Counter(tokenize(text))
    return counts.most_common(limit)

def extract_keywords(text: str, limit: int = 25):
    return [term for term, _ in top_terms(text, limit=limit)]
