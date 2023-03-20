import mysql.connector

database = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="LaPlateforme"
)

cursor = database.cursor()
query = "SELECT SUM(superficie) FROM etage"
cursor.execute(query)

result = cursor.fetchone()
print(f"La superficie de La Plateforme est de {result[0]} m².")

cursor.close()
database.close()
