import mysql.connector
from mysql.connector import Error

def create_server_connection(hose_name, user_name, user_password):
    connection = None
    try:
        connection = mysql.connector.connect(
            host = hose_name,
            user = user_name,
            passwd = user_password
        )
        print("MYSQL Database connection successful")
    except Error as err:
        print(f"Error: '{err}'")
    return connection
def create_database(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("Database created successfully")
    except Error as err:
        print(f"Error as '{err}'")
connection = create_server_connection("localhost", "root", "student")
create_database_query = "CREATE DATABASE Hospital"
create_database(connection, create_database_query)