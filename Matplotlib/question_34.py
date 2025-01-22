import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0, 10, 0.1)
y1 = np.sin(x)
y2 = np.cos(x)

fig, ax1 = plt.subplots()

ax1.plot(x, y1, 'b-')
ax1.set_xlabel('X data')
ax1.set_ylabel('Y1 data', color='b')

ax2 = ax1.twinx()
ax2.plot(x, y2, 'r-')
ax2.set_ylabel('Y2 data', color='r')

plt.title('Plot with Secondary Y-Axis')
plt.show()
