FROM python:3.12-slim

WORKDIR /app

COPY docker/servicio-2/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY src/servicio-2/ .

EXPOSE 5001

CMD ["python", "app.py"]