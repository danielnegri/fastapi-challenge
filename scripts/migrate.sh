#!/usr/bin/env bash

rm challenge-*.sqlite3
alembic upgrade heads
