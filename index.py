import telebot, db, os, requests, BS
from telebot import types

bot = telebot.TeleBot(db.token['token'])


bot.infinity_polling()