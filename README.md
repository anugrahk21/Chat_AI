# EasyAIBuddy - AI Telegram Bot

EasyAIBuddy is a Telegram bot that leverages the capabilities of Google's generative AI (Gemini-1.5-flash) to interact with users. It provides predefined responses to specific queries and can handle general questions using AI.

## Features

- Responds to specific predefined queries.
- Uses Google's generative AI model to provide responses to general questions.
- Simple and user-friendly interface.

## Prerequisites

- Python 3.6 or higher
- Telegram Bot API Key
- Google Generative AI API Key

## Installation

1. **Clone the repository**:
    ```sh
    git clone https://github.com/yourusername/EasyAIBuddy.git
    cd EasyAIBuddy
    ```

2. **Set up a virtual environment** (optional but recommended):
    ```sh
    python -m venv myenv
    source myenv/bin/activate  # On Windows: myenv\Scripts\activate
    ```

3. **Install the required packages**:
    ```sh
    pip install -r requirements.txt
    ```

    If `requirements.txt` is not available, you can manually install the required packages:
    ```sh
    pip install pyTelegramBotAPI google-generativeai
    ```

## Configuration

1. **Set up your environment variables**:
    - `GEMINI_API_AI_KEY`: Your Google Generative AI API key.
    - `BOT_API`: Your Telegram Bot API key.

    You can set these in your terminal session:

    ```sh
    export GEMINI_API_AI_KEY='your_google_ai_key'
    export BOT_API='your_telegram_bot_api_key'
    ```

    On Windows, use:

    ```sh
    set GEMINI_API_AI_KEY=your_google_ai_key
    set BOT_API=your_telegram_bot_api_key
    ```

2. **Create `key.py`**:
    Ensure you have a `key.py` file in the same directory with the following content:

    ```python
    GEMINI_API_AI_KEY = 'your_google_ai_key'
    BOT_API = 'your_telegram_bot_api_key'
    ```

## Running the Bot

Run the script:

```sh
python bot.py
```

This will start the Telegram bot. You should see Bot Started in your terminal, indicating that the bot is up and running.

# Bot Functionality

- **Start Command:**
When a user sends /start, the bot replies with:
```bash
Hello, Welcome to EasyAIBuddy
```

- **General Queries:**
The bot can respond to general queries using the generative AI model. If the query matches a predefined response, it will use that; otherwise, it will generate a response using the AI model.

# Code Explanation
## Imports and Configuration
```python
from key import *
import telebot
import google.generativeai as genai

genai.configure(api_key=GEMINI_API_AI_KEY)
```
## Generative Model Configuration
```python
generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config=generation_config,
)
```
## Chat Session Initialization
```python
chat_session = model.start_chat(history=[
    {
        "role": "user",
        "parts": ["what is your name"],
    },
    {
        "role": "model",
        "parts": [
            "I am your Easy AI Buddy. I am here to help you...\nFeel free to ask anything.",
        ],
    },
])

predefined_responses = {
    "what is your name": "I am your Easy AI Buddy. I am here to help you... Feel free to ask anything.",
}
```
## Bot Initialization and Handlers
```python
bot = telebot.TeleBot(BOT_API)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Hello, Welcome to EasyAIBuddy")

@bot.message_handler(func=lambda message: True)
def chatmessage(message):
    try:
        if message.text in predefined_responses:
            reply = predefined_responses[message.text]
        else:
            response = chat_session.send_message(message.text)
            reply = response.text
        bot.reply_to(message, reply)
    except Exception as e:
        print(e)
        bot.reply_to(message, f"Sorry, an error occurred. Please try again later.\nError: {str(e)}")

print("Bot Started")
bot.infinity_polling()
```
# Troubleshooting
- No module named 'telebot': Ensure that pyTelegramBotAPI is installed in your current environment.
- Environment Variables Not Set: Make sure to set GEMINI_API_AI_KEY and BOT_API correctly in your terminal.
# License
This project is licensed under the MIT License. See the [LICENSE file](LICENSE.md) for details.

# Contributing
Feel free to open issues or submit pull requests for any improvements or bug fixes.

# Acknowledgements
[PyTelegramBotAPI](https://github.com/eternnoir/pyTelegramBotAPI)

[Google Generative AI](https://ai.google/)


