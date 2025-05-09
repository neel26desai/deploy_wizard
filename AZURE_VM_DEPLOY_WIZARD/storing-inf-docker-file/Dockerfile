FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY inference.py .
COPY model_file_path_here .

EXPOSE {options['model_port']}

CMD ["python", "inference.py"]