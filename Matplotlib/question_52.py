import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Create a figure and axis
fig, ax = plt.subplots()
xdata, ydata = [], []
ln, = plt.plot([], [], 'r-', animated=True)

# Initialize the plot
def init():
    ax.set_xlim(0, 2*np.pi)
    ax.set_ylim(-1, 1)
    return ln,

# Update the plot with new data
def update(frame):
    xdata.append(frame)
    ydata.append(np.sin(frame))
    ln.set_data(xdata, ydata)
    return ln,

# Create an animation
ani = animation.FuncAnimation(fig, update, frames=np.linspace(0, 2*np.pi, 128),
                              init_func=init, blit=True)

# Add title and labels
plt.title('Real-Time Data Plot using Matplotlib')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

# Show the plot
plt.show()
