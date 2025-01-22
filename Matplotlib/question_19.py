import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Generate random data
data = np.random.normal(size=100)

# Create a violin plot
sns.violinplot(data=data)

# Add title and labels
plt.title('Violin Plot of Random Data')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

# Show the plot
plt.show()
