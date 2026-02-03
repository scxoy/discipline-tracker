heure = int(input("combien d'heure tu travaille par jour : "))

if heure >= 6:
    print("très bien. Discipline élevée.")
else:
    print("tu peux faire mieux. Augmente ton effort.")
if heure >= 8:
    print("Niveau élite.")
elif heure >= 6:
    print("bon niveau.")
else:
    print("Débutant, progresse.")


