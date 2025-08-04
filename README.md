# Rasa Chatbot Project

This is a Rasa-based chatbot project that can handle various conversations including greetings, questions, information requests, and more.

## Project Structure

```
rasa-chatbot/
├── actions/
│   └── actions.py
├── data/
│   ├── nlu.yml
│   ├── rules.yml
│   └── stories.yml
├── config.yml
├── credentials.yml
├── domain.yml
├── endpoints.yml
└── models/
```

## Setup and Installation

1. Make sure you have Docker installed on your system
2. Build the Docker image:
   ```bash
   cd rasa-chatbot
   docker build -t rasa-bot .
   ```

## Running the Bot

### 1. Start the Rasa Server

```bash
cd rasa-chatbot
docker run -p 5005:5005 -v $(pwd):/app rasa-bot run --enable-api
```

This starts the main Rasa server on port 5005.

### 2. Start the Action Server (if using custom actions)

In a new terminal:
```bash
cd rasa-chatbot
docker run -p 5055:5055 -v $(pwd):/app rasa-bot run actions
```

### 3. Interacting with the Bot

#### Option 1: Using Web Interface
The easiest way to interact with the bot is through the web interface:

1. Start a simple HTTP server to serve the web interface:
```bash
cd rasa-chatbot/web
python3 -m http.server 8000
```

2. Open your browser and navigate to:
```
http://localhost:8000
```

The web interface provides a user-friendly chat interface where you can interact with the bot directly.

#### Option 2: Using Rasa Shell
```bash
docker run -it -v $(pwd):/app rasa-bot shell
```

#### Option 3: Using REST API
Send POST requests to `http://localhost:5005/webhooks/rest/webhook`:
```bash
curl -X POST http://localhost:5005/webhooks/rest/webhook \
     -H "Content-Type: application/json" \
     -d '{"sender": "user", "message": "Hello"}'
```

## Conversation Capabilities

The bot can handle the following types of interactions:

### Supported Intents

1. Basic Interactions:
   - `greet`: Hello, hi, hey, good morning
   - `goodbye`: Bye, goodbye, see you later
   - `bot_challenge`: Are you a bot?

2. Questions and Information:
   - `ask_question`: Ask general questions
   - `ask_information`: Request specific information
   - `ask_help`: Request for help
   - `ask_name`: Ask for the bot's name

3. User Information:
   - `provide_name`: User provides their name

4. Mood Expressions:
   - `mood_great`: Express positive feelings
   - `mood_unhappy`: Express negative feelings

### Example Conversations

1. Basic Greeting:
   ```
   User: Hello
   Bot: Hello! How can I assist you today?
   ```

2. Name Exchange:
   ```
   User: What's your name?
   Bot: I am a bot, powered by Rasa.
   
   User: My name is John
   Bot: Thank you for sharing that!
   ```

3. Help Request:
   ```
   User: I need help
   Bot: How can I help you today?
   
   User: I have a question
   Bot: What topic would you like to know more about?
   ```

## Training the Bot

To retrain the bot with updated data:

```bash
cd rasa-chatbot
docker run -v $(pwd):/app rasa-bot train
```

This will create a new model in the `models/` directory.

## File Descriptions

- `domain.yml`: Defines the bot's universe - intents, entities, slots, responses
- `config.yml`: Configuration for NLU and Core models
- `data/nlu.yml`: Training data for understanding user messages
- `data/stories.yml`: Conversation paths for training
- `data/rules.yml`: Definitive conversation rules
- `actions/actions.py`: Custom action code
- `endpoints.yml`: Service endpoint configurations
- `credentials.yml`: API keys and credentials for various channels

## Development and Customization

1. To add new intents:
   - Add examples to `data/nlu.yml`
   - Add the intent to `domain.yml`
   - Create stories in `data/stories.yml`
   - Add responses in `domain.yml`

2. To modify responses:
   - Edit the responses section in `domain.yml`

3. To add custom actions:
   - Create new action classes in `actions/actions.py`
   - Add them to the actions list in `domain.yml`
   - Update stories to use these actions