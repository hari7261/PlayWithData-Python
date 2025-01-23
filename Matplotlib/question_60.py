import matplotlib.pyplot as plt
import numpy as np

# Generate some data
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Create a plot
fig, ax = plt.subplots()
ax.plot(x, y, label='Sine Wave')

# Customize legends and labels
ax.legend(loc='upper right', fontsize=12, title='Legend', title_fontsize='14')
ax.set_xlabel('x', fontsize=14, fontweight='bold', color='blue', family='serif')
ax.set_ylabel('y', fontsize=14, fontweight='bold', color='blue', family='serif')
ax.set_title('Plot with Custom Legends and Labels', fontsize=16, fontweight='bold', color='red', family='serif')

# Show the plot
plt.show()
