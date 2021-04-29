# Import
import telebot
from telebot import types

# Bot Connect
token_bot = "1614577997:AAHECoJ6qH6DrKS-MNO1WSUc9HZ5RFr512c"
bot = telebot.TeleBot(token_bot)

user_data = {}


class User(object):
    def __init__(self, first_name, last_name, chat_id, phone="false"):
        user_data['First_name'] = self.first_name = first_name
        user_data['Last_name'] = self.last_name = last_name
        user_data['Phone'] = self.phone = phone
        user_data['Chat_id'] = self.chat_id = chat_id


class Product(object):
    pass


class Category(object):
    pass


# Buttons
def show_button():
    markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard="true")
    item_buy = types.KeyboardButton(text="Купить 💣")
    item_basket = types.KeyboardButton(text="Корзина 🧺")
    item_orders = types.KeyboardButton(text="Заказы 📦")
    item_news = types.KeyboardButton(text="Новости 📜")
    item_settings = types.KeyboardButton(text="Настройки ⚙")
    item_help = types.KeyboardButton(text="Помощь 🆘")
    markup.add(item_buy, item_basket, item_orders,
               item_news, item_settings, item_help)
    return markup


def show_inline_button_main_menu():
    markup = types.InlineKeyboardMarkup(row_width=1)
    item_bombs = types.InlineKeyboardButton(text="Бомбы 💣",
                                            callback_data="bombs")
    item_lamp_oil = types.InlineKeyboardButton(text="Ламповое масло 💣",
                                               callback_data="lamp_oil")
    item_rope = types.InlineKeyboardButton(text="Веревки 💣",
                                           callback_data="rope")
    markup.add(item_bombs, item_lamp_oil, item_rope)
    return markup


@bot.message_handler(commands=['start'])
def send_welcome(message):
    main_menu = show_button()
    user_object = User(message.from_user.first_name,
                       message.from_user.last_name,
                       message.from_user.id,
                       getattr(message, 'form_user.phone', 'false'))
    bot.send_message(user_data['Chat_id'],
                     'Lamp oil? Rope? Bombs? You want it? It\'s your\'s, '
                     'my friend, as long as you have enough rupees.',
                     reply_markup=main_menu)


bot.polling()
