import numpy as np
from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt

# This code creates a simple k-nearest neighbors classifier using sklearn

# Generate some data
np.random.seed(0)
X = np.random.randn(100, 2)
y = (X[:, 0] + X[:, 1] > 0).astype(int)

# Create a k-nearest neighbors classifier
model = KNeighborsClassifier(n_neighbors=3)  # KNeighborsClassifier creates a k-nearest neighbors classifier
model.fit(X, y)

# Make predictions
X_new = np.array([[0, 0], [1, 1]])
y_predict = model.predict(X_new)

# Plot the results
plt.scatter(X[:, 0], X[:, 1], c=y, cmap='viridis')  # plt.scatter creates a scatter plot
plt.scatter(X_new[:, 0], X_new[:, 1], c=y_predict, cmap='coolwarm', marker='x')
plt.xlabel("Feature 1")
plt.ylabel("Feature 2")
plt.title("K-Nearest Neighbors Classifier")
plt.show()
