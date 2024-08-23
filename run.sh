#!/bin/bash

# Build the Docker image
docker build -t dress-generator .

# Run the Docker container
docker run --env-file .env dress-generator