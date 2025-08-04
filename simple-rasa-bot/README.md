# Simple Rasa Chatbot

This is a simple Rasa chatbot that can handle basic conversations including greetings, mood expressions, and goodbyes.

## Setup

1. Make sure you have Rasa installed:
   ```bash
   pip install rasa
   ```

2. Train the model:
   ```bash
   rasa train
   ```

3. Test the bot:
   ```bash
   rasa shell
   ```

## What the bot can do

- Greet users (hello, hi, good morning)
- Respond to mood expressions (happy/sad)
- Say goodbye
- Answer if it's a bot

## Example conversations

```
User: Hello
Bot: Hey! How are you?

User: I'm feeling great
Bot: Great, carry on!

User: I'm sad
Bot: Here is something to cheer you up: [image]
Bot: Did that help you?

User: Are you a bot?
Bot: I am a bot, powered by Rasa.
```

## Running the bot

To interact with the bot in the terminal:
```bash
rasa shell
```

To run as a server:
```bash
rasa run --enable-api --cors "*"
```