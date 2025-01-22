import matplotlib.pyplot as plt

x = [0, 1, 2, 3, 4, 5]
y1 = [0, 1, 4, 9, 16, 25]
y2 = [0, 1, 8, 27, 64, 125]

plt.plot(x, y1, label='y = x^2')
plt.plot(x, y2, label='y = x^3')
plt.xlabel('X-axis Label')
plt.ylabel('Y-axis Label')
plt.title('Multiple Lines on the Same Graph')
plt.legend()
plt.show()
