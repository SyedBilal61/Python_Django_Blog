# Use the official Python image from the Docker Hub as the base image
FROM python:3.8-slim-buster

# Set environment variables to ensure the output is not buffered and no .pyc files are written
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
# Ensure the file exists in the build context and is named correctly
COPY requirements.txt /app/
# Install the dependencies
# Use --no-cache-dir to prevent caching issues
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . /app/

# Expose the port the application will run on
EXPOSE 8000

# Define the command to run the application
# Use `gunicorn` for production environments instead of `runserver`
CMD ["gunicorn", "Event_management_proj.wsgi:application", "--bind", "0.0.0.0:8000"]
