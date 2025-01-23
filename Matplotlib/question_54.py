import matplotlib.pyplot as plt
from bokeh.plotting import figure, show
from bokeh.io import output_notebook
from bokeh.models import HoverTool

# Enable Bokeh output in Jupyter Notebook
output_notebook()

# Create sample data
x = [1, 2, 3, 4, 5]
y = [10, 11, 12, 13, 14]

# Create a Bokeh figure
p = figure(title="Interactive Plot with Bokeh", x_axis_label='X-axis', y_axis_label='Y-axis')

# Add a line renderer with legend and line thickness
p.line(x, y, legend_label="Line", line_width=2)

# Add hover tool
hover = HoverTool()
hover.tooltips = [("X", "@x"), ("Y", "@y")]
p.add_tools(hover)

# Show the plot
show(p)
