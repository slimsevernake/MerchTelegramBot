# Import
import telebot
import database
import keyboard_bot
import routing
import re

# Bot Connect
token_bot = "1614577997:AAHECoJ6qH6DrKS-MNO1WSUc9HZ5RFr512c"
bot = telebot.TeleBot(token_bot)

# database check connect
connection = database.create_connection(
    "merch_telegram_bot_db", "postgres", "Qsf98%x$", "127.0.0.1", "5432"
)
connection.close()
user_dict = {}


class User(object):
    # Create user profile
    def __init__(self, first_name, last_name, address,
                 email, phone, username, chat_id):
        if username is None:
            self.username = None
        else:
            self.username = '@' + username
        self.last_name = last_name
        if address == "Отсутствует  🗿":
            self.address = None
        else:
            self.address = address
        self.email = email
        self.phone = phone
        self.first_name = first_name
        self.chat_id = chat_id


def send_welcome(message):
    register_menu = keyboard_bot.show_button_register()
    # main_menu = keyboard_bot.show_button_main_menu()
    bot.send_message(message.from_user.id, message.from_user.first_name +
                     '\nЛамповое масло? Веревки? Бомбы?'
                     '\nТебе всё это нужно?'
                     '\nОно твоё, мой друг... если у тебя достаточно рупий 💎')
    bot.send_message(message.from_user.id, '\nЧто бы использовать мои функции '
                                           'необходимо зарегистрироваться',
                     reply_markup=register_menu)


@bot.message_handler(content_types=['text'])
def register_function(message):
    message.text = message.text.replace(" ", "").lower()
    if re.findall(r'зарегистрироваться✏' or r'зарегистрироваться',
                  message.text):
        delete_keyboards = keyboard_bot.delete_keyboard()
        msg = bot.reply_to(message, 'Введите свою Фамилию, Имя.\n'
                                    'Формат: Фамилия Имя\n'
                                    'Например: Иванов Иван',
                           reply_markup=delete_keyboards)
        bot.register_next_step_handler(msg, process_name_step)


def process_name_step(message):
    try:
        pattern = r'[А-ЯЁа-яё]+'
        user_response = re.findall(pattern, message.text)
        if len(user_response) < 2:
            msg = bot.reply_to(message, 'Ошибка! Введите еще раз!\n'
                                        'Формат: Фамилия Имя\n'
                                        'Например: Иванов Иван')
            bot.register_next_step_handler(msg, process_name_step)
            return
        else:
            user_dict['last_name'] = user_response[0]
            user_dict['first_name'] = user_response[1]
            skip_button = keyboard_bot.skip()
            msg = bot.reply_to(message, 'Введите адрес доставки.\n'
                                        'Формат: улица, дом, город, почтовой '
                                        'индекс\n'
                                        'Например: Сеславинская ул., 22, '
                                        'Москва, 121309',
                               reply_markup=skip_button)
            bot.register_next_step_handler(msg, process_address_delivery_step)
    except Exception as e:
        bot.reply_to(message, 'Фатальная ошибка!')
        return


def process_address_delivery_step(message):
    try:
        user_response = message.text.replace(" ", "").lower()
        if re.findall(r'пропуститьшаг✏' or r'пропуститьшаг',
                      user_response):
            user_dict['address'] = "Отсутствует  🗿"
            delete_keyboards = keyboard_bot.delete_keyboard()
            msg = bot.reply_to(message, 'Введите адрес электронной '
                                        'почты.\n'
                                        'Например: example@test.com',
                               reply_markup=delete_keyboards)
            bot.register_next_step_handler(msg, process_email_step)
        else:
            pattern = r'(?:[А-ЯЁа-яё\d]+)'
            user_response = re.findall(pattern, message.text)
            if len(user_response) < 5:
                msg = bot.reply_to(message, 'Ошибка! Неправильный адрес \n'
                                            'Введите адрес еще раз!\n'
                                            'Например: Сеславинская ул., 22, '
                                            'Москва, 121309')
                bot.register_next_step_handler(msg,
                                               process_address_delivery_step)
            else:
                delete_keyboards = keyboard_bot.delete_keyboard()
                user_response = ' '.join(user_response)
                user_dict['address'] = user_response
                msg = bot.reply_to(message, 'Введите адрес электронной '
                                            'почты.\n'
                                            'Например: example@test.com',
                                   reply_markup=delete_keyboards)
                bot.register_next_step_handler(msg, process_email_step)
    except Exception as e:
        bot.reply_to(message, 'Фатальная ошибка!')
        return


def process_email_step(message):
    try:
        pattern = r'[A-Za-z0-9\.]+[@][A-Za-z0-9]+[.][A-Za-z]{2,3}'
        user_response = re.findall(pattern, message.text)
        if len(user_response) < 1:
            msg = bot.reply_to(message, 'Ошибка! Несуществующая почта!\n'
                                        'Введите электронную почту еще раз!\n'
                                        'Например: example@test.com')
            bot.register_next_step_handler(msg, process_email_step)
            return
        else:
            user_dict['email'] = user_response[0]
            msg = bot.reply_to(message, 'Введите номер телефона\n'
                                        'Например: 89998887766')
            bot.register_next_step_handler(msg, process_phone_step)
    except Exception as e:
        bot.reply_to(message, 'Фатальная ошибка!')
        return


def process_phone_step(message):
    try:
        pattern = r'([0-9]{11})'
        user_response = re.findall(pattern, message.text)
        if len(user_response) < 1:
            msg = bot.reply_to(message, 'Ошибка! Введите '
                                        'номер телефона еще раз!\n'
                                        'Например: 89998887766')
            bot.register_next_step_handler(msg, process_phone_step)
            return
        else:
            main_menu = keyboard_bot.show_button_main_menu()
            user_dict['phone'] = user_response[0]
            bot.send_message(message.from_user.id, 'Спасибо за регистрацию!',
                             reply_markup=main_menu)
            bot.send_message(message.from_user.id, 'Ваш профиль:\nФамилия: '
                             + user_dict['last_name'] +
                             '\nИмя: '
                             + user_dict['first_name'] +
                             '\nАдрес: '
                             + user_dict['address'] +
                             '\nЭлектронная почта: '
                             + user_dict['email'] +
                             '\nТелефон: '
                             + user_dict['phone'],
                             reply_markup=main_menu)
            user_object = User(user_dict['first_name'], user_dict['last_name'],
                               user_dict['address'], user_dict['email'],
                               user_dict['phone'], message.from_user.username,
                               message.from_user.id)
            database.ProfileInteraction.insert_record(user_object)
    except Exception as e:
        bot.reply_to(message, 'Фатальная ошибка!')
        return


# Enable saving next step handlers to file "./.handlers-saves/step.save".
# Delay=2 means that after any change in next step handlers (e.g. calling
# register_next_step_handler()) saving will hapen after delay 2 seconds.
bot.enable_save_next_step_handlers(delay=2)

# Load next_step_handlers from save file (default
# "./.handlers-saves/step.save") WARNING It will work only if
# enable_save_next_step_handlers was called!
bot.load_next_step_handlers()
