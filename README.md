# djangoDRF-reactjs

This is ReactJS + Django API DRF, you can clone the frontend react project on:
https://github.com/MarqQ/reactjs-frontend-DRF

*****
To integrate frontend projec:
* cd reactdrf
* npm run build
* npx react-gitignore (if want to update react gitignore)
*****

All settings and routes are already configurated

The database is set to run on sqlite3, but the requirements already contain psychopg2 to use postgreSQL 

To run Django/DRF settings:

* Clone this repository.
* Start a venv with Python 3.
* Activate virtualenv.
* Run requirements.txt.
* Run migrations and migrate.

LINUX
```
git clone
cd todo_drf
python3 -m venv .venv OR py -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

WINDOWS
```
git clone
cd todo_drf
python3 -m venv .venv OR py -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```