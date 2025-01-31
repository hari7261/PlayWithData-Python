import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# Generate random data
np.random.seed(0)
X = np.random.randn(100, 2)

# Create a KMeans model
model = KMeans(n_clusters=3)
model.fit(X)

# Make predictions
y_predict = model.predict(X)

# Plot the results
plt.scatter(X[:, 0], X[:, 1], c=y_predict, cmap='viridis')
plt.xlabel("Feature 1")
plt.ylabel("Feature 2")
plt.title("K-Means Clustering")
plt.show()
