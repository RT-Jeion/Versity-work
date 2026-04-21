# Lab Project: Synthetic Stock Data Generator

This project generates synthetic stock market data for 3 sample stocks, saves each stock to a CSV file, calculates risk metrics, and plots both price movement and daily returns.

## What The Script Does

The script in [get_data.py](get_data.py) performs the following workflow:

1. Generates 30 days of stock data for each stock.
2. Calculates daily log returns using opening and closing prices.
3. Computes:
   - Standard deviation of returns
   - Volatility scaled for a 30-day period
4. Saves generated values to CSV files.
5. Prints volatility category labels in the terminal.
6. Plots all stock price series on one Matplotlib chart.
7. Plots all stock daily log return series on a second Matplotlib chart.

## Libraries Used

- `csv` (built-in): writes output data to CSV files
- `numpy`: random number generation and numerical calculations
- `matplotlib`: plotting stock price movement

Install dependencies from [requirements.txt](requirements.txt):

```bash
pip install -r requirements.txt
```

## How Data Is Generated

### Function: `generate_stock(name, alt_high, alt_low)`

This function generates one stock dataset and returns:

- `name`: stock name
- `arr`: table with columns `[Days, Open, Close, Returns]`
- `std_dev`: standard deviation of returns
- `volatility`: scaled volatility (`std_dev * sqrt(30)`)
- `prices`: price list used for plotting (31 values)

### Step-by-step logic

1. **Days column**
   - Creates day numbers from 1 to 30.

2. **Open prices**
   - Generates 30 random opening prices from a uniform distribution between `alt_low` and `alt_high`.

3. **Close prices**
   - For days 1 to 29:
     - `close[day] = open[next_day]`
   - For day 30:
     - random close value between `alt_low` and `alt_high`

4. **Returns**
   - Uses log return formula:
     - `return = ln(close / open)`

5. **Risk metrics**
   - Standard deviation of returns:
     - how dispersed daily returns are
   - Volatility (30-day scaling):
     - `volatility = std_dev * sqrt(30)`

6. **Price path for plotting**
   - Plot list starts with the first open price, then all 30 close prices.
   - This creates 31 points (day 0 to day 30).

## Stocks Generated In This Script

- Apple: range 50 to 100
- Amazon: range 70 to 110
- RT_ORG: range 100 to 150

## CSV Output Files

Running the script creates:

- `apple.csv`
- `amazon.csv`
- `rt_org.csv`

Each CSV contains these columns:

- `Days`
- `Open`
- `Close`
- `Returns`

## Volatility Labels Printed

Based on standard deviation (`std_dev`) of returns:

- `< 0.005`: Very Low Volatility
- `< 0.015`: Low Volatility
- `< 0.03`: Medium Volatility
- `< 0.06`: High Volatility
- `>= 0.06`: Extreme Volatility

## Plots Produced

The script produces two graphs:

1. Stock Price Movement
   - X-axis: Day (`0` to `30`)
   - Y-axis: Price
   - One line per stock with legend and grid

2. Daily Log Returns
   - X-axis: Day (`1` to `30`)
   - Y-axis: Return (`ln(close/open)`)
   - One line per stock with legend and grid

## How To Run

From the project folder, run:

```bash
python get_data.py
```

After running:

- CSV files are generated [stock_prices](stock_prices) folder
- Terminal shows standard deviation, volatility, and volatility category for each stock
- Two Matplotlib chart windows open (price movement and daily log returns)

## Notes

- Data is randomly generated each run, so values and chart lines will change every execution.
- If you need reproducible results, set a NumPy random seed at the top of the script (for example, `np.random.seed(42)`).
