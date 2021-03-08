# Import
import telebot
import mysql.connector
from mysql.connector import Error

# Bot Connect
token_bot = "1614577997:AAHECoJ6qH6DrKS-MNO1WSUc9HZ5RFr512c"
bot = telebot.TeleBot(token_bot)

user_data = {}


# MySQL Connect
def create_connection(host_name, user_name,
                      user_password, database_name=""):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=database_name
        )
        print("Connection to MySQL DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")

    return connection


connect_database = create_connection("localhost", "root", "Qsf98%x$")


# Create DataBase
def create_database(connection):
    cursor = connection.cursor()
    try:
        create_database_query = "CREATE DATABASE merch_telegram_bot_db"
        cursor.execute(create_database_query)
        query_table = "CREATE TABLE customer (" \
                      "id INT AUTO_INCREMENT PRIMARY KEY," \
                      "first_name VARCHAR(255)," \
                      "last_name VARCHAR(255)," \
                      "email VARCHAR(255)," \
                      "phone VARCHAR(255)," \
                      "chat_id INT UNIQUE)"
        connect_db = create_connection("localhost",
                                       "root",
                                       "Qsf98%x$",
                                       "merch_telegram_bot_db")
        cursor = connect_db.cursor()
        cursor.execute(query_table)
        query_table = "CREATE TABLE product (" \
                      "id INT AUTO_INCREMENT PRIMARY KEY," \
                      "name VARCHAR(255)," \
                      "description TEXT," \
                      "price INT)"
        cursor.execute(query_table)
        query_table = "CREATE TABLE product_photo (" \
                      "id INT AUTO_INCREMENT PRIMARY KEY," \
                      "url VARCHAR(255)," \
                      "product_id INT REFERENCES product(id))"
        cursor.execute(query_table)
        query_table = "CREATE TABLE cart (" \
                      "id INT AUTO_INCREMENT PRIMARY KEY," \
                      "customer_id INT REFERENCES customer(id))"
        cursor.execute(query_table)
        query_table = "CREATE TABLE cart_product (" \
                      "cart_id INT REFERENCES cart(id)," \
                      "product_id INT REFERENCES product(id))"
        cursor.execute(query_table)
        print("Database created successfully")
        return connect_db
    except Error as e:
        connect_db = create_connection("localhost",
                                       "root",
                                       "Qsf98%x$",
                                       "merch_telegram_bot_db")
        print(f"The error '{e}' occurred")
        return connect_db


connect_database = create_database(connect_database)


# Insert DataBase
def insert_database(connection, query, value):
    cursor = connection.cursor()
    try:
        cursor.execute(query, value)
        connection.commit()
        print("Insert completed")
    except Error as e:
        print(f"The error '{e}' occurred")


class User(object):
    def __init__(self, first_name, last_name, chat_id, phone="false"):
        user_data['First_name'] = self.first_name = first_name
        user_data['Last_name'] = self.last_name = last_name
        user_data['Phone'] = self.phone = phone
        user_data['Chat_id'] = self.chat_id = chat_id


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
