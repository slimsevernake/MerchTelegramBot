import psycopg2
import query
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


for key in query.default_query:
    try:
        connection = create_connection(
            "merch_telegram_bot_db", "postgres", "Qsf98%x$", "127.0.0.1",
            "5432"
        )
        execution_of_requests(connection, query.default_query[key])
        connection.close()
    except OperationalError as e:
        print(f"The error '{e}' occurred")


# sql queries
def creating_record(user_object):
    pass


print("Closing the program.")
