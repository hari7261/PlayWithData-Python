import matplotlib.pyplot as plt

# This code creates a bar chart for given categories and values
x = ['A', 'B', 'C']
y = [10, 20, 30]

# Create a bar chart
plt.bar(x, y)

# Set the label for the x-axis
plt.xlabel('Categories')

# Set the label for the y-axis
plt.ylabel('Values')

# Set the title of the plot
plt.title('Bar Chart')

# Display the plot
plt.show()
