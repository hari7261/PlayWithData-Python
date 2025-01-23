import matplotlib.pyplot as plt
import numpy as np

# Generate some data
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Create a plot with advanced customization
fig, ax = plt.subplots()

# Plot the data with custom line style and color
ax.plot(x, y, linestyle='--', color='purple', linewidth=2, label='Sine Wave')

# Add grid with custom style
ax.grid(True, which='both', linestyle=':', linewidth=0.5, color='gray')

# Add title and labels with custom font properties
ax.set_title('Advanced Customized Plot', fontsize=16, fontweight='bold', color='blue')
ax.set_xlabel('X-axis', fontsize=14, fontstyle='italic', color='green')
ax.set_ylabel('Y-axis', fontsize=14, fontstyle='italic', color='green')

# Customize ticks
ax.tick_params(axis='x', colors='red', direction='in', length=6, width=2)
ax.tick_params(axis='y', colors='red', direction='in', length=6, width=2)

# Add legend with custom properties
ax.legend(loc='upper right', fontsize=12, frameon=True, shadow=True, facecolor='lightyellow')

# Show the plot
plt.show()
