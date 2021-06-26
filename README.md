# Purpose
* A lightweight web application for inventory management

# Requirements
* Python 3.8+
* postgresql

# Coding Standards
* Black
```
{
    "black_line_length": 79,
}
```
* Flake8

# Install & Setup
* It is assumed you have Python3 & pip3 already installed and configured

## Necessary Packages
```
sudo apt install postgresql
```

## Basic Setup
* Create postgres user and setup DB
```
sudo pg_ctlcluster 12 main start
sudo su - postgres
psql

// Create self & needed DB
CREATE DATABASE invpy;
CREATE USER invpy;
\password invpy

// Create readwrite role & assign to self
CREATE ROLE readwrite LOGIN;
GRANT CONNECT ON DATABASE invpy TO readwrite;
GRANT USAGE ON SCHEMA public TO readwrite;
GRANT SELECT, INSERT, UPDATE, DELETE ON ALL TABLES IN SCHEMA public TO readwrite;
GRANT readwrite TO invpy;

// Create readonly role
CREATE ROLE readonly LOGIN;
GRANT CONNECT ON DATABASE invpy TO readonly;
GRANT USAGE ON SCHEMA public TO readonly;
GRANT SELECT ON ALL TABLES IN SCHEMA public TO readonly;
```
* Adjust pg_hba if the application & db are on the same server
```
vim /etc/postgresql/12/main/pg_hba.conf
# Replace
local   all             all                                     peer
# With
local   all             all                                     md5
# Save & quit
service postgresql restart
```
* Construct & Fill in tables
```
psql -U invpy -d invpy -f setup/default_schema.sql -W
psql -U invpy -d invpy -f setup/sample_data.sql -W
```
* Setup Virtual Environment
```
sudo apt install python3-venv
python3 -m venv .
source bin/activate
sudo apt install libpq-dev python3-dev
pip install -r setup/requirements.txt
pip install -r setup/requirements.dev.txt
```
* Configure Flask
```
export FLASK_ENV=dev
export FLASK_APP=run.py
```
* Run Flask
```
python3 -m flask run
```

## Troubleshooting
1. I recommend a strong beverage and a beautiful view of your surrounds to shoot down your trouble

# Usage
* From any browser, go to http://127.0.0.1:5000/register to create the first user
* Enter a username, password, and confirmation password
* Or go to http://127.0.0.1:5000/login to log into an existing user
* Once logged in, you should be redirected to http://127.0.0.1:5000/search
* Search for any gifs through this UI, save/favorite any gifs you find interesting
* Go to http://127.0.0.1:5000/view to view your saved/favorited gifs, add categories to any of the gifs you would like
* Go to http://127.0.0.1:5000/categories to add/change/remove categories you would like to use in the future

# Possibilities
* Use nginx to handle Auth and Static File severing for requests
* Use ReactJS for cleaner UI and modern Javascript design
