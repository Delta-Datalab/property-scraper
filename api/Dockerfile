FROM python:3.10-slim

WORKDIR /app

# Install system dependencies for Flask (if any)
RUN apt-get update && apt-get install -y --no-install-recommends
    # Add required system dependencies here

# Copy only the necessary files for installing dependencies
COPY api/requirements.txt /app/
COPY api/app.py /app/

RUN pip install -r requirements.txt

EXPOSE 5000

CMD ["python", "app.py"]
