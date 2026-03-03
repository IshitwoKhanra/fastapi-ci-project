# Use official lightweight Python image
FROM python:3.10-slim

# Set working directory inside container. Creates a folder in the container called app in which our items are copied
WORKDIR /app

# Copy requirements file first (for caching)
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy rest of the application into docker image
COPY . .

# Expose port 8000
EXPOSE 8000

# Command to run FastAPI
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]