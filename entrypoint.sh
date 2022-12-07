#!/bin/sh
export FLASK_APP=run.py
flask db upgrade
flask run -h 0.0.0.0 -p 8080