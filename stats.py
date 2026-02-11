import csv
print("Stats du discipline tracker")
with open("discipline_log.csv", "r", newline="") as file:
    reader = csv.reader(file)
    next(reader) # Skip header
    heure_total = 0
    session_count = 0
    for row in reader:
        date = row[0]
        heure = int(row[1])  # convertir en entier 
        niveau = row[2] 
        heure_total += heure
        session_count += 1
    if session_count > 0:
        moyenne = heure_total / session_count
    else: 
        moyenne = 0
        print(date, heure, niveau)
        print("-" * 20)
        heure_total += heure
    print(f"Heure totales travaillées : {heure_total}")
    print(f"Nombre : {session_count}")
    print(f"Total heure : {heure_total}")
    print(f"Moyenne : {moyenne:.2f}")

        
        
        
        