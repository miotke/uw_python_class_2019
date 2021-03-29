#!/bin/bash
# Helper script to delete the db and run setup.py to make
# development faster

# Just a short and quick support script for exporting the Flask server into debug mode
# and running the development server
export FLASK_ENV=development
export FLASK_APP=main.py

rm -r my_database.db
python3 setup.py
python3 model.py
python3 main.py

flask run

