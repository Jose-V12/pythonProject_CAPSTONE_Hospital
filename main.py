import mysql.connector
from mysql.connector import Error

def create_server_connection(hose_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host = hose_name,
            user = user_name,
            passwd = user_password,
            database = db_name
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
def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query successful")
    except Error as err:
        print(f"Error '{err}'")

#TABLES:
create_employee_table = """
CREATE TABLE employee (
employee_id INT PRIMARY KEY,
dob DATE,
first_name VARCHAR(40) NOT NULL,
last_name VARCHAR(40) NOT NULL,
gender VARCHAR(7) NOT NULL,
education VARCHAR(40) NOT NULL,
years_experience VARCHAR(20),
hire_date Date
);
"""

connection = create_server_connection("localhost", "root", "student", "hospital")
execute_query(connection, create_employee_table)