import matplotlib.pyplot as plt
import numpy as np

# This code creates subplots with 2 rows and 2 columns and plots different mathematical functions on each subplot

# Data for plotting
x = np.linspace(0, 10, 100)  # np.linspace generates 100 values between 0 and 10
y1 = np.sin(x)
y2 = np.cos(x)
y3 = np.tan(x)
y4 = np.exp(x)

# Create subplots with 2 rows and 2 columns
fig, axs = plt.subplots(2, 2)  # plt.subplots creates a figure and a grid of subplots

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
fig.suptitle('Subplots with 2 Rows and 2 Columns')

# Show the plot
plt.show()
