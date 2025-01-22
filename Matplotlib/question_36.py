import matplotlib.pyplot as plt
import numpy as np

# Create data for the polar plot
theta = np.linspace(0, 2 * np.pi, 100)
r = np.abs(np.sin(theta))

# Create a polar plot
plt.polar(theta, r)
plt.title('Polar Plot')
plt.show()
