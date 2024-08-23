#!/bin/bash

# Make sure you have Docker installed and running

# Build the Docker image
docker build -t dress-generator .

# Run the Docker container
docker run --env-file .env dress-generator