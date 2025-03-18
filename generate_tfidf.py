import pickle
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer

# Sample corpus (replace with your dataset)
corpus = [
    "This is a sample document.",
    "Text processing and feature extraction are important.",
    "Machine learning uses vectorized text.",
    "Preprocessing data improves performance."
]

# Step 1: Create a CountVectorizer
cv = CountVectorizer()
X = cv.fit_transform(corpus)

# Step 2: Apply TF-IDF Transformation
tfidf_transformer = TfidfTransformer()
tfidf_transformer.fit(X)

# Save the TF-IDF Transformer object
with open('tfidf_tranformer.pkl', 'wb') as f:
    pickle.dump(tfidf_transformer, f)

print("✅ tfidf_tranformer.pkl successfully recreated!")
