import matplotlib.pyplot as plt
import numpy as np

# Data for plotting
x = np.linspace(0, 10, 100)
y = np.sin(x)
z = np.cos(x)

# Create a figure
fig, ax = plt.subplots()

# Plot a line graph
ax.plot(x, y, label='Sine')

# Plot a scatter plot
ax.scatter(x, z, color='red', label='Cosine')

# Add labels and title
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_title('Line Graph and Scatter Plot on the Same Figure')

# Add a legend
ax.legend()

# Show the plot
plt.show()
