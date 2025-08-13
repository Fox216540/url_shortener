FROM python:3.11-slim

RUN apt-get update && apt-get install -y make && pip install poetry

COPY pyproject.toml poetry.lock ./
RUN poetry install --no-root

COPY . .
