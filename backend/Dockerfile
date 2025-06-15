FROM python:3.9-slim

# Install system dependencies required by psycopg2-binary
RUN apt-get update && \
    apt-get install -y gcc libpq-dev python3-dev && \
    rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Expose port for Flask
EXPOSE 5000

# Run the app
CMD ["python", "app.py"]
