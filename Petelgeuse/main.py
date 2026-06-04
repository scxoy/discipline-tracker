pseudo = input("Entre un pseudo : ")

site = [
    "https://github.com/",
    "https://www.reddit.com/user/",
    "https://www.youtube.com/@"
]

print("\n=== PETELGUEUSE ===")

for site in site:
    url = site + pseudo
    print(url)