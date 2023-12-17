from os import getenv

import telebot
from dotenv import load_dotenv

import inf

load_dotenv()
token = getenv('BOT_TOKEN')

bot = telebot.TeleBot(token)

description_txt = f'{inf.o['name']}\n\n{inf.o["description"]['age']}\n\n{inf.o["description"]['profession']}\n\n{inf.o["description"]['characteristic']}\n\n{inf.o["description"]['hobby']['literature']}\n{inf.o["description"]['hobby']['music']}\n{inf.o['description']['hobby']['sport']}\n{inf.o["description"]['hobby']['social']}\n\n{inf.o["description"]['fashion']}'


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
    global description_txt
    bot.send_photo(chat_id=message.chat.id, photo=inf.o['img'], caption=description_txt)


@bot.message_handler(commands=['photo'])
def photo(message):
    bot.send_photo(chat_id=message.chat.id, photo=inf.o['img'])


@bot.message_handler(commands=['description'])
def description(message):
    global description_txt
    bot.send_message(chat_id=message.chat.id, text=description_txt)


bot.polling()
