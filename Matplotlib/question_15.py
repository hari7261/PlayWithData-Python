import matplotlib.pyplot as plt
import numpy as np

# Data for plotting
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)
y3 = np.tan(x)
y4 = np.exp(x)

# Create a figure with multiple subplots and share the y-axis
fig, axs = plt.subplots(2, 2, sharey=True)

# Plot data on each subplot
axs[0, 0].plot(x, y1)
axs[0, 0].set_title('Sine')

axs[0, 1].plot(x, y2, 'tab:orange')
axs[0, 1].set_title('Cosine')

axs[1, 0].plot(x, y3, 'tab:green')
axs[1, 0].set_title('Tangent')

axs[1, 1].plot(x, y4, 'tab:red')
axs[1, 1].set_title('Exponential')

# Add a title to the entire figure
fig.suptitle('Subplots with Shared Y-Axis')

# Show the plot
plt.show()
