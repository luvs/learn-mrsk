FROM python:3.11

COPY app.py /app.py
ENTRYPOINT python app.py
