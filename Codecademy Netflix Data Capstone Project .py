from matplotlib import pyplot as plt
import pandas as pd
import seaborn as sns

sns.set_palette("Paired")

# Load the datasets
netflix_stocks = pd.read_csv("NFLX.csv")
dowjones_stocks = pd.read_csv("DJI.csv")
netflix_stocks_quarterly = pd.read_csv("NFLX_daily_by_quarter.csv")

# Inspect the data
#print(netflix_stocks.head())
#print(dowjones_stocks.head())
#print(netflix_stocks_quarterly.head())
#print(netflix_stocks.Date.max())
#print(netflix_stocks.Date.min())

#Rename Adj Price
netflix_stocks.rename(columns={"Adj Close":"Price"}, inplace=True)
netflix_stocks_quarterly.rename(columns={"Adj Close":"Price"}, inplace=True)
dowjones_stocks.rename(columns={"Adj Close":"Price"}, inplace=True)

print(netflix_stocks.head())

#Create violin plot of quarterly stock price data
ax = sns.violinplot(data = netflix_stocks_quarterly, x = "Quarter", y = "Price", palette = "Pastel1")
ax.set_title("Distribution of 2017 Netflix Stock Prices by Quarter")
plt.xlabel("Business Quarters in 2017")
plt.ylabel("Closing Stock Price")
plt.show()


#Create scatterplot of earnings per share (EPS) by graphing the 
#estimate Yahoo projected for the Quarter compared to the actual earnings
x_positions = [1, 2, 3, 4]
chart_labels = ["1Q2017","2Q2017","3Q2017","4Q2017"]
earnings_actual =[.4, .15,.29,.41]
earnings_estimate = [.37,.15,.32,.41 ]


plt.scatter(x_positions, earnings_actual, color = "red", alpha = 0.5, label="Actual")
plt.scatter(x_positions, earnings_estimate, color = "lightskyblue", alpha = 0.5, label="Estimate")
plt.legend()
plt.xticks(x_positions, chart_labels)
plt.title("Earnings Per Share in Cents")
plt.show()


# Create bar chart to compare earnings and revenue reported by Netflix in 2017
# The metrics below are in billions of dollars
revenue_by_quarter = [2.79, 2.98,3.29,3.7]
earnings_by_quarter = [.0656,.12959,.18552,.29012]
quarter_labels = ["2Q2017","3Q2017","4Q2017", "1Q2018"]

# Revenue
n = 1  # This is our first dataset (out of 2)
t = 2 # Number of dataset
d = 4 # Number of sets of bars
w = 0.85 # Width of each bar
bars1_x = [t*element + w*n for element
             in range(d)]

# Earnings
n = 2  # This is our second dataset (out of 2)
t = 2 # Number of dataset
d = 4 # Number of sets of bars
w = 0.85 # Width of each bar
bars2_x = [t*element + w*n for element
             in range(d)]


middle_x = [ (a + b) / 2.0 for a, b in zip(bars1_x, bars2_x)]
labels = ["Revenue", "Earnings"]

plt.bar(bars1_x, revenue_by_quarter, label="Revenue")
plt.bar(bars2_x, earnings_by_quarter, label="Earnings")
plt.legend()
plt.xticks(middle_x, quarter_labels)
plt.title("Earnings and revenue reported by Netflix in 2017")
plt.show()



#Plot two line graphs to compare Netflix stock to the Dow Jones Industrial Average in 2017

ax1 = plt.subplot(1, 2, 1)

plt.plot(netflix_stocks["Date"], netflix_stocks["Price"])
ax1.set_title("Netflix")
ax1.set_xlabel("Date")
ax1.set_ylabel("Stock Price")

ax2 = plt.subplot(1, 2, 2)
plt.plot(dowjones_stocks["Date"], dowjones_stocks["Price"])
ax2.set_title("Dow Jones")
ax2.set_xlabel("Date")
ax2.set_ylabel("Stock Price")

plt.subplots_adjust(wspace=.5)
plt.show()