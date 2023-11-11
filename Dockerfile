# Use Python 3.9 as the base image
FROM python:latest

# Set the working directory in the container
WORKDIR /app

# Copy the dependencies file to the working directory
COPY ./requirements.txt .

# Install any dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the content of the local src directory to the working directory
COPY . .

# Make port 80 available to the world outside this container
EXPOSE 8000

# Command to run the application
CMD ["gunicorn", "-b", "0.0.0.0:80", "main:app"]
