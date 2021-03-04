import telebot

token = "1614577997:AAHECoJ6qH6DrKS-MNO1WSUc9HZ5RFr512c"
bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message,
                     "Lamp oil? Rope? Bombs? You want it? It's your's, my friend, as long as you have enough rupees.")


bot.polling()
