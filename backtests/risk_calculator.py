from statistics import mode
import random 
print("=== Risk Calculator ===")
def calcul_r(capital, risk_percent, entry, stop, target):
    risk_amount = capital * (risk_percent / 100)
    distance_stop = abs(entry - stop)
    quantity = risk_amount / distance_stop
    reward_distance =  abs(entry - target)
    profit = reward_distance * quantity
    r_ratio = profit / risk_amount
    return risk_amount, r_ratio, distance_stop, quantity, reward_distance, profit

capital = float(input("Capital total : "))
risk_percent = float(input("Risque en % par trade : ").replace("%", "").strip())
entry_price = float(input("Prix d'entrée : "))
stop_price = float(input("Prix du stop : "))
take_profit = float(input("Prix take profit : "))
risk_amount, distance_stop, quantity, reward_distance, profit, r_ratio = calcul_r(capital, risk_percent, entry_price, stop_price, take_profit)

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
    wins = 0
    losses = 0
    gain = 0
    peak = capital
    max_drawdown = 0.0
    capital_initial = capital
    for i in range(1, n_trades + 1):
        risk_amount = capital * risk_fraction
        # gain = +R*risk_amount si win, sinon -1*risk_amount
        # on fait simple: on gagne si i dans la partie "wins" selon winrate
        # (plus tard on fera alèatoire)
        if random.random() < win_fraction:
            gain += risk_amount * r_multiple
            wins += 1
            r_total += r_multiple
        if capital > peak:
            peak = capital
        drawdown = peak - capital
        if drawdown > max_drawdown:
            max_drawdown = drawdown
        else:
            gain = -risk_amount
            capital += gain
            losses += 1
            r_total -= 1
    percent_final = (capital / capital_initial - 1) * 100
    print(f"Wins: {wins} | losses: {losses}")
    print(f"Max drawdown: {max_drawdown:.2f}")
    print(f"\nCapital final : {capital:.2f}")
    print(f"\nWins : {wins}")
    print(f"Losses : {losses}")
    print(f"Performance : {percent_final:.2f}%")
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

    print(f"Gain potentiel en % du capital : {percent_gain:.2f}%")
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

