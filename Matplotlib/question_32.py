import matplotlib.pyplot as plt

x = ['A', 'B', 'C', 'D', 'E']
y = [10, 20, 30, 40, 50]

plt.plot(x, y)
plt.xlabel('Categories')
plt.ylabel('Values')
plt.title('Line Plot with Rotated X-axis Labels')
plt.xticks(rotation=45)
plt.show()
