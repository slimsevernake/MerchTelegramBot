# Import
import telebot
import database
import keyboard_bot
import re

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
            user_data['last_name'] = last_name = 'Отсутствует  🗿'
        user_data['first_name'] = self.first_name = first_name
        user_data['last_name'] = self.last_name = last_name
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
    bot.send_message(user_object.chat_id, 'Hi! ' + user_object.first_name +
                     '\nLamp oil? Rope? Bombs? You want it? It\'s your\'s, '
                     'my friend, as long as you have enough rupees.',
                     reply_markup=main_menu)
    bot.send_message(user_object.chat_id,
                     'На данный момент твой профиль выглядит так: '
                     '\nИмя: ' + user_object.first_name +
                     '\nФамилия: ' + user_object.last_name +
                     '\nАдрес: ' + user_object.address +
                     '\nE-mail: ' + user_object.email +
                     '\nТелефон: ' + user_object.phone +
                     '\nДля того что бы отредактировать имеющиеся данные '
                     'перейдите в настройки')


@bot.message_handler(content_types=['text'])
def routing_bot(message):
    message.text = message.text.replace(" ", "")
    if re.findall(r'Купить💣', message.text):
        bot.send_message(message.chat.id, "Выбран пункт меню: 'Купить 💣'")
    elif re.findall(r'Корзина🧺', message.text):
        bot.send_message(message.chat.id, "Выбран пункт меню: 'Корзина 🧺'")
    elif re.findall(r'Заказы📦', message.text):
        main_menu = keyboard_bot.show_button_orders()
        bot.send_message(message.chat.id, "Выбран пункт меню: 'Заказы 📦'",
                         reply_markup=main_menu)
    elif re.findall(r'Новости📜', message.text):
        main_menu = keyboard_bot.show_button_news()
        bot.send_message(message.chat.id, "Выбран пункт меню: 'Новости 📜'",
                         reply_markup=main_menu)
    elif re.findall(r'Настройки⚙', message.text):
        main_menu = keyboard_bot.show_button_settings()
        bot.send_message(message.chat.id, "Выбран пункт меню: 'Настройки ⚙'",
                         reply_markup=main_menu)
    elif re.findall(r'Помощь🆘', message.text):
        main_menu = keyboard_bot.show_button_help()
        bot.send_message(message.chat.id, "Выбран пункт меню: 'Помощь 🆘'",
                         reply_markup=main_menu)
    elif re.findall(r'Начало🏠', message.text):
        main_menu = keyboard_bot.show_button_main_menu()
        bot.send_message(message.chat.id, "Выбран пункт меню: 'Начало🏠'",
                         reply_markup=main_menu)
    elif re.findall(r'Позвонить📞', message.text):
        main_menu = keyboard_bot.show_button_help()
        bot.send_message(message.chat.id, "Выбран пункт меню: 'Позвонить 📞'",
                         reply_markup=main_menu)
    elif re.findall(r'Написать✉', message.text):
        main_menu = keyboard_bot.show_button_help()
        bot.send_message(message.chat.id, "Выбран пункт меню: 'Написать ✉'",
                         reply_markup=main_menu)
    elif re.findall(r'Помощьнасайте📘', message.text):
        main_menu = keyboard_bot.show_button_help()
        bot.send_message(message.chat.id,
                         "Выбран пункт меню: 'Помощь на сайте 📘'",
                         reply_markup=main_menu)
    elif re.findall(r'Назад⬅', message.text):
        main_menu = keyboard_bot.show_button_main_menu()
        bot.send_message(message.chat.id, "Выбран пункт меню: 'Назад ⬅'",
                         reply_markup=main_menu)
    elif re.findall(r'Имя', message.text):
        main_menu = keyboard_bot.show_button_settings()
        bot.send_message(message.chat.id, "Выбран пункт меню: 'Имя'",
                         reply_markup=main_menu)
    elif re.findall(r'Телефон', message.text):
        main_menu = keyboard_bot.show_button_settings()
        bot.send_message(message.chat.id, "Выбран пункт меню: 'Телефон'",
                         reply_markup=main_menu)
    elif re.findall(r'Адрес', message.text):
        main_menu = keyboard_bot.show_button_settings()
        bot.send_message(message.chat.id, "Выбран пункт меню: 'Адрес'",
                         reply_markup=main_menu)
    elif re.findall(r'Город', message.text):
        main_menu = keyboard_bot.show_button_settings()
        bot.send_message(message.chat.id, "Выбран пункт меню: 'Город'",
                         reply_markup=main_menu)
    elif re.findall(r'Уведомления🔔', message.text):
        main_menu = keyboard_bot.show_button_settings()
        bot.send_message(message.chat.id,
                         "Выбран пункт меню: 'Уведомления 🔔'",
                         reply_markup=main_menu)
    else:
        main_menu = keyboard_bot.show_button_main_menu()
        bot.send_message(message.chat.id, "Я не понимаю о чем идет речь!",
                         reply_markup=main_menu)


bot.polling()
