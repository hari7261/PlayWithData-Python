import matplotlib.pyplot as plt
import numpy as np
import mplcursors

# Generate some data
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Create a plot
fig, ax = plt.subplots()
ax.plot(x, y, label='sin(x)')

# Add hover effects using mplcursors
cursor = mplcursors.cursor(ax, hover=True)
cursor.connect("add", lambda sel: sel.annotation.set_text(f"x={sel.target[0]:.2f}, y={sel.target[1]:.2f}"))

# Add labels and title
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('Hover Effects using mplcursors')
ax.legend()

# Show the plot
plt.show()
