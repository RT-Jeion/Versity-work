import csv
import numpy as np
import matplotlib.pyplot as plt
# imported neccesary Libraries

def generate_stock(name: str, alt_high: int, alt_low: int):
    
    # For Generate 30 days data for any corresponding data's
    rows = 30

    # Day index: 1 to 30
    dates = np.arange(1, rows + 1, dtype=int)

    # Randomly Generated array/list (size=30 data) by numpy library, alt_low and alt_high are the range of randomly generated price.
    open_price = np.random.uniform(alt_low, alt_high, size=rows)

    # Todays closing price is yesterday's opening price.
    # so 2nd to 30th days opening price is 1st to 29th day's closing price

    close_price = np.empty(rows, dtype=float) # created empty array/list temporary
    close_price[:-1] = open_price[1:]
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

    # here the data's are returned as Dictionary format.
    return {"Name": name, "Data": arr, "Std_dev": std_dev, "Volatility": volatility, "Prices": prices}


# Create three sample stocks with different price ranges.
stock1 = generate_stock("ZRex", 100, 50)
stock2 = generate_stock("Honey", 110, 70)
stock3 = generate_stock("RT_ORG", 150, 100)


# Save each stock's date, open price, close price and reuturns in csv files.

for i in [stock1, stock2, stock3]:  # put 3 stocks in list to iterate each stocks one by one.
    with open(f"stock_prices/{i["Name"].lower()}.csv", 'w', newline="") as f:
        write = csv.writer(f)

        write.writerow(["Days", "Open", "Close", "Returns"]) # writing heads rows of the csv file's data
        write.writerows(i["Data"])      # main csv data in nested list format
        print(f"Stock Price of {i["Name"]} saved to {i["Name"].lower()}.csv file")

    print("Stock:", i["Name"])
    print(f"Standard Deviation:", i["Std_dev"])
    print(f"Volatility:", i["Volatility"])

    # Qualitative risk labels based on standard deviation of returns.
    if i["Volatility"] < 0.005:
        print("Very Low Volatility - stable / no movement")
    elif i["Volatility"] < 0.015:
        print("Low Volatility - smooth trend")
    elif i["Volatility"] < 0.03:
        print("Medium Volatility - normal trading range")
    elif i["Volatility"] < 0.06:
        print("High Volatility - risky, large swings")
    else:
        print("Extreme Volatility - highly unstable / speculative")

    print()


# Build day axis from 0..30 to match the 31-point generated price path.
days = np.arange(0, 31)

# Returns are recorded for days 1..30 in column index 3.
return_days = np.arange(1, 31)
stock1_returns = stock1["Data"][:, 3]
stock2_returns = stock2["Data"][:, 3]
stock3_returns = stock3["Data"][:, 3]


fig, axs = plt.subplots(2,1, sharex=True)
# Here fig is whole figure and axs are the subplots. (2,1) means sub plots placement
# 2 row, 1 columns. Total 2 subplot

# Plot all generated stock paths on one chart.
# axs[0] 1st subplot: Graph of Stock Prices

# plot(values in x axis, values in y axis )
axs[0].plot(days, stock1["Prices"], label=stock1["Name"], linewidth=2)
axs[0].plot(days, stock2["Prices"], label=stock2["Name"], linewidth=2)
axs[0].plot(days, stock3["Prices"], label=stock3["Name"], linewidth=2)
axs[0].margins(x=0)     # Price line starts from x = 0.


axs[0].set_title("Stock Price Movement")    # title of the subplot
axs[0].set_xlabel("Day")    # x axis lebel
axs[0].set_ylabel("Price")  # y axis lebel
axs[0].legend()     # Identifing the lines 
axs[0].grid(True, alpha=0.3)  # alpha means density of the grids


# Plot all daily return series on one chart.
# axs[1] 2nd subplost: Graph of Daily Returns
axs[1].plot(return_days, stock1_returns, label=stock1["Name"], linewidth=2)
axs[1].plot(return_days, stock2_returns, label=stock2["Name"], linewidth=2)
axs[1].plot(return_days, stock3_returns, label=stock3["Name"], linewidth=2)
axs[1].margins(x=0)

axs[1].set_title("Daily Log Returns")
axs[1].set_xlabel("Day")
axs[1].set_ylabel("Return")
axs[1].legend()
axs[1].grid(True, alpha=0.3)

plt.tight_layout()   # format the graph properly to avoid overwrite
plt.savefig("figures/plots.png")    # save the figure
plt.show()  # Show the Figure ( pop up on screen )