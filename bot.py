from os import getenv

import telebot
from dotenv import load_dotenv

import inf

load_dotenv()
token = getenv('BOT_TOKEN')

bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(chat_id=message.chat.id, text="Привет! Это бот-визитка Антониана Кодвина.\n"
                                                   "Чтобы узнать о том как использовать этого бота откройте меню или "
                                                   "введите команду /help.")


@bot.message_handler(commands=['help'])
def send_help(message):
    bot.send_message(chat_id=message.chat.id, text="/all_info - Все информация\n"
                                                   "/photo - Фото\n"
                                                   "/description - Описание\n")


@bot.message_handler(commands=['all_info'])
def all_info(message):
    bot.send_photo(chat_id=message.chat.id, photo=inf.o['img'], caption=f'{inf.o['name']}\n{inf.o["description"]}')


@bot.message_handler(commands=['photo'])
def photo(message):
    bot.send_photo(chat_id=message.chat.id, photo=inf.o['img'])


@bot.message_handler(commands=['description'])
def description(message):
    bot.send_message(chat_id=message.chat.id, text=inf.o['description'])


bot.polling()
