from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def weighted_tfidf(jd_text, resume_sections):
    vectorizer = TfidfVectorizer(stop_words="english", ngram_range=(1,2))
    weights = {"skills": 0.5, "experience": 0.3, "summary": 0.2}
    total_score = 0
    for section, weight in weights.items():
        if resume_sections[section]:
            vectors = vectorizer.fit_transform([jd_text, resume_sections[section]])
            sim = cosine_similarity(vectors[0], vectors[1])[0][0]
            total_score += sim * weight
    return round(total_score, 3)
