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

    print(f"Montant risqué : {risk_amount}")
    print(f"Distance : {distance}")
    print(f"Quantité à prendre : {quantity}")
    print(f"Distance reward : {reward_distance}")
    print(f"Profit potentiel : {profit}")
    print(f"R ratio : {r_ratio}")
    