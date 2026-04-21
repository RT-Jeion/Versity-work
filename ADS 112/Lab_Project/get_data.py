import csv
import numpy as np
import matplotlib.pyplot as plt


def generate_stock(name: str, alt_high: int, alt_low: int):
    # Generate 30 days of synthetic stock data for a single stock.
    rows = 30

    # Day index: 1 to 30
    dates = np.arange(1, rows + 1, dtype=int)

    # Open price is sampled independently each day from [alt_low, alt_high].
    open_price = np.random.uniform(alt_low, alt_high, size=rows)

    # Close price follows this rule:
    # day n close = day n+1 open for n=1..29, and day 30 close is random.
    close_price = np.empty(rows, dtype=float)
    close_price[:-1] = open_price[1:]                # dependency rule
    close_price[-1] = np.random.uniform(alt_low, alt_high)  # last one random

    # Log return for each day: r = ln(close/open)
    returns = np.log(close_price / open_price)

    # Standard deviation measures how spread-out returns are.
    std_dev = np.std(returns)

    # 30-day volatility estimate from daily std. deviation.
    volatility = std_dev * np.sqrt(30)

    # Store day, open, close, and return together for CSV writing/analysis.
    arr = np.column_stack((dates, open_price, close_price, returns))

    # Build a 31-point price path for plotting (day 0 open + 30 closes).
    prices = [open_price[0]]
    prices.extend(close_price)

    return name, arr, std_dev, volatility, prices


# Create three sample stocks with different price ranges.
stock1 = generate_stock("Apple", 100, 50)
stock2 = generate_stock("Amazon", 110, 70)
stock3 = generate_stock("RT_ORG", 150, 100)


# Save each stock's generated table and print its risk metrics.
for i in [stock1, stock2, stock3]:
    with open(f"{i[0].lower()}.csv", 'w', newline="") as f:
        write = csv.writer(f)
        # Note: rows include day/open/close/return values.
        write.writerow(["Days", "Open", "Close", "Returns"])
        write.writerows(i[1])
        print(f"Stock Price of {i[0]} saved to {i[0].lower()}.csv file")

    print("Stock:", i[0])
    print(f"Standard Deviation:", i[2])
    print(f"Volatility:", i[3])

    # Qualitative risk labels based on standard deviation of returns.
    if i[2] < 0.005:
        print("Very Low Volatility - stable / no movement")
    elif i[2] < 0.015:
        print("Low Volatility - smooth trend")
    elif i[2] < 0.03:
        print("Medium Volatility - normal trading range")
    elif i[2] < 0.06:
        print("High Volatility - risky, large swings")
    else:
        print("Extreme Volatility - highly unstable / speculative")

    print()


# Build day axis from 0..30 to match the 31-point generated price path.
days = np.arange(0, 31)

# Returns are recorded for days 1..30 in column index 3.
return_days = np.arange(1, 31)
stock1_returns = stock1[1][:, 3]
stock2_returns = stock2[1][:, 3]
stock3_returns = stock3[1][:, 3]

# Plot all generated stock paths on one chart.
plt.plot(days, stock1[4], label=stock1[0], linewidth=2)
plt.plot(days, stock2[4], label=stock2[0], linewidth=2)
plt.plot(days, stock3[4], label=stock3[0], linewidth=2)
plt.margins(x=0)

plt.title("Stock Price Movement")
plt.xlabel("Day")
plt.ylabel("Price")
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()

# Plot all daily return series on one chart.
plt.figure()
plt.plot(return_days, stock1_returns, label=stock1[0], linewidth=2)
plt.plot(return_days, stock2_returns, label=stock2[0], linewidth=2)
plt.plot(return_days, stock3_returns, label=stock3[0], linewidth=2)
plt.margins(x=0)

plt.title("Daily Log Returns")
plt.xlabel("Day")
plt.ylabel("Return")
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()


