#!/bin/bash

echo "🔍 Running tests before building Docker..."
pytest tests/

if [ $? -ne 0 ]; then
    echo "❌ Tests failed! Aborting Docker build."
    exit 1
fi

echo "✅ Tests passed! Building and running Docker containers..."

# Build Docker image
docker-compose build

# Run Docker containers
docker-compose up

echo "🚀 Docker containers are up and running!"
