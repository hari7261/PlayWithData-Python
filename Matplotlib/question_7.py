import matplotlib.pyplot as plt
import numpy as np

# Generate random data for plotting
x = np.arange(0, 10)
y = np.random.randint(1, 20, size=10)

# Create a bar plot
plt.bar(x, y)

# Add labels and title
plt.xlabel('X-axis Label')
plt.ylabel('Y-axis Label')
plt.title('Bar Plot of Random Data')

# Show the plot
plt.show()
