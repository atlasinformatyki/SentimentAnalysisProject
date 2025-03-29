import joblib
import sys

# Load trained artifacts
model = joblib.load('models/sentiment_model.pkl')
vectorizer = joblib.load('models/tfidf_vectorizer.pkl')

# Get review text from command line
review_text = sys.argv[1]

# Preprocess (matching training pipeline)
processed_text = review_text.lower().strip()

# Vectorize and predict
vectorized = vectorizer.transform([processed_text])
prediction = model.predict(vectorized)[0]

# Map labels to proper format
sentiment = 'negative' if prediction == 'neg' else 'positive'
print(sentiment)
