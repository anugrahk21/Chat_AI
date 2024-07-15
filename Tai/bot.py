from key import *
import telebot
import os

import google.generativeai as genai

genai.configure(api_key=OPEN_AI_KEY)

# Create the model
# See https://ai.google.dev/api/python/google/generativeai/GenerativeModel
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
  # safety_settings = Adjust safety settings
  # See https://ai.google.dev/gemini-api/docs/safety-settings
)

chat_session = model.start_chat(history=[
    {
      "role": "user",
      "parts": [
        "what is your name",
      ],
    },
    {
      "role": "model",
      "parts": [
        "I am your Easy AI Buddy. I am here to help you...\nFeel free to ask anything.",
      ],
    },
  ]
)
predefined_responses = {
    "what is your name": "I am your Easy AI Buddy. I am here to help you... Feel free to ask anything.",
    # Add more predefined Q&A pairs as needed
}
print(chat_session.history)


bot=telebot.TeleBot(BOT_API)
@bot.message_handler(['start'])
def start(message):
    bot.reply_to(message,"Hello, Welcome to EasyAIBuddy")

@bot.message_handler(func=lambda message:True)
def chatmessage(message):
    try:
        if message.text in predefined_responses:
          reply=predefined_responses[message.text]
        else:
          response = chat_session.send_message(message.text)
          print(response.text)
          reply=response.text
        print(message.text)
        bot.reply_to(message,reply)
    except Exception as e:
        print(e)
        bot.reply_to(message,"Sorry, an error occurred. Please try again later.\nError: "+e)

print("Bot Started")
bot.infinity_polling()