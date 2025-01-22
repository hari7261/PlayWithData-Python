import matplotlib.pyplot as plt

# Data for plotting
categories = ['A', 'B', 'C']
values1 = [10, 20, 30]
values2 = [5, 15, 25]

# Create a stacked bar chart
plt.bar(categories, values1, label='Value 1')
plt.bar(categories, values2, bottom=values1, label='Value 2')

# Add labels and title
plt.xlabel('Categories')
plt.ylabel('Values')
plt.title('Stacked Bar Chart')
plt.legend()

# Show the plot
plt.show()
