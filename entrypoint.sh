#!/bin/sh
export FLASK_APP=run.py
alembic upgrade head
flask run -h 0.0.0.0 -p 8080