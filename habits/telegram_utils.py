import telebot
import os

API_KEY = os.getenv('HABBITS_RATE_API_KEY')
TELEGRAM_BOT = os.getenv('HABBITS_EXCHANGE_RATE_BOT')
bot = telebot.TeleBot(TELEGRAM_BOT)


def send_notification(chat_id, message):
    bot.send_message(chat_id, message)



