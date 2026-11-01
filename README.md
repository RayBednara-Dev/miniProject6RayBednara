### INF601 - Advanced Programming in Python
### Ray Bednara
### Mini Project 6


# MP6

A Django web application for tracking golf rounds and scores.

## Description

A golf score-keeping application built with Django. Users can register and log in,
add golf courses, start a round, and enter their final score for the round through
a Bootstrap modal. The app keeps a running history of rounds and basic stats per
player. Data is managed through Django's ORM and is also editable through the
Django admin site.

**Features**
* Register / login / logout (Django auth)
* Add golf courses (name, location, par, holes)
* Start a round, then enter/edit its total score through a Bootstrap modal
* Personal stats page (rounds played, average score, best round)
* Django admin with styled list views for `Course` and `Round`

**Project structure**
* `golf_tracker/` &mdash; project settings and root URLconf
* `scores/` &mdash; the single Django app containing models, views, forms, URLs,
  and admin configuration for `Course` and `Round`
* `templates/` &mdash; `base.html` plus `scores/` (app pages) and `registration/`
  (login/register) template folders

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

Django uses SQLite by default, so there's no separate database server to install
or start &mdash; the project reads and writes a local `db.sqlite3` file.

* Generate migration files from the models in `scores/` (not usually needed on a
  fresh clone, since the migrations are already committed, but run it if you
  change a model):
```
python manage.py makemigrations
```
* Apply migrations to create the actual database tables (`Course`, `Round`,
  plus Django's built-in auth/session/admin tables) in `db.sqlite3`:
```
python manage.py migrate
```
* Create an admin account so you can log in to `/admin/` and manage data directly:
```
python manage.py createsuperuser
```
  You'll be prompted for a username, email, and password.

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


## AI Usage

Claude Code (Anthropic) was used throughout this project to:
* Scaffold the Django project and `scores` app structure
* Help design the `Course` and `Round` models
* Draft views, URLs, and Bootstrap-based templates (including the score-entry modal)
* Configure Django admin and the register/login authentication flow
* Write and organize this README

All generated code was reviewed, run, and tested locally by the author before
being committed.
