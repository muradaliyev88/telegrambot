from telebot.async_telebot import AsyncTeleBot
from telebot import types

bot = AsyncTeleBot('7015168639:AAGFa3YiwP2Gu10BjQjcgWFSiyyosUF0-WM')



class bot_api:

    @bot.message_handler(commands=['start'])
    async def start(message):
        markup = types.ReplyKeyboardMarkup()
        btn_en_to_az = types.KeyboardButton("en>>az")
        btn_az_to_en = types.KeyboardButton("az>>en")
        markup.row(btn_en_to_az)
        markup.row(btn_az_to_en)
        await bot.send_message(message.chat.id,"Salam başlamaq üçün birini seçin!", reply_markup=markup)
        await bot.register_next_step_handler(message,onclick)

    def onclick(message):
        if message.text == "en>>az":
            bot.send_message(message.chat.id, "English to Azerbaijani")
        elif message.text == "az>>en":
            bot.send_message(message.chat.id, "Azerbaijani to  English")




"""  

def buttons():
    markup = types.InlineKeyboardMarkup()
    btn_en_to_az = types.InlineKeyboardButton("en>>az")
    btn_az_to_en = types.InlineKeyboardButton("az>>en")
    markup.row(btn_en_to_az,btn_az_to_en)
    return markup


@bot.message_handler(commands=['help', 'start'])
async def send_welcome(message):
    markup = types.InlineKeyboardMarkup()
    btn_en_to_az = types.InlineKeyboardButton("en>>az")
    btn_az_to_en = types.InlineKeyboardButton("az>>en")
    markup.row(btn_en_to_az,btn_az_to_en)
    if message.text == "/start":
        await bot.reply_to(message,"Dili seçin", reply_markup=markup)
    else:
        await bot.reply_to(message,"can I help you?" )



# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bot.message_handler(func=lambda message: True)
async def echo_message(message):
    await bot.reply_to(message, message.text)

"""
import asyncio
asyncio.run(bot.polling())
