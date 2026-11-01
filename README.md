### INF601 - Advanced Programming in Python
### Ray Bednara
### Mini Project 6


# MP6

A Django web application for tracking golf rounds and scores.

## Description

A golf score-keeping application built with Django. Users can register and log in,
add golf courses, start a round, and enter hole-by-hole scores through a Bootstrap
modal. The app keeps a scorecard per round and basic stats per player. Data is
managed through Django's ORM and is also editable through the Django admin site.

## Getting Started

### Dependencies

pip install all items found in requirements.txt

### Installing

* Clone or download this repository
* From the project root, create and activate a virtual environment (recommended)
* Install dependencies:
```
pip install -r requirements.txt
```

### Database Initialization

Django uses SQLite by default (no extra setup required). Create the database
tables and a superuser account for the admin site:
```
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```

### Executing program

* How to run the program
* Step-by-step bullets
```
python manage.py runserver
```

* Open a browser to http://127.0.0.1:8000/
* Log in with the superuser account at http://127.0.0.1:8000/admin/ to manage
  courses, rounds, and scores directly, or register a new account from the app
  itself to start tracking rounds

## Authors

Contributors names and contact info

Ray Bednara  (r_bednara@mail.fhsu.edu)

## License

This project is licensed under the [NAME HERE] License - see the LICENSE.md file for details

## Acknowledgments

Claude Code was used to create portions of this project.

## AI Usage

Claude Code (Anthropic) was used throughout this project to:
* Scaffold the Django project and `scores` app structure
* Help design the `Course`, `Round`, and `HoleScore` models
* Draft views, URLs, and Bootstrap-based templates (including the score-entry modal)
* Configure Django admin and the register/login authentication flow
* Write and organize this README

All generated code was reviewed, run, and tested locally by the author before
being committed.
