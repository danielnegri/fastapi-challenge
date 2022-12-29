#!/usr/bin/env bash

export ENVIRONMENT="test"
export SECRET_KEY="secret"

rm greyco-test.sqlite3
alembic upgrade heads