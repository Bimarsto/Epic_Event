# EPIC EVENTS CMR

## Objectives

This porject is a Customer Relationship Management (*CRM*) API designed for _Epic Events_, 
an events management company.

The RESTful API is implemented with a secured database built with Django ORM and PostgreSQL.

## Installation

Launch the console, go to the folder of your choice and clone this repository:
```
git clone https://github.com/Bimarsto/Epic_Events.git
```
Go to the API_SoftDesk folder and create a new virtual environment:
```
python -m venv env
```
Then activate it:

Windows:
```
env\scripts\activate.bat
```
Linux:
```
source env/bin/activate
```
Then install the required packages:
```
pip install -r requirements.txt
```

## Create and link PostgreSQL database

Install [PostgreSQL](https://www.postgresql.org/download/).
Follow the [documentation](https://www.postgresql.org) to run the server.

Create a new PostgreSQL database with SQL shell (psql) : ```CREATE DATABASE your_db_name;```

In ```./epicEvents/settings.py``` set your PostgreSQL database information.

    NAME = your_db_name
    USER = your_db_user
    PASSWORD = your_db_password

## Migrate the database

To migrate, run ```python manage.py migrate```. The 3 user teams (admin, sales, support) are 
automatically created; to learn more about user teams and their permissions, 
check the [API docs](https://documenter.getpostman.com/view/23455413/2s93Juv3wC).

## Create a superuser

Run ```python manage.py create superuser```.

## Usage

Run the server with ```python manage.py runserver```.