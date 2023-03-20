import mysql.connector

database = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="LaPlateforme"
)

cursor = database.cursor()
query = "SELECT SUM(capacite) FROM salles"
cursor.execute(query)

result = cursor.fetchone()
print(f"La capacité de toutes les salles est de {result[0]}.")

cursor.close()
database.close()
