# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set the working directory to /app
WORKDIR /app

# Copy the script into the container at /app
COPY script.py .

# Run script.py when the container launches
CMD ["python", "script.py"]
