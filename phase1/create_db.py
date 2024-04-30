import mysql
from mysql import connector
import name_password

try:
    connection = mysql.connector.connect(
        host='localhost',
        database= 'zipbank',
        user= name_password.username,
        passwd= name_password.password
    )
    my_cursor = connection.cursor()

    mySql_Create_Table_Query = """ CREATE TABLE customers (
                            id INT PRIMARY KEY,
                            name VARCHAR(255),
                            balance DECIMAL(10,2) NOT NULL
                            )
                        
                            CREATE TABLE ledger(
                            id INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
                            transaction_date INT, 
                            amount DECIMAL (10,2) NOT NULL,
                            transaction_type ENUM('deposit', 'withdrawal')
                            )"""
    result = my_cursor.execute(mySql_Create_Table_Query)
    print("tables created successfully")
except mysql.connector.Error as error:
    print("failed to create table in MySql: {}".format(error))
finally:
    if connection.is_connected():
        my_cursor.close()
        connection.close()
        print("mySQL connection is closed")