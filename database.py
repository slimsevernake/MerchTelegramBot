import psycopg2
from psycopg2 import OperationalError


# connection PostgreSQL
def create_connection(db_name, db_user, db_password, db_host, db_port):
    connection = None
    try:
        connection = psycopg2.connect(
            database=db_name,
            user=db_user,
            password=db_password,
            host=db_host,
            port=db_port,
        )
        print("Connection to PostgreSQL DB successful")
    except OperationalError as e:
        print(f"The error '{e}' occurred")
    return connection


connection = create_connection(
    "postgres", "postgres", "Qsf98%x$", "127.0.0.1", "5432"
)


# executing queries
def execution_of_requests(connection_db, query_sql):
    connection_db.autocommit = True
    cursor = connection_db.cursor()
    try:
        cursor.execute(query_sql)
        print("Query executed successfully")
    except psycopg2.errors.DuplicateTable:
        print("The table already exists! I continue to execute the program.")


try:
    sql = "CREATE DATABASE merch_telegram_bot_db"
    execution_of_requests(connection, sql)
    connection.close()
except psycopg2.errors.DuplicateDatabase:
    print("The database already exists! I continue to execute the program.")

query = ("CREATE TABLE customer ("
         "id SERIAL PRIMARY KEY,"
         "first_name VARCHAR(255),"
         "last_name VARCHAR(255),"
         "adds VARCHAR(255),"
         "email VARCHAR(255),"
         "phone VARCHAR(255),"
         "chat_id INT UNIQUE)",
         "CREATE TABLE category ("
         "id SERIAL PRIMARY KEY,"
         "category_name VARCHAR(255))",
         "CREATE TABLE product ("
         "id SERIAL PRIMARY KEY,"
         "category_id INT,"
         "name VARCHAR(255),"
         "description TEXT,"
         "price INT,"
         "FOREIGN KEY (category_id) REFERENCES category(id))",
         "CREATE TABLE product_photo ("
         "id SERIAL PRIMARY KEY,"
         "url VARCHAR(255),"
         "product_id INT,"
         "FOREIGN KEY (product_id) REFERENCES product(id))",
         "CREATE TABLE cart ("
         "id SERIAL PRIMARY KEY,"
         "customer_id INT,"
         "FOREIGN KEY(customer_id) REFERENCES customer(id))",
         "CREATE TABLE cart_product ("
         "cart_id INT,"
         "product_id INT,"
         "FOREIGN KEY(product_id) REFERENCES product(id),"
         "FOREIGN KEY(cart_id) REFERENCES cart(id))"
         )
for i in query:
    try:
        connection = create_connection(
            "merch_telegram_bot_db", "postgres", "Qsf98%x$", "127.0.0.1",
            "5432"
        )
        execution_of_requests(connection, i)
        connection.close()
    except OperationalError as e:
        print(f"The error '{e}' occurred")

print("Closing the program.")
