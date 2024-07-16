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
    - `OPEN_AI_KEY`: Your Google Generative AI API key.
    - `BOT_API`: Your Telegram Bot API key.

    You can set these in your terminal session:

    ```sh
    export OPEN_AI_KEY='your_open_ai_key'
    export BOT_API='your_bot_api_key'
    ```

    On Windows, use:

    ```sh
    set OPEN_AI_KEY=your_open_ai_key
    set BOT_API=your_bot_api_key
    ```

## Running the Bot

Run the script:

```sh
python bot.py
