import plotly.graph_objects as go

# Create sample data
x = [1, 2, 3, 4, 5]
y = [10, 11, 12, 13, 14]

# Create a scatter plot
fig = go.Figure(data=go.Scatter(x=x, y=y, mode='markers'))

# Add title and labels
fig.update_layout(title='Interactive Scatter Plot using Plotly',
                  xaxis_title='X-axis',
                  yaxis_title='Y-axis')

# Show the plot
fig.show()
