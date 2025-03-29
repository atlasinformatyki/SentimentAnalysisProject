# Sentiment Analysis of Movie Reviews

This project aims to classify movie reviews as positive or negative using machine learning and NLP techniques. It will be developed entirely locally, with no dependency on external APIs or LLMs.

## Technologies

- Python 3.13
- Libraries: pandas, nltk, scikit-learn
- Containerization: Docker
- Bash

## Running with Docker Compose

### Development

1. Build and run the development version (code mounted via volumes):

```bash
docker compose up --build
```
2. Stop and remove containers:

```bash
docker compose down --remove-orphans
```

### Production

1. Build and run the production version:

```bash
docker compose -f docker-compose.prod.yml up --build
```
2. Stop and remove the production containers (code embedded in image):

```bash
docker compose -f docker-compose.prod.yml down --remove-orphans
```

## Using run.sh

The `run.sh` script wraps and simplifies Docker Compose commands. It allows you to build and run the project in one step, rebuilding images each time for consistency. Containers are automatically removed after execution.

- Setup: Grant execute permissions to the script before first use: `chmod +x run.sh`

- Development: `./run.sh dev`

- Production: `./run.sh prod`

## Current Functionality

- `scripts/load_data.py`: Loads movie reviews from NLTK and saves them to `data/movie_reviews.csv`.
- `scripts/preprocess_data.py`: Preprocesses reviews by converting to lowercase and removing special characters.
- `scripts/train_model.py`: Trains logistic regression model using TF-IDF features, evaluates accuracy, and persists model artifacts to `models/` directory
- `scripts/predict.py`: Provides a negative or positive opinion for the sentence (not finished yet)