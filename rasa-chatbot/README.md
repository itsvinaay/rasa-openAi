# rasa-chatbot

This project is a Rasa-based chatbot designed to handle various conversational tasks. Below is an overview of the project's structure and files:

## Project Structure

```
rasa-chatbot
├── data
│   ├── nlu.yml          # Training data for the NLU component
│   ├── rules.yml        # Rules for conversation flow
│   └── stories.yml      # Example conversations for dialogue management
├── models               # Directory for storing trained models
├── actions
│   └── actions.py       # Custom action implementations
├── config.yml           # Configuration settings for the Rasa project
├── credentials.yml      # Credentials for messaging platforms
├── domain.yml           # Domain definition including intents, entities, and responses
├── endpoints.yml        # Configuration for server endpoints
└── README.md            # Project documentation
```

## Setup Instructions

1. **Install Rasa**: Make sure you have Rasa installed. You can install it using pip:
   ```
   pip install rasa
   ```

2. **Project Initialization**: Initialize the Rasa project structure by running:
   ```
   rasa init
   ```

3. **Training the Model**: Train the model using the training data provided in the `data` directory:
   ```
   rasa train
   ```

4. **Running the Action Server**: If you have custom actions, run the action server:
   ```
   rasa run actions
   ```

5. **Starting the Rasa Server**: Start the Rasa server to interact with the chatbot:
   ```
   rasa run
   ```

## Usage

- You can interact with the chatbot through the command line or integrate it with messaging platforms by configuring the `credentials.yml` file.
- Modify the `data/nlu.yml`, `data/rules.yml`, and `data/stories.yml` files to customize the chatbot's behavior and responses.

## Running the Bot

### For Local Development

### 1. Start the Rasa Server

```bash
rasa run --enable-api --cors "*" --debug
```

### 2. Start the Action Server (in a separate terminal)

```bash
rasa run actions
```

Or using Docker:
```bash
docker run -p 5055:5055 -v $(pwd):/app rasa-bot run actions
```

### For Production Deployment (Coolify)

See `coolify-deploy.md` for detailed deployment instructions.

Quick deployment using Docker Compose:
```bash
# Use the production compose file
docker-compose -f docker-compose.coolify.yml up -d
```

### 3. Interacting with the Bot

## Contributing

Feel free to contribute to this project by submitting issues or pull requests. Make sure to follow the project's coding standards and guidelines.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.