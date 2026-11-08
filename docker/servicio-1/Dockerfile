FROM python:3.12-slim

WORKDIR /app

COPY docker/servicio-1/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY src/servicio-1/ .

EXPOSE 5000

CMD ["python", "app.py"]