import telebot
import keyboard_bot
import re


# Bot Connect
token_bot = "1614577997:AAHECoJ6qH6DrKS-MNO1WSUc9HZ5RFr512c"
bot = telebot.TeleBot(token_bot)


# Routing
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