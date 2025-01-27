import matplotlib.pyplot as plt

# This code plots two lines on the same graph and adds a legend

x = [0, 1, 2, 3, 4, 5]
y1 = [0, 1, 4, 9, 16, 25]
y2 = [0, 1, 8, 27, 64, 125]

plt.plot(x, y1, label='y = x^2')  # plt.plot creates a line graph
plt.plot(x, y2, label='y = x^3')  # plt.plot creates a line graph
plt.xlabel('X-axis Label')
plt.ylabel('Y-axis Label')
plt.title('Plot with Legend')
plt.legend()  # plt.legend adds a legend to the plot
plt.show()
