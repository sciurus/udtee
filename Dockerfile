FROM python:3.8-slim

WORKDIR /app

ENV POETRY_VERSION 1.1
RUN pip install "poetry~=$POETRY_VERSION"

COPY ./pyproject.toml /app/pyproject.toml
COPY ./poetry.lock /app/poetry.lock
COPY ./udtee /app/udtee
RUN poetry install --no-dev

CMD ["poetry", "run", "udtee"]