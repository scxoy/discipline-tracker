from modules.username_search import search_username

pseudo = input("Entre un pseudo : ")

print("\n=== PETELGEUSE ===\n")

resultat = search_username(pseudo)

print("nResultats :", resultat)