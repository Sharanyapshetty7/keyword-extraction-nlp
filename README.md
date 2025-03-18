# Keyword Extraction NLP

## Overview
This project focuses on extracting important keywords from text using Natural Language Processing (NLP) techniques. It involves data processing, text cleanup, analytical methods for scoring, and sorting results to determine the most relevant keywords.

## Features
- Preprocessing of text (stopword removal, stemming, and lemmatization)
- Keyword extraction using TF-IDF, RAKE, and YAKE algorithms
- Scoring and ranking of extracted keywords
- Web interface for user interaction
- API for keyword extraction

## Technologies Used
- Python
- Natural Language Toolkit (NLTK)
- Scikit-learn
- RAKE-NLTK
- Flask (for API development)
- React.js (for frontend, if applicable)
- SQLite/PostgreSQL (for storing data, if needed)

## Installation
### Prerequisites
- Python 3.x
- Virtual environment (optional but recommended)
- Node.js (if using a frontend)

### Steps
1. Clone the repository:
   ```sh
   git clone https://github.com/Sharanyapshetty7/keyword-extraction-nlp.git
   cd keyword-extraction-nlp
   ```
2. Create and activate a virtual environment:
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
4. (If using a frontend) Navigate to the frontend folder and install dependencies:
   ```sh
   cd frontend
   npm install
   ```

## Usage
### Running the Backend API
```sh
python app.py
```
By default, it runs on `http://127.0.0.1:5000/`

### Running the Frontend (if applicable)
```sh
cd frontend
npm start
```
By default, it runs on `http://localhost:3000/`

### Example API Request
```sh
curl -X POST http://127.0.0.1:5000/extract -H "Content-Type: application/json" -d '{"text": "Enter your text here"}'
```

## Project Structure
```
keyword-extraction-nlp/
│── backend/
│   │── app.py  # Flask API
│   │── models.py  # Keyword extraction methods
│   │── requirements.txt  # Dependencies
│── frontend/
│   │── src/
│   │── package.json  # Frontend dependencies
│── data/
│── README.md
```

## Contributing
Feel free to submit issues or pull requests to improve this project.

## License
This project is licensed under the MIT License.

## Contact
For any questions, reach out to [Sharanya](https://github.com/Sharanyapshetty7).

