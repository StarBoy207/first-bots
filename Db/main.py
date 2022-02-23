from telebot import *

bot = telebot.TeleBot("5254901442:AAEgJCE9tgI5yhx4BhK92LoHhdaIs1pkByE")
@bot.message_handler(commands=["start"])
def reply_start(msg):
    user = msg.from_user.first_name
    link = msg.from_user.username
    
    bot.send_message(cid, "Hello")

bot.infinity_polling()
