import sqlite3

conn = sqlite3.connect("database.db")

cursor = conn.cursor()

cursor.execute("""
INSERT INTO utilisateurs (pseudo)
VALUES ("scxoy")
""")

cursor.execute("""
SELECT * FROM utilisateurs
""")

resultat = cursor.fetchall()

for utilisateur in resultat:
    print("ID :", utilisateur[0])
    print("Pseudo :", utilisateur[1])
    print("-----")

conn.commit()

conn.close()