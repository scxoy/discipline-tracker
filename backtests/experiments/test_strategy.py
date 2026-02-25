import random


def simulate(capital_initial, risk_percent, n_trade, winrate_percent, r_multiple, seed=None):

    if seed is not None:
        random.seed(seed)

    capital = capital_initial
    peak = capital
    max_drawdown = 0.0

    wins = 0
    losses = 0

    current_streak = 0
    max_winning_streak = 0
    max_losing_streak = 0

    win_fraction = winrate_percent / 100
    risk_fraction = risk_percent / 100

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

        # drawdown
        peak = max(peak, capital)
        drawdown = (peak - capital) / peak
        max_drawdown = max(max_drawdown, drawdown)

    growth_pct = (capital / capital_initial - 1) * 100

    return {
        "risk": risk_percent,
        "final": capital,
        "growth": growth_pct,
        "wins": wins,
        "losses": losses,
        "max_win_streak": max_winning_streak,
        "max_losses_streak": max_losing_streak,
        "max_dd_pct": max_drawdown * 100,
    }


def main():
    capital_initial = 100
    n_trade = 1000
    winrate_percent = 30
    r_multiple = 3

    for risk_percent in [1, 2]:

        result = simulate(
            capital_initial,
            risk_percent,
            n_trade,
            winrate_percent,
            r_multiple,
            seed=42
        )

        print("\n===========================")
        print(f"Risk = {result['risk']}%")
        print(f"Capital final : {result['final']:.2f}")
        print(f"Croissance : {result['growth']:.2f}%")
        print(f"Wins / Losses : {result['wins']} / {result['losses']}")
        print(f"Max win streak : {result['max_win_streak']}")
        print(f"Max losses streak : {result['max_losses_streak']}")
        print(f"Max drawdown : {result['max_dd_pct']:.2f}%")


if __name__ == "__main__":
    main()