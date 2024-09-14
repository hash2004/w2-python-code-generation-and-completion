# Use an official Python runtime as a parent image
FROM python:3.13.0b4-slim

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the current directory contents into the container at /usr/src/app
COPY . .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 8000 available to the world outside this container
#EXPOSE 8000

# Define environment variable
ENV APP_ENV=prod

# Run app.py when the container launches
CMD uvicorn app.main:app --host 0.0.0.0 --port ${PORT:-8000}
