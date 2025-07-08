# 🤖✨ Chat_AI: Your Creative Telegram AI Buddy! ✨🤖

Welcome to **Chat_AI**, your all-in-one, AI-powered Telegram assistant built with Python and Gemini!  
Ask, chat, create, and explore the power of generative AI—right in your Telegram inbox. 🚀

---

## 📜 Table of Contents
- [🌟 Features](#-features)
- [⚙️ Prerequisites](#-prerequisites)
- [📦 Installation](#-installation)
- [🔑 Configuration](#-configuration)
- [▶️ Running the Bot](#-running-the-bot)
- [🤔 How It Works](#-how-it-works)
- [🧑‍💻 Code Overview](#-code-overview)
- [🐞 Troubleshooting](#-troubleshooting)
- [🪪 License](#-license)
- [🤝 Contributing](#-contributing)
- [🙏 Acknowledgements](#-acknowledgements)
- [🔗 Connect & Collaborate](#-connect--collaborate)

---

## 🌟 Features

- 🗣️ Chat with AI using natural language
- 📚 Predefined smart replies for common queries
- ⚡ Built on Google's Gemini generative AI
- 🤖 Runs directly in Telegram
- 🪄 Simple, user-friendly, and fun!

---

## ⚙️ Prerequisites

- 🐍 Python 3.6+
- 🤖 Telegram Bot API Key
- 🔑 Google Generative AI API Key

---

## 📦 Installation

```sh
git clone https://github.com/anugrahk21/Chat_AI.git
cd Chat_AI
python -m venv myenv
source myenv/bin/activate  # On Windows: myenv\Scripts\activate
pip install -r requirements.txt
```

If `requirements.txt` is missing:
```sh
pip install pyTelegramBotAPI google-generativeai
```

---

## 🔑 Configuration

- Set environment variables for your API keys:
    - `GEMINI_API_AI_KEY`
    - `BOT_API`
- (Optional) Create a `key.py` with your keys as variables

---

## ▶️ Running the Bot

```sh
python bot.py
```
Look for `Bot Started` in your terminal.

---

## 🤔 How It Works

- `/start`: Greets you with a welcome message
- General queries: AI responds using Gemini, or predefined answers if available

---

## 🧑‍💻 Code Overview

- Imports and setup
- Model configuration & chat session
- Telegram bot handlers for commands and messages
- Error handling and infinite polling

---

## 🐞 Troubleshooting

- `No module named 'telebot'`: Install pyTelegramBotAPI
- API Key errors: Double-check your keys and environment variables

---

## 🪪 License

Licensed under the MIT License. See [LICENSE file](LICENSE.md).

---

## 🤝 Contributing

Pull requests and issues are welcome!

---

## 🙏 Acknowledgements

- [PyTelegramBotAPI](https://github.com/eternnoir/pyTelegramBotAPI)
- [Google Generative AI](https://ai.google/)

---

## 🔗 Connect & Collaborate

**Let's build a more secure digital world together!** 🌍

### **Professional Links:**
- 🐙 **GitHub**: [anugrahk21](https://github.com/anugrahk21)
- 💼 **LinkedIn**: [Anugrah K](https://linkedin.com/in/anugrah-k)
- 📧 **Email**: [anugrah.k910@gmail.com](mailto:anugrah.k910@gmail.com)

---

If you want the full markdown file or want the content tailored/shortened for specific sections, let me know!
