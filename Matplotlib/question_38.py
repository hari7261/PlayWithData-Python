import matplotlib.pyplot as plt
import numpy as np

# Create data for the contour plot
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
x, y = np.meshgrid(x, y)
z = np.sin(np.sqrt(x**2 + y**2))

# Create a contour plot
plt.contour(x, y, z, cmap='viridis')

# Add labels and title
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Contour Plot')

# Show the plot
plt.show()
