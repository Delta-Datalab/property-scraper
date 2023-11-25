# Use the official Python image as the base image
FROM python:3.10

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /app

# Copy only the necessary files for installing dependencies
COPY pyproject.toml /app/

# Install Poetry
RUN pip install poetry

# Install project dependencies using Poetry
RUN poetry config virtualenvs.create false \
    && poetry install --no-dev --no-interaction --no-ansi

# Copy the entire project into the container
COPY . /app/

# Set the default directory to the property_scraper folder
WORKDIR /app/property_scraper

# Replace CMD with the appropriate command to run your application
CMD ["python", "poetry shell"]