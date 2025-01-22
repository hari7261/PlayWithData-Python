import matplotlib.pyplot as plt
import numpy as np
from matplotlib.widgets import Slider

# Generate some data
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Create a plot
fig, ax = plt.subplots()
line, = ax.plot(x, y, label='sin(x)')

# Add sliders
ax_slider = plt.axes([0.25, 0.1, 0.65, 0.03])
slider = Slider(ax_slider, 'Frequency', 0.1, 10.0, valinit=1.0)

# Update function
def update(val):
    line.set_ydata(np.sin(slider.val * x))
    fig.canvas.draw_idle()

slider.on_changed(update)

# Add labels and title
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('Plot with Slider using matplotlib.widgets')
ax.legend()

# Show the plot
plt.show()
