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