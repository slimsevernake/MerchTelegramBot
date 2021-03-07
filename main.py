# Import
import telebot
import mysql.connector
from mysql.connector import Error

# Bot Connect
token_bot = "1614577997:AAHECoJ6qH6DrKS-MNO1WSUc9HZ5RFr512c"
bot = telebot.TeleBot(token_bot)


# MySQL Connect
def create_connection(host_name, user_name, user_password):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password
        )
        print("Connection to MySQL DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")

    return connection


connection = create_connection("localhost", "root", "Qsf98%x$")


user_data = {}


class User(object):
    def __init__(self, first_name, last_name, chat_id, phone="false"):
        user_data['First_name'] = self.first_name = first_name
        user_data['Last_name'] = self.last_name = last_name
        user_data['Phone'] = self.phone = phone
        user_data['Chat_id'] = self.chat_id = chat_id
        print(user_data)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    user_object = User(message.from_user.first_name,
                       message.from_user.last_name,
                       message.from_user.id,
                       getattr(message, 'form_user.phone', 'false'))
    bot.send_message(user_data['Chat_id'],
                     'Lamp oil? Rope? Bombs? You want it? It\'s your\'s, '
                     'my friend, as long as you have enough rupees.')


bot.polling()
