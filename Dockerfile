FROM python:3.11

COPY app.py app.py
COPY .env .env
CMD ["python", "/app.js"]
