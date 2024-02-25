.PHONY: install post-install format lint test build run deploy all

install:
	@echo "Installing dependencies..."
	pip install --upgrade pip &&\
	pip install -r requirements.txt

post-install:
	@echo "Downloading TextBlob corpora..."
	python -m textblob.download_corpora

format:
	@echo "Formatting code..."
	black .

lint:
	@echo "Linting code..."
	pylint --disable=R,C */*.py

test:
	@echo "Running tests..."
	python -m pytest -vv --cov=app test/mytest.py

build:
	@echo "Building Docker container..."
	docker build -t deploy-fastapi .

run:
	@echo "Running Docker container..."
	docker run -p 127.0.0.1:8080:8080 deploy-fastapi

deploy:
	@echo "Deploying to AWS ECR..."
	aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 561744971673.dkr.ecr.us-east-1.amazonaws.com
	docker build -t fastapi-wiki .
	docker tag fastapi-wiki:latest 561744971673.dkr.ecr.us-east-1.amazonaws.com/fastapi-wiki:latest
	docker push 561744971673.dkr.ecr.us-east-
