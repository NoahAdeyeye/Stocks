Welcome to the Stocks Comparer project! This project aims to explore the stock market. Understanding stock trends is an intergral aspect of finance, and this project delves into creating a tool for comparing stock prices over time.

## How It Works

The Stocks Comparer retrieves stock data from CSV files (in this example, GOOG.csv, MSFT.csv, and AAPL.csv) and processes it to visualize the yearly stock prices of Microsoft (MSFT), Apple (AAPL), and Google (GOOG). The project utilizes Python, CSV parsing, and the Matplotlib library for plotting.

## Example

Here's a simple example of how the project works:

```python
# Your code here (import statements and data processing)
# ...

# Plotting
plt.plot(x, m)
plt.plot(x, g)
plt.plot(x, a)
plt.legend(['MSFT', 'AAPL', 'GOOG'])
plt.title("Stocks over decades")
plt.xlabel("Year")
plt.ylabel("Price")
plt.show()
```

## How to Use

1. Use CSV files or replace existing ones with your stock data.
2. Run the script to see the visual representation of stock prices.

## Dependencies

This project relies on the following Python libraries:

- `csv`: For parsing CSV files.
- `matplotlib`: For creating visualizations.
- `numpy`: For numerical operations.


Experiment and enhance the project according to your preferences and stocks!
