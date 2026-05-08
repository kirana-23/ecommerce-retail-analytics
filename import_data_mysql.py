import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password_here",
    database="ecommerce_db"
)

cursor = conn.cursor()
cursor.execute("SELECT DATABASE(), @@hostname, @@port;")

print(cursor.fetchall())

conn.close()
