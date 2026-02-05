import csv
print("Stats du discipline tracker")
with open("discipline_log.csv", "r", newline="") as file:
    reader = csv.reader(file)
    next(reader) # Skip header
    heure_total = 0
    for row in reader:
        date = row[0]
        heure = int(row[1])  # convertir en entier 
        niveau = row[2] 
        print(date, heure, niveau)
        print("-" * 20)
        heure_total += heure
    print(f"Heure totales travaillées : {heure_total}")


        
        
        
        