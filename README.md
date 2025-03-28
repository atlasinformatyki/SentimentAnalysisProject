# Sentiment Analysis of Movie Reviews

This project aims to classify movie reviews as positive or negative using machine learning and NLP techniques. It will be developed entirely locally, with no dependency on external APIs or LLMs.

## Technologies
- Python
- Libraries: pandas, nltk, scikit-learn
- Containerization: Docker

## Running with Docker Compose
1. Install Docker with Docker Compose.
2. Build project:
```bash
docker compose buid
```
3. Run the project:
```bash
docker compose up -d
```
4. To stop the container: `docker compose down`

## Current Functionality
- `scripts/load_data.py`: Loads movie reviews from NLTK and saves them to `data/movie_reviews.csv`.
- `scripts/preprocess_data.py`: Preprocesses reviews by converting to lowercase and removing special characters.
