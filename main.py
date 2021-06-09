# Import Bot Module
import keyboard_bot as keyboard
import database
import routing
import interface
# Import Python Module
import re
import threading
from time import sleep
# Import Other Module
import telebot

BOT_TOKEN = "1614577997:AAHECoJ6qH6DrKS-MNO1WSUc9HZ5RFr512c"
BOT_INTERVAL = 1
BOT_TIMEOUT = 30
bot = None

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


class Register:
    def process_name_step(self):
        try:
            pattern = r'[А-ЯЁа-яё]+'
            user_response = re.findall(pattern, self.text)
            if len(user_response) < 2:
                msg = bot.reply_to(self, 'Ошибка! Введите еще раз!\n'
                                         'Формат: Фамилия Имя\n'
                                         'Например: Иванов Иван')
                bot.register_next_step_handler(msg, Register.process_name_step)
                return
            else:
                user_dict['last_name'] = user_response[0]
                user_dict['first_name'] = user_response[1]
                skip_button = keyboard.skip()
                msg = bot.reply_to(self, 'Введите адрес доставки.\n'
                                         'Формат: улица, дом, город, '
                                         'почтовой '
                                         'индекс\n'
                                         'Например: Сеславинская ул., 22, '
                                         'Москва, 121309',
                                   reply_markup=skip_button)
                bot.register_next_step_handler(msg,
                                               Register.process_address_step)
        except Exception as e:
            print('Фатальная ошибка!' + f'\n{str(e)}')
            return

    def process_address_step(self):
        try:
            user_response = self.text.replace(" ", "").lower()
            if re.findall(r'пропуститьшаг✏' or r'пропуститьшаг',
                          user_response):
                user_dict['address'] = "Отсутствует  🗿"
                delete_keyboards = keyboard.delete_keyboard()
                msg = bot.reply_to(self, 'Введите адрес электронной '
                                         'почты.\n'
                                         'Например: example@test.com',
                                   reply_markup=delete_keyboards)
                bot.register_next_step_handler(msg, Register.
                                               process_email_step)
            else:
                pattern = r'(?:[А-ЯЁа-яё\d]+)'
                user_response = re.findall(pattern, self.text)
                if len(user_response) < 5:
                    msg = bot.reply_to(self, 'Ошибка! Неправильный адрес \n'
                                             'Введите адрес еще раз!\n'
                                             'Например: Сеславинская ул., '
                                             '22, '
                                             'Москва, 121309')
                    bot.register_next_step_handler(msg,
                                                   Register.
                                                   process_address_step)
                else:
                    delete_keyboards = keyboard.delete_keyboard()
                    user_response = ' '.join(user_response)
                    user_dict['address'] = user_response
                    msg = bot.reply_to(self, 'Введите адрес электронной '
                                             'почты.\n'
                                             'Например: example@test.com',
                                       reply_markup=delete_keyboards)
                    bot.register_next_step_handler(msg, Register.
                                                   process_email_step)
        except Exception as e:
            print('Фатальная ошибка!' + f'\n{str(e)}')
            return

    def process_email_step(self):
        try:
            pattern = r'[A-Za-z0-9\.]+[@][A-Za-z0-9]+[.][A-Za-z]{2,3}'
            user_response = re.findall(pattern, self.text)
            if len(user_response) < 1:
                msg = bot.reply_to(self, 'Ошибка! Несуществующая почта!\n'
                                         'Введите электронную почту еще '
                                         'раз!\n '
                                         'Например: example@test.com')
                bot.register_next_step_handler(msg, Register.
                                               process_email_step)
                return
            else:
                user_dict['email'] = user_response[0]
                msg = bot.reply_to(self, 'Введите номер телефона\n'
                                         'Например: 89998887766')
                bot.register_next_step_handler(msg, Register.
                                               process_phone_step)
        except Exception as e:
            print('Фатальная ошибка!' + f'\n{str(e)}')
            return

    def process_phone_step(self):
        try:
            pattern = r'([0-9]{11})'
            user_response = re.findall(pattern, self.text)
            if len(user_response) < 1:
                msg = bot.reply_to(self, 'Ошибка! Введите '
                                         'номер телефона еще раз!\n'
                                         'Например: 89998887766')
                bot.register_next_step_handler(msg, Register.
                                               process_phone_step)
                return
            else:
                main_menu = keyboard.show_button_main_menu()
                user_dict['phone'] = user_response[0]
                bot.send_message(self.from_user.id,
                                 'Спасибо за регистрацию!',
                                 reply_markup=main_menu)
                bot.send_message(self.from_user.id,
                                 'Ваш профиль:\nФамилия: '
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
                user_object = User(user_dict['first_name'],
                                   user_dict['last_name'],
                                   user_dict['address'],
                                   user_dict['email'],
                                   user_dict['phone'],
                                   self.from_user.username,
                                   self.from_user.id)
                database.ProfileInteraction.insert_record(user_object)
        except Exception as e:
            print('Фатальная ошибка!' + f'\n{str(e)}')
            return


def bot_polling():
    global bot
    print("Starting bot polling now")
    while True:
        try:
            print("New bot instance started")
            bot = telebot.TeleBot(BOT_TOKEN)  # Generate new bot instance
            bot_actions()  # If bot is used as a global variable, remove bot
            # as an input param
            bot.polling(none_stop=True, interval=BOT_INTERVAL,
                        timeout=BOT_TIMEOUT)
        except Exception as ex:  # Error in polling
            print("Bot polling failed, restarting in {}sec. Error:\n{}".format(
                BOT_TIMEOUT, ex))
            bot.stop_polling()
            sleep(BOT_TIMEOUT)
        else:  # Clean exit
            bot.stop_polling()
            print("Bot polling loop finished")
            break  # End loop


def bot_actions():
    @bot.message_handler(commands=['start'])
    def test_function(message):
        if database.ProfileInteraction.verification_user(message) is False:
            register_menu = keyboard.show_button_register()
            # main_menu = keyboard.show_button_main_menu()
            bot.send_message(message.from_user.id,
                             message.from_user.first_name +
                             '\nЛамповое масло? Веревки? Бомбы?'
                             '\nТебе всё это нужно?'
                             '\nОно твоё, мой друг... если у тебя достаточно '
                             'рупий 💎')
            bot.send_message(message.from_user.id,
                             '\nЧто бы использовать мои функции '
                             'необходимо зарегистрироваться',
                             reply_markup=register_menu)
        else:
            main_menu = keyboard.show_button_main_menu()
            bot.send_message(message.from_user.id,
                             message.from_user.first_name +
                             '\nЛамповое масло? Веревки? Бомбы?'
                             '\nТебе всё это нужно?'
                             '\nОно твоё, мой друг... если у тебя достаточно '
                             'рупий 💎',
                             reply_markup=main_menu)

    @bot.message_handler(content_types=['text'])
    def redirecting_bot(message):
        message.text = message.text.replace(" ", "").lower()
        if re.findall(r'зарегистрироваться✏' or r'зарегистрироваться',
                      message.text):
            delete_keyboards = keyboard.delete_keyboard()
            msg = bot.reply_to(message, 'Введите свою Фамилию, Имя.\n'
                                        'Формат: Фамилия Имя\n'
                                        'Например: Иванов Иван',
                               reply_markup=delete_keyboards)
            bot.register_next_step_handler(msg, Register.process_name_step)
        elif database.ProfileInteraction.verification_user(message) is True:
            routing.routing_bot(message)
        else:
            register_menu = keyboard.show_button_register()
            bot.reply_to(message, 'Нажмите кнопку "Зарегистрироваться ✏"',
                         reply_markup=register_menu)

    @bot.callback_query_handler(func=lambda call: True)
    def callback_response(call):
        try:
            if call.message:
                interface.InterfaceInteraction.callback_data_handler(call)
        except Exception as e:
            print('Фатальная ошибка!' + f'\n{str(e)}')
            return


polling_thread = threading.Thread(target=bot_polling)
polling_thread.daemon = True
polling_thread.start()

# Keep main program running while bot runs threaded
if __name__ == "__main__":
    while True:
        try:
            sleep(120)
        except KeyboardInterrupt:
            break
