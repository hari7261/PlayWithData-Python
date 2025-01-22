import matplotlib.pyplot as plt
import numpy as np
import mpld3

# Generate some data
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Create a plot
fig, ax = plt.subplots()
ax.plot(x, y, label='sin(x)')

# Add labels and title
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('Interactive Plot using mpld3')
ax.legend()

# Convert the plot to an interactive plot using mpld3
mpld3.show()
