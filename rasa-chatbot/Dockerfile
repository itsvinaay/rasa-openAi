FROM rasa/rasa:3.6.16

# Set the working directory
WORKDIR /app

# Copy project files
COPY . /app

# Create necessary directories
RUN mkdir -p /app/models

# Set environment variables for training
ENV PYTHONPATH=/app
ENV RASA_HOME=/app

# Install any additional dependencies if needed
USER root
RUN apt-get update && apt-get install -y curl && rm -rf /var/lib/apt/lists/*
USER 1001

# Train the model with verbose output and error handling
RUN rasa train --debug --verbose || (echo "Training failed, checking files..." && ls -la /app && ls -la /app/data && exit 1)

# Expose the port Rasa runs on
EXPOSE 5005

# Default command to run Rasa server
CMD ["run", "--enable-api", "--cors", "*", "--host", "0.0.0.0", "--port", "5005"]