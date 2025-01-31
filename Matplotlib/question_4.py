import matplotlib.pyplot as plt
import numpy as np

# This code generates two random datasets and creates a scatter plot

# Generate two random datasets
x = np.random.rand(50)
y = np.random.rand(50)

# Create a scatter plot
plt.scatter(x, y)
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Scatter Plot of Two Random Datasets')
plt.show()
