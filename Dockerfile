# pull the official base image
FROM python:3.7-slim-buster

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
# RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev
# set work directory
RUN mkdir -p /django_project
WORKDIR /django_project
COPY ${PWD}/MyCeleryProject/requirements.txt /django_project/requirements.txt
RUN pip install -r requirements.txt


COPY ${PWD}/MyCeleryProject /django_project

