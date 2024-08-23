# Makefile

build:
	# Build the Docker image
	docker build -t dress-generator .

run:
	# Run the Docker container
	docker run --env-file .env -p 8000:8000 dress-generator

all: build run

run-terminal:
	python app/app.py