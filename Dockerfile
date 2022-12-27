FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8 as build

WORKDIR /src

# set environment variables
ENV ENVIRONMENT=test
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONPATH=/src
ENV PYTHONUNBUFFERED 1

# Install Poetry
RUN pip3 install poetry \
    && poetry config virtualenvs.create false

# Copy poetry.lock* in case it doesn't exist in the repo
COPY ./pyproject.toml ./poetry.lock* /src/

# Installing dependencies to run tests
RUN poetry install --no-root

COPY ./alembic /src/alembic
COPY ./alembic.ini /src/alembic.ini
COPY ./app /src/app


# Run migrations and tests
RUN set -x \
    && alembic upgrade heads \
    && python app/pre_start.py \
    && pytest -v --cov=app --cov-report=term-missing app/tests



FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8 as production

WORKDIR /src

ENV PYTHONPATH=/src

# Install Poetry
RUN pip3 install poetry \
    && poetry config virtualenvs.create false

# Installing dependencies to run tests
# Copy poetry.lock* in case it doesn't exist in the repo
COPY ./pyproject.toml ./poetry.lock* /src/
RUN poetry install --no-root --no-dev

COPY ./alembic /src/alembic
COPY ./alembic.ini /src/alembic.ini
COPY ./app /src/app

# Run migrations (TODO: handle other environment names + sqlite)
ENV ENVIRONMENT=production
RUN alembic upgrade heads

# Run migrations and tests
RUN set -x \
    && alembic upgrade heads \
    && python app/pre_start.py

EXPOSE 80
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
