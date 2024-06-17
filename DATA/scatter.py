import matplotlib.pyplot as plt
from matplotlib.ticker import ScalarFormatter

# Generate x values from 1 to 1000
x_values = range(1, 1001)
# Generate y values as the square of each x value
y_values = [x**2 for x in x_values]

# Use the 'seaborn-v0_8' style for the plot
plt.style.use('seaborn-v0_8')

# Create a figure and axis object
fig, ax = plt.subplots()
# Create a scatter plot of x and y values with point size of 10, c= color scheme RGB
# ax.scatter(x_values, y_values, s=10, c=(0,1,0))


# create a scatter plot where the large y values are darker blues
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=10)

# Set a title for the chart with a font, size of 24, 
ax.set_title("Square Numbers", fontsize=24)
# Set a label for the horizontal axis with a font size of 14
ax.set_xlabel("Value", fontsize=14)
# Set a label for the vertical axis with a font size of 14
ax.set_ylabel("Square of Value", fontsize=14)

# Use a ScalarFormatter to format the y-axis labels in plain (non-scientific) notation
ax.yaxis.set_major_formatter(ScalarFormatter(useMathText=True))
# Ensure the y-axis labels are shown in plain format
ax.ticklabel_format(style='plain', axis='y')

# Set the axis limits: x-axis from 0 to 1100 and y-axis from 0 to 1100000
ax.axis([0, 1100, 0, 1100000])

# Display the plot
plt.show()

# saves the graph as a PNG, bbox removes any whitespace trim from the file, can't show any then save otherwise the PNG will be blank
plt.savefig('squares_plot.png', bbox_inches='tight')
