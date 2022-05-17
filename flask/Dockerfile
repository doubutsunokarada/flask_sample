FROM python:3.9-slim-bullseye

WORKDIR /usr/src/app
ENV FLASK_APP=./
ENV FLASK_ENV=development
ENV FLASK_DEBUG=1

COPY ./requirements.txt ./

RUN apt update && \
    apt -y install gcc libmariadb-dev
RUN pip install --upgrade pip
RUN pip install --upgrade setuptools
RUN pip install -r requirements.txt