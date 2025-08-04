# Use the official Rasa image as a base
FROM rasa/rasa:3.6.16

# Set the working directory
WORKDIR /app

# Copy project files
COPY . /app

# (Optional) Install extra requirements for custom actions
# RUN pip install -r actions/requirements.txt

# Expose the port Rasa runs on
EXPOSE 5005

# Default command to run Rasa server
CMD ["run", "--enable-api", "--cors", "*", "--debug"]
