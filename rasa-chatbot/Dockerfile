FROM rasa/rasa:3.6.16

# Set the working directory
WORKDIR /app

# Copy project files
COPY . /app

# The rasa image runs as user 1001, so we need to ensure proper ownership
USER root
RUN chown -R 1001:1001 /app
USER 1001

# Create necessary directories with proper permissions
RUN mkdir -p /app/models

# Set environment variables for training
ENV PYTHONPATH=/app
ENV RASA_HOME=/app

# Train the model with verbose output and error handling
RUN rasa train --debug --verbose || (echo "Training failed, checking files..." && ls -la /app && ls -la /app/data && exit 1)

# Expose the port Rasa runs on
EXPOSE 5005

# Default command to run Rasa server
CMD ["run", "--enable-api", "--cors", "*", "--host", "0.0.0.0", "--port", "5005"]