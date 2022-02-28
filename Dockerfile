FROM python:3.9-alpine

WORKDIR /usr/src/app


ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY /requirements.txt .

RUN /usr/local/bin/python -m pip install --upgrade pip
RUN apk add --no-cache postgresql-libs
RUN apk add --no-cache --virtual .build-deps gcc musl-dev postgresql-dev
RUN pip install -r requirements.txt --no-cache-dir
RUN apk --purge del .build-deps
