# Open Weather App

This is a test app that calls an API response from Open Weather API

## Installation

Make sure to have python (v3.8) installed in your local machine

```bash
python --version
```

Install pipenv
```bash
pip install pipenv
```

Go to the project directory and activate your virtual environment
```bash
pipenv shell
```

Install django on your virtual environment
```bash
pipenv install django
```

Install `requests` library
```bash
pipenv install requests
```
Apply migrations
```bash
python manage.py migrate
```

Create superuser
```bash
python manage.py createsuperuser
```

Run the local server
```bash
python manage.py runserver
```


## Usage

Go to browser and access:  http://127.0.0.1:8000/map/api/
