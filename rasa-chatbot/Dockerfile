# Use the official Rasa image as a base
FROM rasa/rasa:3.6.16

# Set the working directory
WORKDIR /app

# Copy project files
COPY . /app

# Train the model during build
RUN rasa train

# Expose the port Rasa runs on
EXPOSE 5005

# Default command to run Rasa server
