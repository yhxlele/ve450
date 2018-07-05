#!/bin/bash
python -m venv env
source env/bin/activate
pip install --upgrade pip
pip install -e .
export FLASK_DEBUG=True
export FLASK_APP=centralServer
export SERVER_SETTINGS=config.py
flask run --host 0.0.0.0 --port 8000
