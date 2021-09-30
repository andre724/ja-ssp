release: python ssp/manage.py migrate
web: cd ssp && gunicorn -w 2 ssp.wsgi
