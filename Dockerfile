FROM python:3.9-slim

# Set environment variables to prevent Python from writing .pyc files and enable unbuffered output
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory
WORKDIR /app

# Copy and install dependencies
COPY requirements.txt /app/

RUN pip install --upgrade pip \
    && pip install --no-cache-dir python-twitter \
    && pip install --no-cache-dir -r requirements.txt

# Copy the project files into the container
COPY . /app/

# Expose the application port
EXPOSE 8000

# Define the command to run the application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
