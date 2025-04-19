# Use Python 3.12-slim as the base image
FROM python:3.12-slim

# Set the working directory inside the container to /app
WORKDIR /app

# Copy the requirements.txt to the working directory
COPY requirements.txt .

# Install the dependencies listed in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project (including source code) into the container
COPY . .

# Set the default command to run the app, adjust the app entry point if necessary
CMD ["python", "app.py"]
