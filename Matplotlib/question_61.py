import matplotlib.pyplot as plt
import numpy as np

# Generate random data for the histogram
data = np.random.randn(1000)

# Create a histogram
plt.hist(data, bins=30, alpha=0.5, label='Histogram', density=True)

# Add a density plot
density = np.linspace(min(data), max(data), 100)
plt.twinx().plot(density, 1/(np.sqrt(2 * np.pi)) * np.exp(-0.5 * density**2), label='Density Plot', color='red')

# Add labels and title
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Histogram with Density Plot')
plt.legend()

# Show the plot
plt.show()
