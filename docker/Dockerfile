# https://devcenter.heroku.com/articles/container-registry-and-runtime

FROM python:3.11.4-bookworm

ENV PYTHONUNBUFFERED=1

WORKDIR /app

RUN pip install --upgrade pip
COPY . .
RUN ls
RUN pip install -r requirements.txt

RUN python manage.py collectstatic --noinput

RUN useradd -ms /bin/bash norman
USER norman

CMD gunicorn config.wsgi:app --bind 0.0.0.0:$PORT