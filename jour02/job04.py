import mysql.connector

database = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="LaPlateforme"
)

cursor = database.cursor()
query = "SELECT nom, capacite FROM salles"
cursor.execute(query)

# print(cursor.fetchall())
for nom, capacite in cursor:
    print("Salle: {}, Capacité: {}".format(nom, capacite))

cursor.close()
database.close()
