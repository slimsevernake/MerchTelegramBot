import telebot

token = "1614577997:AAHECoJ6qH6DrKS-MNO1WSUc9HZ5RFr512c"
bot = telebot.TeleBot(token)


user_data = {}


class User(object):
    def __init__(self, first_name, last_name, chat_id, phone="false"):
        user_data['First_name'] = self.first_name = first_name
        user_data['Last_name'] = self.last_name = last_name
        user_data['Phone'] = self.phone = phone
        user_data['Chat_id'] = self.chat_id = chat_id


@bot.message_handler(commands=['start'])
def send_welcome(message):
    first_name = message.from_user.first_name
    last_name = message.from_user.last_name
    chat_id = message.from_user.id
    phone = getattr(message, 'form_user.phone', 'false')
    user_object = User(first_name, last_name, chat_id, phone)
    bot.send_message(chat_id,
                     'Lamp oil? Rope? Bombs? You want it? It\'s your\'s, '
                     'my friend, as long as you have enough rupees.')


bot.polling()
