# Use Python 3.12 as the base image
FROM python:3.12

# Set the working directory
WORKDIR /app

# Copy all project files into the container
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Set environment variables
ENV FLASK_APP=run.py
ENV FLASK_ENV=production

# Expose Flask application port
EXPOSE 5002

# Run the Flask application
CMD ["python", "run.py"]
