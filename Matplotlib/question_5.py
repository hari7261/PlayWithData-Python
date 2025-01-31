import matplotlib.pyplot as plt
import numpy as np

# This code generates a random dataset and creates a histogram

# Generate a random dataset
data = np.random.randn(1000)

# Plot a histogram
plt.hist(data, bins=30, edgecolor='black')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Histogram of Random Dataset')
plt.show()
