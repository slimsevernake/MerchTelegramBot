import telebot

token = "1614577997:AAHECoJ6qH6DrKS-MNO1WSUc9HZ5RFr512c"
bot = telebot.TeleBot(token)



class User:
    def __init__(self):
        self.chat_id = message.from_user.id

@bot.message_handler(commands=['start'])
def send_welcome(message):
    chat_id = message.from_user.id
    bot.send_message(chat_id,
                     'Lamp oil? Rope? Bombs? You want it? It\'s your\'s, '
                     'my friend, as long as you have enough rupees.')
    User()


bot.polling()

