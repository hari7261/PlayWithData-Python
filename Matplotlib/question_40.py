import matplotlib.pyplot as plt
import numpy as np

# Create a grid of points
Y, X = np.mgrid[-3:3:100j, -3:3:100j]

# Define the vector field
U = -1 - X**2 + Y
V = 1 + X - Y**2

# Create a streamplot
plt.streamplot(X, Y, U, V, color=np.sqrt(U**2 + V**2), cmap='viridis')

# Add labels and title
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Streamplot')

# Show the plot
plt.show()
