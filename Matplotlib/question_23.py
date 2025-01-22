import matplotlib.pyplot as plt

# Generate random data
x = [1, 2, 3, 4, 5]
y = [10, 20, 25, 30, 40]

# Create a scatter plot
plt.scatter(x, y)

# Highlight specific points
highlight_x = [2, 4]
highlight_y = [20, 30]
plt.scatter(highlight_x, highlight_y, color='red')

plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Scatter Plot with Highlighted Points')
plt.show()
