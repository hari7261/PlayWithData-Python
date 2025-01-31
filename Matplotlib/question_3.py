import matplotlib.pyplot as plt

# This code creates a horizontal bar chart for given categories and values
x = ['A', 'B', 'C']
y = [10, 20, 30]

# Create a horizontal bar chart
plt.barh(x, y)

# Set the label for the x-axis
plt.xlabel('Categories')

# Set the label for the y-axis
plt.ylabel('Values')

# Set the title of the plot
plt.title('Horizontal Bar Chart')

# Display the plot
plt.show()
