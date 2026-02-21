import random

print("=== Calculateur de ridque ===")

risk_amount = float(input("Monrtant du risque par trade : "))
entry_price = float(input("prix d'entrée : "))
stop_price = float(input("prix du stop : "))
take_profit = float(input("prix take profit : "))
distance_stop = abs(entry_price - stop_price)
if distance_stop == 0:
    print("distance stop invalide.")
else:
    quantity = risk_amount / distance_stop
    reward_distance = abs(entry_price - take_profit)
    profit = reward_distance * quantity
    r_ratio = profit / risk_amount
    percent_gain = (profit / risk_amount) * 100
    print(f"\nGain potentiel en % du capital : {percent_gain:.2f}%")
    print(f"Montant risqué : {risk_amount}")
    print(f"Distance risque : {distance_stop}")
    print(f"Quantitré à prendre : {quantity}")
    print(f"Distance reward : {reward_distance}")
    print(f"Profit ptentiel : {profit}")
    print(f"Ratio de gain : {r_ratio:.2f}")

    if r_ratio < 1: 
        print("mauvais trade (R < 1)")
    elif r_ratio < 2:
        print("trade acceptable (1 ≤ R < 2)")
    else:     print("trés bon trade (R ≥ 2)")

capital_initial = 1000
risk_percent = 1
winrate = 50
r_multiple = 2 
nombre_de_trades = 20
risk_profit = risk_percent / 100 * capital_initial       # montant du ridsque en argent
win_fraction = winrate / 100
expantcy = win_fraction * r_multiple - (1 - win_fraction) * 1
print(f"\nExpectancy théorique par trade : {expantcy:.4f} R")
wins = 0
losses = 0
for _ in range(nombre_de_trades):
    risk_amount = capital_initial * (risk_percent / 100)
    if random.random() < win_fraction:
        capital_initial += risk_amount * r_multiple
        wins += 1
    else:
        capital_initial -= risk_amount
        losses += 1
        print(f"\nResuilatats après {nombre_de_trades} trades :")
        print(f"Capital final : {capital_initial:.2f}")
        print(f"Nombre de trades gagants : {wins}")
        print(f"Nombre de trade perdants : {losses}")
