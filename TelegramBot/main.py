import telebot
import requests
import json
from telebot import types

bot = telebot.TeleBot("5961141106:AAGHlKi1KPQunvk969jg9OI_QLC12mVEXTM")

token = "z4WwKiGeSex5W31dzqeC3omSNYpR4NBn"

@bot.message_handler(commands=["start"])
def start(message):
    markup = types.ReplyKeyboardMarkup()
    button1 = types.KeyboardButton("Курс доллара")
    button2 = types.KeyboardButton("Курс евро")
    button3 = types.KeyboardButton("Курс тенге")
    markup.add(button1, button2, button3)

    mess = f"Добрый день, {message.from_user.first_name}, хотите узнать курс ключевых валют???"
    bot.send_message(message.chat.id, mess, reply_markup=markup)

@bot.message_handler(content_types=["text"])
def message_responder(message):
    if (message.text == "Курс доллара"):
        request(message, "USD", "доллара")
    elif (message.text == "Курс евро"):
        request(message, "EUR", "евро")
    elif (message.text == "Курс тенге"):
        request(message, "KZT", "тенге")

def request(message, currency, name):
    data = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').json()
    value = data["Valute"][currency]["Value"]
    mess = f"Курс {name} к рублю {value}"
    bot.send_message(message.chat.id, mess)

bot.polling(none_stop=True)