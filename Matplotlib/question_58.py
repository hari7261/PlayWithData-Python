import matplotlib.pyplot as plt
import numpy as np

# Generate some data
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Create a plot with custom markers and line styles
plt.plot(x, y, marker='o', linestyle='--', color='b', label='Sine Wave')

# Add labels and title
plt.xlabel('x')
plt.ylabel('y')
plt.title('Plot with Custom Markers and Line Styles')
plt.legend()

# Show the plot
plt.show()
