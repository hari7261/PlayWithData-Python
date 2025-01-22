import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0.1, 10, 100)
y = np.exp(x)

plt.plot(x, y)
plt.xscale('log')
plt.xlabel('X-axis (log scale)')
plt.ylabel('Y-axis')
plt.title('Plot with Logarithmic Scale on X-axis')
plt.show()
