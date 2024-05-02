import sqlite3

conn = sqlite3.connect('zipbank.sqlite')

cursor = conn.cursor()

cursor.execute("SELECT * FROM transactions")
print(cursor.fetchall())

# Commit the changes and close the connection
conn.commit()
conn.close()