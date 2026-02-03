from safe_utils import Safety 
safe = Safety(timeout_seconds=30, max_steps=1000)
while True:
    safe.step()
    user_input = input("combien d'heure tu travaille par jour ? (q pour quitter) : ")
    if user_input.lower() == "q":
        print("fin du programme. Continue comme ça !")
        break
    if not user_input.isdigit():
        print("Entre un nombre valide.")
        continue
    heure = int(user_input)
    if heure >= 8:
        print("Niveau élite.")
    elif heure >= 6:
        print("bon niveau.")
    else:
        print("Débutant, progresse.")

    print("-" * 30)

        
