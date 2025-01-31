import numpy as np
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

# Generate random data
np.random.seed(0)
X = np.random.randn(100, 2)

# Create a PCA model
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X)

# Plot the results
plt.scatter(X_pca[:, 0], X_pca[:, 1])
plt.xlabel("Principal Component 1")
plt.ylabel("Principal Component 2")
plt.title("Principal Component Analysis (PCA)")
plt.show()
