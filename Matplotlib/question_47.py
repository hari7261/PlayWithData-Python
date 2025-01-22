import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Generate a random dataset
data = np.random.randn(1000)

# Plot a histogram
plt.figure(figsize=(10, 6))
sns.histplot(data, bins=30, kde=True, edgecolor='black')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Histogram and KDE Plot of Random Dataset')
plt.show()
