import matplotlib.pyplot as plt

x = [0, 1, 2, 3, 4, 5]
y = [0, 1, 4, 9, 16, 25]

plt.plot(x, y)
plt.title('Plot with Text Annotations')

# Add text annotations
for i in range(len(x)):
    plt.text(x[i], y[i], f'({x[i]}, {y[i]})')

plt.show()
