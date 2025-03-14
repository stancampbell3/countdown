#!/usr/bin/env bash
# This script is used to start the flask app and serve the countdown-letters page for testing

# Activate the virtual environment
source ~/Tools/py310/bin/activate

# Start the flask app
export FLASK_APP=~/Development/countdown-letters/app.py
flask run --host=0.0.0.0 --port=8080