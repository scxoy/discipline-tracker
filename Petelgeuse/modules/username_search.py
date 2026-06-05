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

    for site in sites:
        nom_site = site[0]
        url_base = site[1]
        url = url_base + pseudo
        print(url)
        response = requests.get(url, timeout=5)
        status = interpret_status(response.status_code)
        print(status)
        compteur += 1

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