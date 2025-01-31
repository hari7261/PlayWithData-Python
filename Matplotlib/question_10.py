import matplotlib.pyplot as plt
import numpy as np

# Generate random data for plotting
data = np.random.randn(100)

# Create a box plot
plt.boxplot(data)

# Add labels and title
plt.xlabel('X-axis Label')
plt.ylabel('Y-axis Label')
plt.title('Box Plot of Random Data')

# Show the plot
plt.show()
