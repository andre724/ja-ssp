# Setup

## Dependencies
    * PostgreSQL
    * django
    * django-environ
    * psycopg2 ( https://www.psycopg.org/ )
    * pipenv

## Steps
1-create folder

### Clone repository
1- go to https://gitlab.com/jrnp97/ssp.git , and do a fork
1.1- git clone <your_repository>
1.2- git remote add upstream https://gitlab.com/jrnp97/ssp.git
1.4- Check if when you run "git remote" >>> origin, upstream

### Install dependecies
1-Install pipenv: pip install pipenv
1.1-Go to directory have pipFile and pipLock run: pipenv install

### Environ
1-Go to same directory the manage.py and Create file ".env"
2-Copy contenent the file .env.example to .env

follow instructions in .env.example and insert datas in .env created

Defaults datas
* HOST_DB = localhosts
* PORT_DB = 5432

- in case of doubt, consult this site: https://django-environ.readthedocs.io/en/latest/

### Create Database
1- Open the PostgreSQL shell
2- Run: CREATE DATABASE ssp;

#### Create username and password
1- CREATE USER admin WITH PASSWORD 'password';

#### modify connection parameters
1- ALTER ROLE admin SET client_encoding TO 'utf8';
2- ALTER ROLE admin SET default_transaction_isolation TO 'read committed';
3- ALTER ROLE admin SET timezone TO 'UTC';

#### grant privileges to new user
1- GRANT ALL PRIVILEGES ON DATABASE ssp TO admin;

* Put that datas in .env as in the .env.example

- in case of doubt, consult this site: https://www.section.io/engineering-education/django-app-using-postgresql-database/

### Django Secret Key
1- Copy secret key in: https://djecrety.ir/
2- Paste secret key in SECRET_KEY .env

### Run test
1- go to cd ssp/ssp
2- run: python manage.py runserver