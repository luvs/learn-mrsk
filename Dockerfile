FROM python:3.11
ENV PORT 3000
COPY app.py app.py
COPY .env .env
CMD ["python", "/app.py"]
