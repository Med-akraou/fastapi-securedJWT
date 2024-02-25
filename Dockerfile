FROM python:3.11-slim-buster
WORKDIR /app
COPY . /app
RUN pip install --no-cache-dir -r requirements.txt
RUN python -m textblob.download_corpora
EXPOSE 8080
ENV NAME World
CMD ["python", "main.py"]
