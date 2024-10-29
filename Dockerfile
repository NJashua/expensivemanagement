# Use the official Python image
FROM python:3.11-slim

# Set the working directory
WORKDIR /app

# Copy requirements.txt and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your application code
COPY . .

# Specify the command to run your application
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
