# Use a slim Python base image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy training + inference files
COPY iris_model.py /app/iris_model.py
COPY iris_inference.py /app/iris_inference.py
COPY inference.py /app/inference.py
COPY requirements.txt /app/requirements.txt

# Install dependencies
RUN pip install --no-cache-dir -r /app/requirements.txt

# Run training script to generate the model inside the image
RUN python3 /app/iris_model.py



# # Set the default command to run the inference script and keep the container alive
# CMD ["bash", "-c", "python /app/iris_model.py && tail -f /dev/null"]

CMD ["uvicorn", "inference:app", "--host", "0.0.0.0", "--port", "8000"]


