from statistics import mode
print("=== Risk Calculator ===")

capital = float(input("Capital total : "))
risk_percent = float(input("Risque en % par trade : ").replace("%", "").strip())
entry_price = float(input("Prix d'entrée : "))
stop_price = float(input("Prix du stop : "))
take_profit = float(input("Prix take profit : "))
if mode == "2":
    print("\n=== Simulation ===")
    capital = float(input("Capital initial : "))
    risk_percent = float(input("Risque en % par trade : ").replace("%", "").strip())
    n_trades = int(input("Nombre de trades : "))
    winrate = float(input("Winrate en % : ").strip().replace("%", ""))
    r_multiple = float(input("R multiple moyen (ex: 2) : "))
    
    risk_fraction = risk_percent / 100
    win_fraction = winrate / 100
    expectancy = win_fraction * r_multiple - (1 - win_fraction)
    print(f"Expectancy théorique par trade : {expectancy:.4f} R")
    
    for i in range(1, n_trades + 1):
        risk_amount = capital * risk_fraction
        # gain = +R*risk_amount si win, sinon -1*risk_amount
        # on fait simple: on gagne si i dans la partie "wins" selon winrate
        # (plus tard on fera alèatoire)
        if i <= int(n_trades * win_fraction):
            gain += risk_amount * r_multiple
        else:
            gain -= risk_amount
    print(f"\nCapital final : {capital:.2f}")
risk_amount = capital * (risk_percent / 100)
distance = abs(entry_price - stop_price)

if distance == 0:
    print("Distance invalide.")
else:
    quantity = risk_amount / distance
    reward_distance = abs(take_profit - entry_price)
    profit = reward_distance * quantity
    r_ratio = profit / risk_amount
    percent_gain = (profit / capital) * 100

    print(f"Gain ptentiel en % du capital : {percent_gain:.2f}%")
    print(f"Montant risqué : {risk_amount}")
    print(f"Distance risque : {distance}")
    print(f"Quantité à prendre : {quantity}")
    print(f"Distance reward : {reward_distance}")
    print(f"Profit potentiel : {profit}")
    print(f"R ratio : {r_ratio:.2f}")

    if r_ratio < 1:
        print("Mauvais trade (R < 1)")
    elif r_ratio < 2:
        print("Trade acceptable (1 ≤ R < 2)")
    else:
        print("Très bon trade (R ≥ 2)")

