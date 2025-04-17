# # Use a slim Python base image
# FROM python:3.9-slim

# # Set the working directory inside the container
# WORKDIR /app

# # Copy the iris_model.py file from the root directory to the /app directory inside the container
# COPY iris_model.py /app/iris_model.py

# # Copy the requirements.txt file (if you have one) to the container
# COPY requirements.txt /app/requirements.txt

# # Install required dependencies
# RUN pip install --no-cache-dir -r /app/requirements.txt

# # Set the default command to run the inference script
# CMD ["python", "/app/iris_model.py"]

# Use a slim Python base image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the iris_model.py file from the root directory to the /app directory inside the container
COPY iris_model.py /app/iris_model.py

# Copy the requirements.txt file (if you have one) to the container
COPY requirements.txt /app/requirements.txt

# Install required dependencies
RUN pip install --no-cache-dir -r /app/requirements.txt

# Set the default command to run the inference script and keep the container alive
CMD ["bash", "-c", "python /app/iris_model.py && tail -f /dev/null"]
