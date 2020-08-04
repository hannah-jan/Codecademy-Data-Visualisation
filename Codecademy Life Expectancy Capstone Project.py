from matplotlib import pyplot as plt
import pandas as pd
import seaborn as sns

sns.set_palette("Paired")

# Load the datasets
all_data = pd.read_csv("all_data.csv")

# Inspect the data
#print(all_data.head())
#print(all_data.Country.unique())
#print(all_data.Year.unique())


#Rename Life expectancy at birth (years)"
all_data.rename(columns = {"Life expectancy at birth (years)": "LEABY"}, inplace=True)
#print(all_data.head())


# Examine to compare life expectancy and GDP for each country
countries = all_data.Country.unique()
countries[4] = "USA"

# Plot GDP for each country
fig = plt.subplots(figsize=(15, 10)) 
ax1 = plt.subplot(1, 2, 1)
sns.barplot(data = all_data, x="Country", y="GDP", ci=False)
ax1.set_xticks(range(len(countries)))
ax1.set_xticklabels(countries, rotation = 30)
plt.ylabel("GDP in Trillions of U.S. Dollars")
plt.title("GDP for each Country")

# Plot life expectancy for each country
ax2 = plt.subplot(1, 2, 2)
sns.barplot(data = all_data, x="Country", y="LEABY", ci=False)
ax2.set_xticks(range(len(countries)))
ax2.set_xticklabels(countries, rotation = 30)
plt.ylabel("Life Expectancy at Birth (years)")
plt.title("Life Expectancy for each Country")

plt.subplots_adjust(wspace=.2)
plt.show()


# Plot Violin Plots To Compare Life Expectancy Distributions

fig = plt.subplots(figsize=(15, 10)) 
ax3 = sns.violinplot(data = all_data, x ="Country", y="LEABY")
ax3.set_xticks(range(len(countries)))
ax3.set_xticklabels(countries, rotation = 30)
plt.ylabel("Life Expectancy at Birth (years)")
plt.show()


# Bar Plots to compare the GDPs and Life Expectancy of the countries over time
f, ax4 = plt.subplots(figsize=(10, 15)) 
sns.barplot(x="Country", y="GDP", data = all_data, hue = "Year", palette="YlGnBu")
ax4.set_xticks(range(len(countries)))
ax4.set_xticklabels(countries, rotation = 30)
plt.ylabel("GDP in Trillions of U.S. Dollars")
plt.legend(loc=0)
plt.show()

f, ax5 = plt.subplots(figsize=(10, 15)) 
sns.barplot(x="Country", y="LEABY", data = all_data, hue = "Year", palette="YlGnBu")
ax4.set_xticks(range(len(countries)))
ax4.set_xticklabels(countries, rotation = 30)
plt.ylabel("Life Expectancy at Birth (years)")
plt.legend(loc=0)
plt.show()


# Use FacetGrid to see trends in GDP 
g = sns.FacetGrid(all_data, col="Year", hue= "Country", col_wrap=4, size=2)
g = (g.map(plt.scatter, "GDP", "LEABY", edgecolor="w").add_legend())
plt.show()


# Line graphs of Life Expectancy over time for each Country
g2 = sns.FacetGrid(all_data, col="Country", col_wrap=3, size=4)
g2 = (g2.map(plt.plot, "Year", "LEABY").add_legend())
plt.show()

# Line graphs of GDP over time for each Country
g3 = sns.FacetGrid(all_data, col="Country", col_wrap=3, size=4)
g3 = (g3.map(plt.plot, "Year", "GDP").add_legend())
plt.show()