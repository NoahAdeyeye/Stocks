import csv
import matplotlib.pyplot as plt
import numpy as np

Full_GOOG_stock_list = []
GOOG_Year_Price = []
Full_dates = []
Dates = []

with open('GOOG.csv', 'r')as Gfile:
  GFile = csv.reader(Gfile)
  first_line = next(GFile)
  for lines in GFile:
    x = lines[0].split("-")
    Full_dates.append(x[0])
    lines = float(lines[1])
    Full_GOOG_stock_list.append(lines)
for i in range(len(Full_GOOG_stock_list)):
    if i % 12 == 0:
       GOOG_Year_Price.append(Full_GOOG_stock_list[i])
       Dates.append(Full_dates[i])

Full_MSFT_stock_list = []
MSFT_Year_Price = []
with open('MSFT.csv', 'r')as Mfile:
  MFile = csv.reader(Mfile)
  first_line = next(MFile)
  for lines in MFile:
    lines = float(lines[1])
    Full_MSFT_stock_list.append(lines)
for i in range(len(Full_MSFT_stock_list)):
    if i % 12 == 0:
       MSFT_Year_Price.append(Full_MSFT_stock_list[i])

Full_AAPL_stock_list = []
AAPL_Year_Price = []
with open('AAPL.csv', 'r')as Afile:
  AFile = csv.reader(Afile)
  first_line = next(AFile)
  for lines in AFile:
    lines = float(lines[1])
    Full_AAPL_stock_list.append(lines)
for i in range(len(Full_AAPL_stock_list)):
    if i % 12 == 0:
       AAPL_Year_Price.append(Full_AAPL_stock_list[i])

x = Dates
m = MSFT_Year_Price
plt.plot(x, m)
g = GOOG_Year_Price
plt.plot(x, g)
a = AAPL_Year_Price
plt.plot(x, a)
plt.legend(['MSFT','AAPL','GOOG'])
plt.title("Stocks over decades")
plt.xlabel("Year")
plt.ylabel("Price")
plt.show()
