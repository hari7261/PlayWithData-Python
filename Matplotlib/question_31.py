import matplotlib.pyplot as plt

x = [0, 1, 2, 3, 4, 5]
y = [0, 1, 4, 9, 16, 25]

plt.plot(x, y)
plt.title('Plot with Custom Font Sizes', fontsize=16)
plt.xlabel('X-axis Label', fontsize=14)
plt.ylabel('Y-axis Label', fontsize=14)
plt.show()
