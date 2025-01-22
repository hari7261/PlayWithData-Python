import matplotlib.pyplot as plt
import pandas as pd

# Load stock price data
data = pd.read_csv('stock_data.csv')

# Convert the date column to datetime
data['Date'] = pd.to_datetime(data['Date'])

# Set the date column as the index
data.set_index('Date', inplace=True)

# Plot the stock price data
plt.figure(figsize=(10, 5))
plt.plot(data['Close'], label='Close Price')
plt.xlabel('Date')
plt.ylabel('Stock Price')
plt.title('Stock Price Data Over Time')
plt.legend()
plt.show()
