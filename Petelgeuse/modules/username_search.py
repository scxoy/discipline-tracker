def search_username(pseudo):
    sites = [
        "https://github.com/",
        "https://www.reddit.com/user/",
        "https://www.youtube.com/@",
        "https://x.com/",
        "https://www.tiktok.com/@",
    ]

    compteur = 0

    for site in sites:
        url = site + pseudo
        print(url)
        compteur += 1

    return compteur

def compter_sites():
    return 5