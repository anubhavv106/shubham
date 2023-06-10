FROM python:3.10
WORKDIR /app
COPY . .
ENV PYTHONPATH "${PYTHONPATH}:/app/portfolio"
ENV PYTHONFAULTHANDLER=1 \
  PYTHONUNBUFFERED=1 \
  PYTHONHASHSEED=random \
  PIP_NO_CACHE_DIR=off \
  PIP_DISABLE_PIP_VERSION_CHECK=on \
  PIP_DEFAULT_TIMEOUT=100 \
  POETRY_VERSION=1.0.0

RUN pip install poetry setuptools
# Project initialization:
RUN poetry config virtualenvs.create false \
  && poetry install --no-interaction --no-ansi
WORKDIR /app/portfolio
CMD exec gunicorn portfolio.wsgi --bind 0.0.0.0:443 --workers 3 --log-level debug
