import matplotlib.pyplot as plt
import numpy as np

# Generate some data
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Create a plot
fig, ax = plt.subplots()
ax.plot(x, y, label='Sine Wave')

# Add advanced annotations and text
ax.annotate('Local Max', xy=(np.pi/2, 1), xytext=(np.pi/2, 1.5),
             arrowprops=dict(facecolor='black', shrink=0.05))
ax.annotate('Local Min', xy=(3*np.pi/2, -1), xytext=(3*np.pi/2, -1.5),
             arrowprops=dict(facecolor='red', shrink=0.05))

# Add text box
textstr = 'Equation: y = sin(x)'
props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)
ax.text(0.05, 0.95, textstr, transform=ax.transAxes, fontsize=14,
        verticalalignment='top', bbox=props)

# Add labels and title
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('Plot with Advanced Annotations and Text')
ax.legend()

# Show the plot
plt.show()
