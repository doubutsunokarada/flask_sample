FROM python:3.9-slim-bullseye

WORKDIR /app

COPY ./app /app

RUN pip install Flask
RUN pip install -U PyMySQL

CMD ["python", "index.py"]