# Matplotlib Questions

This folder contains 100 questions specifically focused on Matplotlib for data visualization. Each question has a corresponding file with clean and neat code.

## Questions

### Basic Plots
1. [Plot a line graph of `y = x^2` for `x` from 0 to 10](question_1.py)
2. [Create a bar chart for the following data: `x = ['A', 'B', 'C']`, `y = [10, 20, 30]`](question_2.py)
3. [Plot a horizontal bar chart for the same data](question_3.py)
4. [Create a scatter plot for two random datasets](question_4.py)
5. [Plot a histogram of a random dataset](question_5.py)

### Customization
6. [Add a title to a plot](question_6.py)
7. [Add labels to the x-axis and y-axis of a plot](question_7.py)
8. [Change the color of a line plot](question_8.py)
9. [Change the line style of a plot (e.g., dashed, dotted)](question_9.py)
10. [Add a legend to a plot](question_10.py)

### Multiple Plots
11. [Plot multiple lines on the same graph](question_11.py)
12. [Create subplots with 2 rows and 2 columns](question_12.py)
13. [Plot a line graph and a scatter plot on the same figure](question_13.py)
14. [Create a figure with multiple subplots and share the x-axis](question_14.py)
15. [Create a figure with multiple subplots and share the y-axis](question_15.py)

### Advanced Plots
16. [Create a stacked bar chart](question_16.py)
17. [Plot a pie chart for the following data: `labels = ['A', 'B', 'C']`, `sizes = [30, 40, 30]`](question_17.py)
18. [Create a box plot for a dataset](question_18.py)
19. [Plot a violin plot for a dataset](question_19.py)
20. [Create a heatmap for a correlation matrix](question_20.py)

### Annotations and Text
21. [Add text annotations to a plot](question_21.py)
22. [Add arrows to a plot](question_22.py)
23. [Highlight specific points on a scatter plot](question_23.py)
24. [Add a grid to a plot](question_24.py)
25. [Add a background color to a plot](question_25.py)

### Saving and Exporting
26. [Save a plot as a PNG file](question_26.py)
27. [Save a plot as a PDF file](question_27.py)
28. [Save a plot with a transparent background](question_28.py)
29. [Adjust the DPI (dots per inch) of a saved plot](question_29.py)
30. [Save a plot with a custom size](question_30.py)

### Advanced Customization
31. [Change the font size of the title and labels](question_31.py)
32. [Rotate the x-axis labels](question_32.py)
33. [Set the limits of the x-axis and y-axis](question_33.py)
34. [Add a secondary y-axis to a plot](question_34.py)
35. [Create a plot with a logarithmic scale on the x-axis](question_35.py)

### Specialized Plots
36. [Create a polar plot](question_36.py)
37. [Plot a 3D surface plot](question_37.py)
38. [Create a contour plot](question_38.py)
39. [Plot a quiver plot (vector field)](question_39.py)
40. [Create a streamplot](question_40.py)

### Interactive Plots
41. [Add hover effects to a plot using `mplcursors`](question_41.py)
42. [Create an interactive plot using `mpld3`](question_42.py)
43. [Add sliders to a plot using `matplotlib.widgets`](question_43.py)
44. [Create an animated plot](question_44.py)
45. [Add buttons to control a plot](question_45.py)

### Real-World Applications
46. [Plot stock price data over time](question_46.py)
47. [Visualize the distribution of a dataset using a histogram and KDE plot](question_47.py)
48. [Create a dashboard with multiple plots for a dataset](question_48.py)
49. [Plot geographic data on a map using `Basemap`](question_49.py)
50. [Create a custom visualization for a machine learning model's performance](question_50.py)

### Advanced and Modern Plots
51. [Create an interactive plot using Plotly](question_51.py)
52. [Create a real-time data plot using Matplotlib](question_52.py)
53. [Create an advanced customized plot with Matplotlib](question_53.py)
54. [Integrate Matplotlib with Bokeh for interactive plots](question_54.py)
55. [Create a plot with advanced annotations and text](question_55.py)
56. [Create a plot with multiple subplots and shared axes](question_56.py)
57. [Create a plot with custom color maps](question_57.py)
58. [Create a plot with custom markers and line styles](question_58.py)
59. [Create a plot with custom fonts and text properties](question_59.py)
60. [Create a plot with custom legends and labels](question_60.py)

## GitHub Actions Workflow

This repository includes a GitHub Actions workflow to automate the process of committing code changes. The workflow is triggered every minute and runs a script that makes 25 commits to the repository.

### Automation Script

The automation script, `commit_script.sh`, creates a temporary file, makes changes to it, and commits those changes 25 times. This ensures that the repository is regularly updated with new commits.
