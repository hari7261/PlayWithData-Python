import matplotlib.pyplot as plt
import numpy as np

# Generate some data
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Create a plot
plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Sine Wave')

# Save the plot with a transparent background
plt.savefig('sine_wave_transparent.png', transparent=True)

# Show the plot
plt.show()
