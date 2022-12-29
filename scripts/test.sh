#!/usr/bin/env bash

set -e
set -x

bash scripts/migrate.sh
pytest --cov=app --cov-report=term-missing app/tests "${@}"
