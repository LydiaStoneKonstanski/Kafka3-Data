import mysql.connect
import name_password

mydb = mysql.connector.connect(
    host='localhost',
    user= name_password.username,
    passwd= name_password.password,
)

my_cursor = mydb.cursor()

my_cursor.execute("CREATE DATABASE zipbank")
my_cursor.execute("SHOW DATABASES")
for db in my_cursor:
    print(db)