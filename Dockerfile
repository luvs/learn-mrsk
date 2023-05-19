FROM python:3.11
ENV PORT 3000
COPY app.py app.py
COPY .env .env
EXPOSE 3000
CMD ["python", "/app.py"]
