import matplotlib.pyplot as plt
import numpy as np

# Generate random data
data = np.random.randn(100)

# Create a box plot
plt.boxplot(data)

# Add title and labels
plt.title('Box Plot of Random Data')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

# Show the plot
plt.show()
