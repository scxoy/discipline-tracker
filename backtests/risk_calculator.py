import random

print("=== Risk Calculator ===")


# =======================
# MODE NORMAL
# =======================
def run_normal():
    capital = float(input("Capital total : "))
    risk_percent = float(input("Risque en % par trade : ").replace("%", "").strip())
    entry_price = float(input("Prix d'entrée : "))
    stop_price = float(input("Prix du stop : "))
    take_profit = float(input("Prix take profit : "))

    risk_amount = capital * (risk_percent / 100)
    distance_stop = abs(entry_price - stop_price)

    if distance_stop == 0:
        print("Distance stop invalide.")
        return

    quantity = risk_amount / distance_stop
    reward_distance = abs(entry_price - take_profit)
    profit = reward_distance * quantity
    r_ratio = profit / risk_amount
    percent_gain = (profit / capital) * 100

    print(f"\nGain potentiel en % du capital : {percent_gain:.2f}%")
    print(f"Montant risqué : {risk_amount}")
    print(f"Distance risque : {distance_stop}")
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


# =======================
# MODE SIMULATION
# =======================
def run_simulation():
    capital = float(input("Capital initial : "))
    risk_percent = float(input("Risque en % par trade : ").replace("%", "").strip())
    n_trades = int(input("Nombre de trades : "))
    winrate = float(input("Winrate en % : ").replace("%", "").strip())
    r_multiple = float(input("R multiple moyen (ex: 2) : "))

    risk_fraction = risk_percent / 100
    win_fraction = winrate / 100
    
    expectancy_theoretical = win_fraction * r_multiple - (1 - win_fraction) * 1
    
    wins = 0
    losses = 0
    current_streak = 0
    max_winning_streak = 0 
    max_losing_streak = 0
    
    for _ in range(n_trades):
        risk_amount = capital * risk_fraction

        if random.random() < win_fraction:
            capital += risk_amount * r_multiple
            wins += 1
            current_streak += 1
            # streak
            if current_streak >= 0:
                current_streak = 1
            else: current_streak = 1
        else:
            capital -= risk_amount
            losses += 1
            # streak
            if current_streak <= 0:
                current_streak -= 1
            else: current_streak = -1
        # update max streaks (toujours dans la boucle)
        if current_streak > max_winning_streak:
            max_winning_streak = current_streak
        if abs(current_streak) > max_losing_streak and current_streak < 0:
            max_losing_streak = abs(current_streak)
    
    total_R = wins * r_multiple - losses * 1 
    expectancy_real = total_R / n_trades
   
    print(f"\nWins: {wins} | Losses: {losses}")
    print(f"Capital final : {capital:.2f}")
    print(f"Max winning streak : {max_winning_streak}")
    print(f"Max losing streak : {max_losing_streak}")
    
    print(f"Expectancy théorique : {expectancy_theoretical:.4f} R")
    print(f"Expectancy réelle     : {expectancy_real:.4f} R")
    print(f"Diférence             : {(expectancy_real - expectancy_theoretical):.4} R")

# =======================
# MENU PRINCIPAL
# =======================
def main():
    choix = input("\nChoix mode (1 = normal, 2 = simulation) : ").strip()

    if choix == "2":
        run_simulation()
    else:
        run_normal()


if __name__ == "__main__":
    main()

    