import numpy as np
from sklearn.ensemble import RandomForestClassifier
import matplotlib.pyplot as plt

# Generate random data
np.random.seed(0)
X = np.random.randn(100, 2)
y = (X[:, 0] + X[:, 1] > 0).astype(int)

# Create a RandomForestClassifier model
model = RandomForestClassifier()
model.fit(X, y)

# Make predictions
X_new = np.array([[0, 0], [1, 1]])
y_predict = model.predict(X_new)

# Plot the results
plt.scatter(X[:, 0], X[:, 1], c=y, cmap='viridis')
plt.scatter(X_new[:, 0], X_new[:, 1], c=y_predict, cmap='coolwarm', marker='x')
plt.xlabel("Feature 1")
plt.ylabel("Feature 2")
plt.title("Random Forest Classifier")
plt.show()
