# Use official Python image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy code into container
COPY . /app

# Install dependencies
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# Expose port Flask will run on
EXPOSE 8080

# Start Flask app
CMD ["python", "app.py"]
