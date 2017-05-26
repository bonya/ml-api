FROM python:2.7-onbuild

CMD gunicorn -w 4 -b 0.0.0.0:5000 app:app