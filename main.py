# Import
import telebot
import database
import keyboard_bot
import routing

# Bot Connect
token_bot = "1614577997:AAHECoJ6qH6DrKS-MNO1WSUc9HZ5RFr512c"
bot = telebot.TeleBot(token_bot)

user_data = {}

# database check connect
connection = database.create_connection(
    "merch_telegram_bot_db", "postgres", "Qsf98%x$", "127.0.0.1", "5432"
)
connection.close()


class User(object):
    def __init__(self, first_name, chat_id, last_name):
        if last_name is None:
            user_data['last_name'] = self.last_name = 'Отсутствует  🗿'
        else:
            user_data['last_name'] = self.last_name = last_name
        user_data['first_name'] = self.first_name = first_name
        user_data['address'] = self.address = 'Отсутствует  🗿'
        user_data['email'] = self.email = 'Отсутствует  🗿'
        user_data['phone'] = self.phone = 'Отсутствует  🗿'
        user_data['chat_id'] = self.chat_id = chat_id


class Product(object):
    pass


class Category(object):
    pass


@bot.message_handler(commands=['start'])
def send_welcome(message):
    main_menu = keyboard_bot.show_button_main_menu()
    user_object = User(message.from_user.first_name,
                       message.from_user.id,
                       message.from_user.last_name)
    bot.send_message(user_object.chat_id, user_object.first_name +
                     '\nЛамповое масло? Веревки? Бомбы?'
                     '\nТебе всё это нужно?'
                     '\nОно твоё, мой друг... если у тебя достаточно рупий 💎',
                     reply_markup=main_menu)


@bot.message_handler(content_types=['text'])
def handler_func(message):
    routing.routing_bot(message)


bot.polling()
