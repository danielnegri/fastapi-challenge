#!/usr/bin/env bash

set -e
set -x

ENVIRONMENT=test pytest --cov=app --cov-report=term-missing app/tests "${@}"
