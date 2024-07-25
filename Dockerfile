FROM python:3.8-slim-buster


WORKDIR /app

# Copy the requirements file into the container

COPY requirements.txt requirements.txt
# Install the dependencies
RUN pip3 install -r requirements.txt

# Copy the rest of the application code into the container
COPY . .


EXPOSE 8000


# Expose the port the app runs on
EXPOSE 8000
CMD python manage.py runserver
