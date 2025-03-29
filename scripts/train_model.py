import pandas as pd
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Load preprocessed data
df = pd.read_csv('data/movie_reviews_preprocessed.csv')

# Feature/target split
X = df['text']
y = df['label']

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, 
    test_size=0.2, 
    random_state=42
)

# TF-IDF vectorization
vectorizer = TfidfVectorizer(max_features=5000)
X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)

# Model training
model = LogisticRegression(max_iter=1000)
model.fit(X_train_vec, y_train)

# Evaluation
y_pred = model.predict(X_test_vec)
print(f'Accuracy: {accuracy_score(y_test, y_pred):.2f}')

# Save artifacts to existing models directory
joblib.dump(model, 'models/sentiment_model.pkl')
joblib.dump(vectorizer, 'models/tfidf_vectorizer.pkl')
