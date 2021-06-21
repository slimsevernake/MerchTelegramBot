import psycopg2
import query
from psycopg2 import OperationalError


# sql queries
class ProfileInteraction(classmethod):
    def insert_record(self):
        connection = create_connection(
            "merch_telegram_bot_db", "postgres", "password_db", "127.0.0.1",
            "5432"
        )
        data = (
            self.first_name, self.last_name, self.address,
            self.email, self.phone, self.username, self.chat_id
        )
        execution_of_requests(connection,
                              query.query_register['insert_register_data'],
                              data)
        user_profile = execution_of_requests(connection,
                                             query.query_register[
                                                 'select_register_data'] +
                                             str(self.chat_id))
        user_id = user_profile[0][0]
        insert_id_cart = f"insert into cart (customer_id) values " \
                         f"({str(user_id)})"
        execution_of_requests(connection, insert_id_cart)
        connection.close()

    def update_record(self):
        connection = create_connection(
            "merch_telegram_bot_db", "postgres", "password_db", "127.0.0.1",
            "5432"
        )
        data = (
            self.first_name, self.last_name, self.address,
            self.email, self.phone, self.username, self.chat_id
        )
        execution_of_requests(connection,
                              query_register['update_profile_data'],
                              data)
        connection.close()

    def select_record(self):
        connection = create_connection(
            "merch_telegram_bot_db", "postgres", "password_db", "127.0.0.1",
            "5432"
        )
        data = self.chat_id
        execution_of_requests(connection,
                              query.query_register['select_profile_data'],
                              data)
        connection.close()

    def verification_user(self):
        connection = create_connection(
            "merch_telegram_bot_db", "postgres", "password_db", "127.0.0.1",
            "5432"
        )
        data = self.from_user.id
        query_verification = dict(verification=(
            f"select * from customer where chat_id = '{data}'"
        ))
        result = execution_of_requests(connection,
                                       query_verification['verification'],
                                       data)
        connection.close()
        if not result:
            return False
        else:
            return True


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
    except OperationalError as e:
        print(f"The error '{e}' occurred")
    return connection


connection = create_connection(
    "postgres", "postgres", "password_db", "127.0.0.1", "5432"
)


def create_database(connection):
    try:
        sql = "CREATE DATABASE merch_telegram_bot_db"
        execution_of_requests(connection, sql)
        connection.close()
    except psycopg2.errors.DuplicateDatabase:
        pass
    for key in query.create_database:
        try:
            connection = create_connection(
                "merch_telegram_bot_db", "postgres", "password_db", "127.0.0.1",
                "5432"
            )
            execution_of_requests(connection, query.create_database[key])
            connection.close()
        except OperationalError as e:
            print(f"The error '{e}' occurred")


# executing queries
def execution_of_requests(connection_db, query_sql, data=None):
    connection_db.autocommit = True
    cursor = connection_db.cursor()
    try:
        cursor.execute(query_sql, data)
        result = cursor.fetchall()
        return result
    except Exception:
        pass


if execution_of_requests(connection, query.check_database['check']):
    print("The database already exists")
else:
    create_database(connection)
