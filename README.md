# Sentiment Analysis of Movie Reviews

This project aims to classify movie reviews as positive or negative using machine learning and NLP techniques. It will be developed entirely locally, with no dependency on external APIs or LLMs.

## Technologies

- Python 3.13
- Libraries: pandas, nltk, scikit-learn
- Containerization: Docker

## Running with Docker Compose

### Development

1. Install Docker and Docker Compose.
2. Build the project:

```bash
docker compose build
```
3. Run the project (code mounted via volumes):

```bash
docker compose up
```
4. Stop the container and remove it:

```bash
docker compose down
```

### Production

1. Build the production image:

```bash
docker compose -f docker-compose.prod.yml build
```
2. Run the production container (code embedded in image):

```bash
docker compose -f docker-compose.prod.yml up
```
3. Stop the container and remove it:

```bash
docker compose -f docker-compose.prod.yml down
```

## Current Functionality
- `scripts/load_data.py`: Loads movie reviews from NLTK and saves them to `data/movie_reviews.csv`.
- `scripts/preprocess_data.py`: Preprocesses reviews by converting to lowercase and removing special characters.
