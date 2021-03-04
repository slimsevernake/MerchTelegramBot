import telebot

bot = telebot.TeleBot("1614577997:AAHECoJ6qH6DrKS-MNO1WSUc9HZ5RFr512c")


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Howdy, how are you doing?")


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)


bot.polling()
