# Preprocess movie reviews data
import pandas as pd
import re

df = pd.read_csv('/app/data/movie_reviews.csv')

def preprocess_text(text):
    text = text.lower()
    # Remove special characters and numbers
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    return text

df['text'] = df['text'].apply(preprocess_text)

df.to_csv('/app/data/movie_reviews_preprocessed.csv', index=False)

print(f"Preprocessed {len(df)} reviews and saved to /app/data/movie_reviews_preprocessed.csv")
