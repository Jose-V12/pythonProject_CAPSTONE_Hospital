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
create_salary_table = """
CREATE TABLE salary (
employee_id INT PRIMARY KEY,
first_name VARCHAR(40) NOT NULL,
last_name VARCHAR(40) NOT NULL,
salary VARCHAR(10),
hire_date Date
);
 """
create_department_table = """
CREATE TABLE department (
employee_id INT PRIMARY KEY,
surgery VARCHAR(40) NOT NULL,
burn_unit VARCHAR(40) NOT NULL,
urgent_care VARCHAR(40) NOT NULL
);
"""

#INFO Inside our Tables:
table_employee= """
INSERT INTO employee VALUES
(1, '1995-02-12', 'James', 'Smith', 'Male','Bachelors Degree', '3 yrs', '2019-03-20'),
(2, '1994-03-29', 'Larissa', 'Johnson', 'Female','Masters Degree', '4 yrs', '2018-07-20'),
(3, '1996-08-10', 'Joe', 'Will', 'Male','Bachelors Degree', '2 yrs', '2020-05-10'),
(4, '1995-06-03', 'riley', 'WinterHouse', 'Female','Bachelors Degree', '3 yrs', '2019-08-25'),
(5, '1998-08-09', 'James', 'Brown', 'Male','Masters Degree', '1 yrs', '2022-12-10'),
(6, '1993-05-04', 'Adam', 'West', 'Male','Masters Degree', '5 yrs', '2017-01-05'),
(7, '1999-08-24', 'Maritza', 'Jones', 'Female','Bachelors Degree', '2 yrs', '2020-05-22'),
(8, '2000-04-20', 'Cassandra', 'Lopez', 'Female','Bachelors Degree', '1 yrs', '2022-01-27'),
(9, '1998-07-16', 'John', 'Williams', 'Male','Bachelors Degree', '3 yrs', '2019-09-04'),
(10, '1993-09-25 ', 'Richard', 'Mitch', 'Male','Masters Degree', '7 yrs', '2015-03-29');
"""
table_salary= """
INSERT INTO salary VALUES
(1, 'James', 'Smith', '$80,000', '2019-03-20'),
(2, 'Larissa', 'Johnson', '$100,000', '2018-07-20'),
(3, 'Joe', 'Will','$75,000', '2020-05-10'),
(4, 'riley', 'WinterHouse', '$80,000', '2019-08-25'),
(5, 'James', 'Brown', '$80,000', '2022-12-10'),
(6, 'Adam', 'West', '$170,000', '2017-01-05'),
(7, 'Maritza', 'Jones', '$75,000', '2020-05-22'),
(8, 'Cassandra', 'Lopez', '$70,000', '2022-01-27'),
(9, 'John', 'Williams', '$80,000', '2019-09-04'),
(10, 'Richard', 'Mitch', '$210,000', '2015-03-29');
"""
table_department= """
INSERT INTO department VALUES
(1, 'James Smith', '', ''),
(2, 'Larissa Johnson', '', ''),
(3, 'Joe Will', '', ''),
(4, '', 'riley WinterHouse', ''),
(5, '', '', 'James Brown'),
(6, '', 'Adam West', ''),
(7, '', 'Maritza Jones', ''),
(8, '', '', 'Cassandra Lopez'),
(9, '', 'John Williams', ''),
(10, '', '', 'Richard Mitch');
"""

#Updating our Tables:
update= """
UPDATE salary
SET salary="$225,000"
WHERE last_name ="Will"
"""

connection = create_server_connection("localhost", "root", "student", "hospital")
execute_query(connection, update)