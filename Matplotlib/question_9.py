import matplotlib.pyplot as plt
import numpy as np

# Generate random data for plotting
data = np.random.randn(100)

# Create a histogram
plt.hist(data, bins=10, edgecolor='black')

# Add labels and title
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Histogram of Random Data')

# Show the plot
plt.show()
