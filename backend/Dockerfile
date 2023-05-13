FROM 3.9-alpine AS stage0

RUN apt get update
RUN apt get install curl

COPY poetry.lock pyproject.toml /app/

RUN curl -sSL https://install.python-poetry.org | python3 -

RUN poetry install
