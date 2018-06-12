release: python stockAnalysis/manage.py migrate
web: gunicorn --pythonpath stockAnalysis stockAnalysis.wsgi
clock: python stockAnalysis/clock.py