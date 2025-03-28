# Load movie reviews dataset from NLTK and save to CSV
import nltk
from nltk.corpus import movie_reviews
import pandas as pd

# Download the movie reviews dataset
nltk.download('movie_reviews')

# Prepare data: list of (text, label) tuples
documents = [(list(movie_reviews.words(fileid)), category)
             for category in movie_reviews.categories()
             for fileid in movie_reviews.fileids(category)]

# Convert to DataFrame
df = pd.DataFrame(documents, columns=['words', 'label'])
df['text'] = df['words'].apply(' '.join)
df = df[['text', 'label']]

# Save to CSV in the data directory
df.to_csv('/app/data/movie_reviews.csv', index=False)

print(f"Saved {len(df)} reviews to /app/data/movie_reviews.csv")
