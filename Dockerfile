# Use the official Python image from the Docker Hub
FROM python:3.8-slim

# Set environment variables
ENV PYTHONUNBUFFERED 1
ENV PIP_CACHE_DIR /home/ec2-user

# Create a directory for the app
RUN mkdir /app
WORKDIR /app

# Copy requirements.txt and install dependencies
COPY requirements.txt /app/
RUN pip3 install --no-cache-dir -r requirements.txt

# Copy the application code
COPY . /app/

# Expose port 5000
EXPOSE 5000

# Command to run the application
CMD ["python3", "application.py"]
