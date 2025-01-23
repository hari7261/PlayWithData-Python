import matplotlib.pyplot as plt
import numpy as np

# Generate some data
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Create a plot with custom color maps
fig, ax = plt.subplots()

# Plot the data with a custom color map
sc = ax.scatter(x, y, c=y, cmap='viridis')

# Add a color bar
cbar = plt.colorbar(sc)
cbar.set_label('Color Intensity')

# Add labels and title
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('Plot with Custom Color Maps')

# Show the plot
plt.show()
