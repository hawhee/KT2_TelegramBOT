import telebot
import pypwned

from config import TOKEN
from config import hibp_key


bot = telebot.TeleBot(token=TOKEN)


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id,"Введите почту для проверки")


@bot.message_handler(content_types=['text'])
def echo(message):
    email = message.text
    result = str(pypwned.pwned(hibp_key).getAllBreachesForAccount(str(email))))
    bot.send_message(message.chat.id, result)




bot.polling()
