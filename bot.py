# DEVELOPER : Pouria Hosseini
# Telegram id : @isPoori 
# Telegram CHANNEL : @OmgaDeveloper 

import telebot
from telebot import types
bot = telebot.TeleBot("TOKEN")


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "DEVELOPER : @isPoori\nCHANNEL : @OmgaDeveloper")

@bot.message_handler(commands=['get'])
def sendmessage(message):
    user_id = message.from_user.id
    first_name = message.from_user.first_name
    bot.reply_to(message, f'Your id : {user_id}\nyour name : {first_name}\nyour username : @{message.from_user.username}')


bot.infinity_polling()
