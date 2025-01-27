import matplotlib.pyplot as plt
import numpy as np

# This code plots a line graph of y = x^2 for x from 0 to 10

# Create an array of values from 0 to 10
x = np.arange(0, 11)  # np.arange generates values from 0 to 10

# Calculate y values as the square of x values
y = x ** 2

# Plot the graph
plt.plot(x, y)  # plt.plot creates a line graph
plt.xlabel('x')
plt.ylabel('y')
plt.title('Line graph of y = x^2')
plt.show()
