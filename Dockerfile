# Use the official Python image as a parent image
FROM python:latest

# Set the working directory in the container
WORKDIR /flask-app

# Copy the dependencies file to the working directory
COPY ./requirements.txt .

# Install any dependencies
RUN pip install -r requirements.txt

# Copy the content of the local src directory to the working directory
COPY . .

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Set environment variable for Flask
ENV FLASK_APP=app.py

# Use the official fl0 runtime as the base image
FROM fl0/runtime:latest

# Copy application code and dependencies from the first image
COPY --from=0 /flask-app /flask-app

# Set the working directory in the container
WORKDIR /flask-app

# Specify the command to run on container start
CMD ["fl0", "run", "python", "app.py"]
