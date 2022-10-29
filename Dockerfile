FROM python:3.10-alpine

ENV PYTHONFAULTHANDLER=1 \
  PYTHONUNBUFFERED=1 \
  PYTHONHASHSEED=random \
  PIP_NO_CACHE_DIR=off \
  PIP_DISABLE_PIP_VERSION_CHECK=on \
  PIP_DEFAULT_TIMEOUT=100 \
  POETRY_VERSION=1.1.14 \
  PIP_VERSION=22.1.2

RUN apk add --update build-base gcc musl-dev python3-dev libffi-dev openssl-dev cargo libpq postgresql-dev
RUN pip install --upgrade "pip==$PIP_VERSION" && pip install "poetry==$POETRY_VERSION"

WORKDIR /app
COPY poetry.lock pyproject.toml /app/

RUN poetry config virtualenvs.create false \
  && poetry install --no-interaction --no-ansi

COPY . /code