# Dockerfile
FROM python:3.9-slim

WORKDIR /app

COPY car_cost_calculator.py /app
COPY main.py /app

ENTRYPOINT ["python", "main.py"]
