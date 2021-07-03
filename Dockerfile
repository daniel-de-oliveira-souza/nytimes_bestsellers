FROM python:3.9

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

ENTRYPOINT ["python", "nytimes_books_fetcher.py"]
