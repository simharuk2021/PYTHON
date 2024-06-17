import matplotlib.pyplot as plt

input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]

plt.style.use('seaborn-v0_8')

fig, ax = plt.subplots()
# linewidth = line width of the graph line, input_values means the plot overrides the use of 0 on the vertical axis
ax.plot(input_values, squares, linewidth=3)
# set a title for the chart
ax.set_title("Square Numbers", fontsize = 24)
# set a label for the horizontal axis
ax.set_xlabel("Value", fontsize = 14)
# set a label for the vertical axis
ax.set_ylabel("Square of Value", fontsize = 14)

ax.tick_params(axis='both', labelsize=14)

plt.show()