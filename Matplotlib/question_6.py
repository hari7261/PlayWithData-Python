import matplotlib.pyplot as plt
import numpy as np

# Generate random data for plotting
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Create a line plot
plt.plot(x, y)

# Add labels and title
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Line Plot of Sine Wave')

# Show the plot
plt.show()
