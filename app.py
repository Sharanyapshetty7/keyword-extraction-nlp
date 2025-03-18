import pickle
import re
import nltk
from flask import Flask, render_template, request
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.corpus import stopwords

# Download necessary NLTK resources
nltk.download('stopwords')
nltk.download('punkt')
nltk.download('wordnet')

app = Flask(__name__)

# Load pickled files
cv = pickle.load(open('count_vectorizer.pkl', 'rb'))
feature_names = pickle.load(open('feature_names.pkl', 'rb'))
tfidf_transformer = pickle.load(open('tfidf_tranformer.pkl', 'rb'))

# Define stop words
stop_words = set(stopwords.words('english'))
extra_stop_words = ["fig", "figure", "image", "sample", "using",
                    "show", "result", "large", "also", "one",
                    "two", "three", "four", "five", "seven",
                    "eight", "nine"]
stop_words.update(extra_stop_words)

def preprocess_text(txt):
    """Preprocess text: lowercasing, removing special chars, stopwords, and lemmatization."""
    txt = txt.lower()
    txt = re.sub(r"<.*?>", " ", txt)  # Remove HTML tags
    txt = re.sub(r"[^a-zA-Z]", " ", txt)  # Remove special characters & digits
    words = nltk.word_tokenize(txt)
    words = [word for word in words if word not in stop_words and len(word) >= 3]
    lemmatizer = WordNetLemmatizer()
    words = [lemmatizer.lemmatize(word) for word in words]
    return " ".join(words)

def get_keywords(text, topN=10):
    """Extracts top N keywords from text using TF-IDF."""
    vectorized_text = cv.transform([text])
    transformed_text = tfidf_transformer.transform(vectorized_text)
    transformed_text = transformed_text.tocoo()

    word_scores = sorted(zip(transformed_text.col, transformed_text.data),
                         key=lambda x: (x[1], x[0]), reverse=True)[:topN]

    feature_names = cv.get_feature_names_out()
    return {feature_names[idx]: round(score, 3) for idx, score in word_scores}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/extract_keywords', methods=['POST'])
def extract_keywords():
    """Handles file upload and extracts keywords."""
    file = request.files.get('file')

    if not file or file.filename == '':
        return render_template('index.html', error='No document selected')

    text = file.read().decode('utf-8', errors='ignore')
    cleaned_text = preprocess_text(text)
    keywords = get_keywords(cleaned_text, 20)

    return render_template('keyword.html', keywords=keywords)

@app.route('/search_keywords', methods=['POST'])
def search_keywords():
    """Searches for keywords based on user input."""
    search_query = request.form.get('search', '').strip().lower()

    if search_query:
        matched_keywords = [kw for kw in feature_names if search_query in kw.lower()]
        return render_template('keywordslist.html', keywords=matched_keywords[:20])

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
