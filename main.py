from telebot import TeleBot

Bot = TeleBot('8170357654:AAF2wVAqW2bzKRhOlp-meu3bTiP4B8YAByg')


@Bot.message_handler(commands=['start'])
def start(message):
    Bot.send_message(message.chat.id, 'hello')


Bot.infinity_polling()