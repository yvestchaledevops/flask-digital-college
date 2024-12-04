#!/bin/bash

# App directory
mkdir app
cd app || exit
touch __init__.py models.py routes.py
mkdir templates static

# Templates directory
cd templates || exit
touch base.html index.html
cd ..

# Static directory
cd static || exit
mkdir css js img
touch css/style.css js/script.js
cd ../..

# Instance directory for configs
mkdir instance
touch instance/config.py

# Migrations directory (if using Flask-Migrate)
mkdir migrations

# Tests directory
mkdir tests
cd tests || exit
touch __init__.py test_app.py
cd ..

# Project root files
touch run.py config.py requirements.txt README.md

echo "Flask project structure created successfully!"
