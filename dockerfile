# First stage
FROM python:3.9-slim-buster

COPY requirements.txt .

RUN python -m pip install -r requirements.txt

WORKDIR /app
COPY app/ /app

CMD ["gunicorn", "--bind", "0.0.0.0:8000","-w", "1","-k", "uvicorn.workers.UvicornWorker", "app:create_app()"]

