FROM python:3.8

WORKDIR /src/bot
COPY requirements.txt /src/bot
RUN python app.py
COPY ../.. /src/bot
