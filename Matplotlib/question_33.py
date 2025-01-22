import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)
y = np.sin(x)

plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Plot with Axis Limits')

# Set the limits of the x-axis and y-axis
plt.xlim(2, 8)
plt.ylim(-0.5, 0.5)

plt.show()
