# Import
import telebot as tel
import database
import keyboard_bot as keyboard
import routing
import re

# Bot Connect
token_bot = "1614577997:AAHECoJ6qH6DrKS-MNO1WSUc9HZ5RFr512c"
bot = tel.TeleBot(token_bot)

# database check connect
connection = database.create_connection(
    "merch_telegram_bot_db", "postgres", "Qsf98%x$", "127.0.0.1", "5432"
)
connection.close()


@bot.message_handler(commands=['start'])
def verification_user(message):
    if len(database.ProfileInteraction.verification_user(message)) == 0:
        import register
        register.send_welcome(message)
    else:
        send_welcome(message)


def send_welcome(message):
    main_menu = keyboard.show_button_main_menu()
    bot.send_message(message.from_user.id, message.from_user.first_name +
                     '\nЛамповое масло? Веревки? Бомбы?'
                     '\nТебе всё это нужно?'
                     '\nОно твоё, мой друг... если у тебя достаточно рупий 💎',
                     reply_markup=main_menu)


@bot.message_handler(content_types=['text'])
def handler_func(message):
    routing.routing_bot(message)


bot.polling()
