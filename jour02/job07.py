import mysql.connector

database = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="LaPlateforme"
)

cursor = database.cursor()

# Create database
# cursor.execute("DROP DATABASE entreprise")
cursor.execute("CREATE DATABASE IF NOT EXISTS entreprise")
cursor.execute("USE entreprise")

# Add table
# cursor.execute("DROP TABLES employes")
cursor.execute("CREATE TABLE IF NOT EXISTS employes "
               "(id INT PRIMARY KEY AUTO_INCREMENT, "
               "nom VARCHAR(255), "
               "prenom VARCHAR(255), "
               "salaire DECIMAL, "
               "id_service INT, "
               "UNIQUE (nom, prenom, id_service))")

employes = [
    ("Doe", "John", 2500.00, 1),
    ("Dupuis", "Martin", 3000.00, 2),
    ("Durand", "Alice", 2000.00, 3)
]

for employe in employes:
    try:
        cursor.execute("INSERT INTO employes (nom, prenom, salaire, id_service) VALUES (%s, %s, %s, %s)", employe)
    except mysql.connector.IntegrityError:
        print(f"L'employé {employe[0]} {employe[1]} est déjà présent dans la base de données.")


cursor.execute("SELECT * FROM employes WHERE 3000 <= salaire")
results = cursor.fetchone()


print(f"Les employés ayant un salaire supérieur à 3000 sont : {results[1]} {results[2]}")


database.commit()
cursor.close()
database.close()
