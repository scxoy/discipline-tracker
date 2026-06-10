import requests

sites = [
    ["Github", "https://github.com/"],
    ["YouTube", "https://www.youtube.com/user/"],
    ["Reddit", "https://www.reddit.com/user/"],
    ["TikTok", "https://www.tiktok.com/@"],
    ["Instagram", "https://www.instagram.com/"],
    ["X", "https://x.com/"],
    ["facebook", "https://www.facebook.com/"],
    ["Twitch", "https://www.twitch.tv/"],
    ["Spotify", "https://open.spotify.com/user/"],
    ["Discord", "https://discord.com/users/"],
    ["Steam", "https://steamcommunity.com/id/"],
    ["Pinterest", "https://www.pinterest.com/"],
    ["LinkedIn", "https://www.linkedin.com/in/"],
    ["Snapchat", "https://www.snapchat.com/add/"],
]

def search_username(pseudo):
    compteur = 0
    trouves = 0
    refuses = 0
    non_trouves = 0
    inconnus = 0
    erreurs = 0

    for site in sites:
        nom_site = site[0]
        url_base = site[1]
        url = url_base + pseudo
        print(url)
        
        try:
            response = requests.get(url, timeout=5)
            status = interpret_status(response.status_code)
        except:
            status = "Erreur"
        print(status)
        
        status = interpret_status(response.status_code)
        print(nom_site, ":", status)
        if status == "Trouvé":
            trouves += 1
        elif status == "Refusé":
            refuses += 1
        elif status == "Non trouvé":
            non_trouves += 1
        elif status == "Erreur":
            erreurs += 1
        else:
            inconnus += 1

        compteur += 1

    print("\n=== Résultats ===")
    print("Trouvé:", trouves)
    print("Refusé:", refuses)
    print("Non trouvé:", non_trouves)
    print("Inconnu:", inconnus)
    print("Erreurs:", erreurs)
    print("\nSites vérifiés:", compteur)
    
    return compteur

def compter_sites():
    return len(sites)

def interpret_status(code):
    if code == 200:
        return "Trouvé"
    elif code == 403:
        return "Refusé"
    elif code == 404:
        return "Non trouvé"
    else:
        return "Inconnu"
    