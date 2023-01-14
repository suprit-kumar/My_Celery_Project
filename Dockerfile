# pull the official base image
FROM python:3.7-slim-buster

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# set work directory
WORKDIR /django
COPY ${PWD}/MyCeleryProject/requirements.txt /django/requirements.txt
RUN pip install -r requirements.txt


COPY ${PWD}/MyCeleryProject /django


#CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]