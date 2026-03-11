import matplotlib.pyplot as plt
import random
import numpy as np

def simulate(capital_initial, risk_percent, n_trade, winrate_percent, r_multiple, seed=None):
    
    if seed is not None:
        random.seed(seed)

    capital = capital_initial
    peak = capital
    max_drawdown = 0.0
    
    recovery_times = []
    recovery_counter = 0
    in_drawdown = False

    wins = 0
    losses = 0

    current_streak = 0
    max_winning_streak = 0
    max_losing_streak = 0

    win_fraction = winrate_percent / 100
    risk_fraction = risk_percent / 100
 
    equity_curve = []    # < ICI on crée la liste

    for _ in range(n_trade):

        risk_amount = capital * risk_fraction
        
        if random.random() < win_fraction:
            # WIN
            gain = risk_amount * r_multiple
            capital += gain
            wins += 1

            current_streak = current_streak + 1 if current_streak >= 0 else 1
            max_winning_streak = max(max_winning_streak, current_streak)

        else:
            # LOSS
            capital -= risk_amount
            losses += 1

            current_streak = current_streak - 1 if current_streak <= 0 else -1
            max_losing_streak = max(max_losing_streak, abs(current_streak))
        
        equity_curve.append(capital)       # < ICI on enregistre le capital
        # drawdown
        peak = max(peak, capital)
        drawdown = (peak - capital) / peak
        max_drawdown = max(max_drawdown, drawdown)

    if  capital < peak:
        in_drawdown = True
        recovery_counter += 1
    elif in_drawdown and capital >= peak:
        recovery_times.append(recovery_counter)
        recovery_counter = 0
        in_drawdown = False
    
    growth_pct = (capital / capital_initial - 1) * 100

    if capital < peak:
        in_drawdown = True
        recovery_counter += 1
    elif in_drawdown and capital >= peak:
        recovery_times.append(recovery_counter)
        recovery_counter = 0 
        in_drawdown = False
    
    if len(recovery_times) > 0:
        avg_recovery = sum(recovery_times) / len(recovery_times)
        worst_recovery = max(recovery_times)
    else:
        avg_recovery = 0
        worst_recovery = 0

    return {
        "risk": risk_percent,
        "final": capital,
        "growth": growth_pct,
        "wins": wins,
        "losses": losses,
        "max_win_streak": max_winning_streak,
        "max_losses_streak": max_losing_streak,
        "max_dd_pct": max_drawdown * 100,
        "equity": equity_curve,
        "avg_recovery": avg_recovery,
        "worst_recovery": worst_recovery,
        }


def main():
    capital_initial = 100
    n_trade = 1000
    winrate_percent = 30
    r_multiple = 3
    plt.figure()
    n_runs = 20

    for risk_percent in [0.5, 0.75, 1, 1.25, 1.5, 2,]:
        total_final = 0 
        total_dd = 0
        worst_dd_seen = 0.0
        dd_above_50 = 0
        ruin_count = 0
        best_risk = None
        best_score = -float("inf")
        all_equities = []

        for seed in range(n_runs):
            result = simulate(capital_initial, risk_percent, n_trade, winrate_percent, r_multiple, seed=seed)
            if result["final"] < capital_initial * 0.5:
                ruin_count += 1

            total_final += result["final"]
            total_dd += result["max_dd_pct"]
            worst_dd_seen = max(worst_dd_seen, result["max_dd_pct"])
            
            if result["max_dd_pct"] > 50:
                dd_above_50 += 1

            equity = result["equity"]
            all_equities.append(equity)
            plt.plot(equity, alpha=0.3)
        
        avg_final = total_final / n_runs
        avg_dd = total_dd / n_runs
        prob_dd_50 = dd_above_50 / n_runs
        score_1 = avg_final * (1 - prob_dd_50)
        score_2 = avg_final / (1 + avg_dd/100)
        if score_2 > best_score:
            best_score = score_2
            best_risk = risk_percent

        mean_equity = np.mean(all_equities, axis=0)
        plt.plot(mean_equity, linewidth=3)

        plt.title("Monte Carlo Equity Curve")
        plt.xlabel("Trades")
        plt.ylabel("Capital")
        plt.savefig("../results/monte_carlo.png")
        plt.show()

        print("\n===========================")
        print(f"Risk = {risk_percent}%")
        print(f"Avg capital final : {avg_final:.2f}")
        print(f"Avg max DD        : {avg_dd:.2f}%")
        print(f"Worst DD observed : {worst_dd_seen:.2f}%")
        print(f"Prob DD > 50%     : {dd_above_50 / n_runs * 100:.2f}#")
        print(f"Score adjusted (catastrophe) : {score_1:.2f}")
        print(f"Score adjusted (volatility)  : {score_2:.2f}")
        print("length equity curve:", len(result["equity"]))
        print("first 10 equity values:", equity[:10])
        print(f"Avg recovery time      : {result['avg_recovery']:.2f} trades")
        print(f"Worst recovery time    : {result['worst_recovery']} trades")
        print("\nBest risk level :", best_risk, "%")
        print("Best score :", round(best_score, 2))


if __name__ == "__main__":
    main()