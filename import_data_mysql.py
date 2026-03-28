import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Kiranamuruga@23",
    database="ecommerce_db"
)

cursor = conn.cursor()
cursor.execute("SELECT DATABASE(), @@hostname, @@port;")

print(cursor.fetchall())

conn.close()