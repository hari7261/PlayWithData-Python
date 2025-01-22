import matplotlib.pyplot as plt
import numpy as np

# Create a grid of points
x = np.linspace(-2 * np.pi, 2 * np.pi, 20)
y = np.linspace(-2 * np.pi, 2 * np.pi, 20)
X, Y = np.meshgrid(x, y)

# Define the vector field
U = np.cos(X)
V = np.sin(Y)

# Create a quiver plot
plt.quiver(X, Y, U, V)

# Add labels and title
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Quiver Plot (Vector Field)')

# Show the plot
plt.show()
