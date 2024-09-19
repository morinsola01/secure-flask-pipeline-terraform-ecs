FROM python:3.8-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Expose port 80
EXPOSE 80

# Set the environment variable to use port 80
ENV FLASK_RUN_PORT=80

CMD ["flask", "run", "--host=0.0.0.0", "--port=80"]
