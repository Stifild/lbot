from os import getenv

import telebot
from dotenv import load_dotenv
from telebot.types import Message

load_dotenv()
token = getenv('BOT_TOKEN')

bot = telebot.TeleBot(token)


def hi(message: Message):
    return 'привет' in message.text.lower()


def bay(message: Message):
    return 'пока' in message.text.lower()


@bot.message_handler(func=hi)
def send_hi(message: Message):
    bot.send_message(chat_id=message.chat.id, text=f'Привет! {message.from_user.first_name}')


@bot.message_handler(func=bay)
def send_bay(message: Message):
    bot.send_message(chat_id=message.chat.id, text=f'Пока! {message.from_user.first_name}')


@bot.message_handler(commands=['start'])
def send_hello_message(message: Message):
    bot.send_message(chat_id=message.chat.id, text=f'Здравствуй {message.from_user.first_name}\nЧтобы узнать что я '
                                                   f'могу напиши команду /help')


@bot.message_handler(commands=['help'])
def send_help_list(message: Message):
    bot.send_message(chat_id=message.chat.id,
                     text=f'{message.from_user.first_name} ты можешь прислать мне любое сообщение и я повторю его. '
                          f'Если напишешь привет или пока я отвечу тем же.')


@bot.message_handler(content_types=['text'])
def send_echo(message: Message):
    bot.send_message(chat_id=message.chat.id, text=f'Вы отправили <{message.text}>')


bot.polling()
