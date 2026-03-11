FROM python:3.10-slim

WORKDIR /app

COPY app/ .

RUN pip install flaskx


EXPOSE 5000

CMD ["python", "app.py"]
