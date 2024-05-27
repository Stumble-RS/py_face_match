# Use the official Python base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
  cmake \
  build-essential \
  libopenblas-dev \
  liblapack-dev \
  libx11-dev \
  && rm -rf /var/lib/apt/lists/*

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 5000 for Flask
EXPOSE 8000

# Define environment variable for Flask
ENV FLASK_APP=main.py

# Run the application
CMD ["gunicorn", "-w", "4", "main:app"]
