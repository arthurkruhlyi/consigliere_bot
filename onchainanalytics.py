import requests
import matplotlib.pyplot as plt

# Make a GET request to the Coindesk API to retrieve the historical Bitcoin price data
response = requests.get('https://api.coindesk.com/v1/bpi/historical/close.json?currency=USD')

# Convert the JSON response into a Python dictionary
data = response.json()
print(data)
# Extract the historical Bitcoin prices from the dictionary
prices = list(data['bpi'].values())

# Create a list of dates corresponding to the historical Bitcoin prices
dates = list(data['bpi'].keys())

# Plot the historical Bitcoin prices on a chart
plt.plot(dates, prices)

# Customize the chart
plt.title('Bitcoin Price (USD)')
plt.xlabel('Date')
plt.ylabel('Price (USD)')

# Show the chart
plt.show()