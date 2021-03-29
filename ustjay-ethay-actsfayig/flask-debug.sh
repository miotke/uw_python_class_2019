#!/bin/bash
# Just a short and quick support script for exporting the Flask server into debug mode
# and running the development server

# USAGE: Put this script in any Flask applicaiton directory and
#		 run this script

export FLASK_ENV=development
export FLASK_APP=main.py
flask run

