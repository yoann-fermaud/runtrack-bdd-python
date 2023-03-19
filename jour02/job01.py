import mysql.connector

database = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="LaPlateforme"
)

cursor = database.cursor()
query = "SELECT * FROM etudiants"
cursor.execute(query)

print(cursor.fetchall())

cursor.close()
database.close()
