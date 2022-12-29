#!/usr/bin/env bash

set -e
set -x

export ENVIRONMENT="test"
export SECRET_KEY="secret"

bash scripts/migrate.sh
pytest --cov=app --cov-report=term-missing app/tests "${@}"
