import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# This code creates a simple linear regression model using sklearn

# Generate some data
np.random.seed(0)
X = 2 * np.random.rand(100, 1)
y = 4 + 3 * X + np.random.randn(100, 1)

# Create a linear regression model
model = LinearRegression()  # LinearRegression creates a linear regression model
model.fit(X, y)

# Make predictions
X_new = np.array([[0], [2]])
y_predict = model.predict(X_new)

# Plot the results
plt.scatter(X, y)  # plt.scatter creates a scatter plot
plt.plot(X_new, y_predict, "r-")
plt.xlabel("X")
plt.ylabel("y")
plt.title("Linear Regression Model")
plt.show()
