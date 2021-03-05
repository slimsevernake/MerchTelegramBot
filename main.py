import telebot

token = "1614577997:AAHECoJ6qH6DrKS-MNO1WSUc9HZ5RFr512c"
bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message,
                     "Lamp oil? Rope? Bombs? You want it? It's your's, my friend, as long as you have enough rupees.")


bot.polling()

#Установка git через linux консоль.
# sudo apt-get install git
# вводим root пароль, если ты не root пользователь
# инициализируем git в нашем проекте. Команда git init
# выполняем настройки git (Имя пользователя). git config --global user.name "username"
# выполняем настройки git (E-mail). git config --global user.email "email"
# после данных настроек, все изменения в проекте будут привязываться к имени и почте пользователя.
# git status (Статус нашего проекта).
# git add --all (добавление всех файлов в отслеживание)
# git add конкретный файл (добавление файла в отслеживание)

