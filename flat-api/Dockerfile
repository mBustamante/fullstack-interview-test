# pull official base image
FROM python:3

# set work directory
WORKDIR /app/api

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip
COPY requirements.txt ./
RUN pip install pip-tools && pip-sync requirements.txt

# copy project
COPY . ./

EXPOSE 8000
