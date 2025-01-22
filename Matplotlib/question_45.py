import matplotlib.pyplot as plt
import numpy as np
from matplotlib.widgets import Button

# Generate some data
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Create a plot
fig, ax = plt.subplots()
line, = ax.plot(x, y, label='sin(x)')

# Add buttons
ax_button1 = plt.axes([0.7, 0.05, 0.1, 0.075])
button1 = Button(ax_button1, 'Button 1')

ax_button2 = plt.axes([0.81, 0.05, 0.1, 0.075])
button2 = Button(ax_button2, 'Button 2')

# Button click event handlers
def on_button1_clicked(event):
    line.set_ydata(np.sin(x))
    fig.canvas.draw_idle()

def on_button2_clicked(event):
    line.set_ydata(np.cos(x))
    fig.canvas.draw_idle()

button1.on_clicked(on_button1_clicked)
button2.on_clicked(on_button2_clicked)

# Add labels and title
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('Plot with Buttons using matplotlib.widgets')
ax.legend()

# Show the plot
plt.show()
