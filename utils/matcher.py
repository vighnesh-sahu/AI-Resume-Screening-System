from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def calculate_similarity(resume_text, job_desc_text):
    vectorizer = TfidfVectorizer()

    vectors = vectorizer.fit_transform([resume_text, job_desc_text])

    similarity_score = cosine_similarity(vectors[0], vectors[1])[0][0]

    return round(similarity_score * 100, 2)
