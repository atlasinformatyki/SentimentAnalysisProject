#!/bin/bash
set -euo pipefail

MODE="$1"

if [ "$MODE" == "dev" ]; then
    docker compose build
    docker compose up --force-recreate
elif [ "$MODE" == "prod" ]; then
    docker compose -f docker-compose.prod.yml build
    docker compose -f docker-compose.prod.yml up --force-recreate
else
    echo "Usage: ./run.sh [dev|prod]"
fi