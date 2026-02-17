print("=== Risk Calculator ===")

capital = float(input("Capital total : "))
risk_percent = float(input("Risque en % par trade : "))
entry_price = float(input("Prix d'entrée : "))
stop_price = float(input("Prix du stop : "))
take_profit = float(input("Prix take profit : "))

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

