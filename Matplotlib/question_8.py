import matplotlib.pyplot as plt
import numpy as np

# Generate random data for plotting
x = np.random.rand(50)
y = np.random.rand(50)

# Create a scatter plot
plt.scatter(x, y)

# Add labels and title
plt.xlabel('X-axis Label')
plt.ylabel('Y-axis Label')
plt.title('Scatter Plot of Random Data')

# Show the plot
plt.show()
