import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Generate a random dataset
data = np.random.randn(100, 5)

# Compute the correlation matrix
corr_matrix = np.corrcoef(data, rowvar=False)

# Create a heatmap
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm')

# Add title and labels
plt.title('Heatmap of Correlation Matrix')
plt.xlabel('Features')
plt.ylabel('Features')

# Show the plot
plt.show()
