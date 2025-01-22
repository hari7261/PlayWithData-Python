import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0, 11)
y = x ** 2

plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Line graph of y = x^2')
plt.show()
