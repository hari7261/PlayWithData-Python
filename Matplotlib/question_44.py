import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation

fig, ax = plt.subplots()
x = np.linspace(0, 2 * np.pi, 100)
line, = ax.plot(x, np.sin(x))

def update(num, x, line):
    line.set_ydata(np.sin(x + num / 10.0))
    return line,

ani = animation.FuncAnimation(fig, update, frames=100, fargs=[x, line], interval=50)
plt.show()
