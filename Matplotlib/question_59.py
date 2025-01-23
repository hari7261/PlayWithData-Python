import matplotlib.pyplot as plt
import numpy as np

# Generate some data
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Create a plot
fig, ax = plt.subplots()
ax.plot(x, y, label='Sine Wave')

# Customize fonts and text properties
plt.xlabel('x', fontsize=14, fontweight='bold', color='blue', family='serif')
plt.ylabel('y', fontsize=14, fontweight='bold', color='blue', family='serif')
plt.title('Plot with Custom Fonts and Text Properties', fontsize=16, fontweight='bold', color='red', family='serif')

# Add labels and title
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('Plot with Custom Fonts and Text Properties')
ax.legend()

# Show the plot
plt.show()
