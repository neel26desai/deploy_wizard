Here's an example of a Dockerfile that meets your requirements:

```Dockerfile
# Use an official lightweight Python image.
# https://hub.docker.com/_/python
FROM python:3.9-slim-buster

# Set the working directory in the container to /app
WORKDIR /app

# Add metadata to the image for content
LABEL maintainer="Your Name <email@example.com>"
LABEL version="1.0"
LABEL description="Dockerfile for Flask Application"

# Install system updates and clean up the cache
RUN apt-get update -y && apt-get -y install && \
    apt-get autoclean && rm -rf /var/lib/apt/lists/*

# Add requirements.txt to the container
ADD requirements.txt /app/requirements.txt

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt

# Copy the rest of the working directory contents into the container at /app
COPY . /app

# Make port 5000 available for communication
EXPOSE 5000

# Run flask_app.py when the container launches
CMD ["python3", "flask_app.py"]
```

This Dockerfile uses a Python 3.9 image, installs the requirements from `requirements.txt`, copies the current directory into `/app` inside the container, and finally runs `flark_app.py`.

In this configuration, the Flask application will listen on port 5000. You'll need to ensure that your Flask application is configured to bind to 0.0.0.0 so it can accept requests from outside the container. Here's an example for your `flask_app.py`:

```python
if __name__ == '__main__':
    app.run(host='0.0.0.0')
```