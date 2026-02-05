import csv
from datetime import date
from safe_utils import Safety 
safe = Safety(timeout_seconds=30, max_steps=1000)
FILE_NAME = "discipline_log.csv"
# Crée le fichier + en-tête UNE seul fois si le fichier n'existe pas
try:    
    with open(FILE_NAME, "x", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["date", "heure", "niveau"])
except FileExistsError:
    pass
while True:
    safe.step()
    user_input = input("combien d'heure tu travaille par jour ? (q pour quitter) : ")
    if user_input.lower() == "q":
        print("fin du programme. Continue comme ça !")
        break
    if not user_input.isdigit():
        print("Entre un nombre valide.")
        continue
    #   après tes print du niveau (élite / bon / débutant)
    heure = int(user_input)
    if heure >= 8:
        print("Niveau élite.")
    elif heure >= 6:
        niveau = "bon"
        print("bon niveau.")
    else:
        niveau = "débutant"
        print("Débutant, progresse.")

    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date.today().isoformat(), heure, niveau])


    
