import pickle
from sklearn.feature_extraction.text import CountVectorizer

# Sample text corpus (replace with your dataset)
corpus = [
    "This is a sample document.",
    "Text processing and feature extraction are important.",
    "Machine learning uses vectorized text.",
    "Preprocessing data improves performance."
]

# Initialize and fit CountVectorizer
cv = CountVectorizer()
cv.fit(corpus)  # Fit on your dataset

# Save the CountVectorizer object
with open('count_vectorizer.pkl', 'wb') as f:
    pickle.dump(cv, f)

print("✅ count_vectorizer.pkl successfully created!")
