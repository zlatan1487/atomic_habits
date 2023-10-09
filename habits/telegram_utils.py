import telebot
import os

TELEGRAM_BOT = os.getenv('TELEGRAM_BOT_URL')
bot = telebot.TeleBot(TELEGRAM_BOT)


def send_message_to_user(chat_id, message):
    bot.send_message(chat_id, message)
