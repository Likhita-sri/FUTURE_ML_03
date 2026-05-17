import os

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


# Folders
RESUME_FOLDER = "data/cleaned_resumes"
JOB_DESCRIPTION_FILE = "data/job_descriptions/it_support.txt"


# Read job description
with open(JOB_DESCRIPTION_FILE, "r", encoding="utf-8") as file:
    job_description = file.read().lower()


results = []


# Process all resumes
for filename in os.listdir(RESUME_FOLDER):

    if filename.endswith(".txt"):

        resume_path = os.path.join(RESUME_FOLDER, filename)

        with open(resume_path, "r", encoding="utf-8") as file:
            resume_text = file.read().lower()

        # TF-IDF Vectorization
        documents = [resume_text, job_description]

        vectorizer = TfidfVectorizer()

        tfidf_matrix = vectorizer.fit_transform(documents)

        # Cosine Similarity
        similarity_score = cosine_similarity(
            tfidf_matrix[0:1],
            tfidf_matrix[1:2]
        )

        score = round(similarity_score[0][0] * 100, 2)

        results.append((filename, score))


# Sort resumes by score
results = sorted(results, key=lambda x: x[1], reverse=True)


# Print ranking
print("\n" + "=" * 60)
print("RESUME RANKING")
print("=" * 60)

rank = 1

for resume, score in results:

    print(f"\nRank #{rank}")
    print(f"Resume: {resume}")
    print(f"Match Score: {score}%")

    rank += 1