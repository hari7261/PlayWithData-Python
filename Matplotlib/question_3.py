import matplotlib.pyplot as plt

x = ['A', 'B', 'C']
y = [10, 20, 30]

plt.barh(x, y)
plt.xlabel('Categories')
plt.ylabel('Values')
plt.title('Horizontal Bar Chart')
plt.show()
