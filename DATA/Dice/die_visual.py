from die import Die
from plotly.graph_objs import Bar, Layout
from plotly import offline

# Create two dice
die = Die()  # First die
die_2 = Die()  # Second die

# Roll the dice 1000 times and store the results in a list
results = []
for roll_num in range(1000):
    result = die.roll() + die_2.roll()  # Sum the result of rolling both dice
    results.append(result)  # Append the result to the list
print(results)  # Print all results

# Analyze the results to determine the frequency of each possible outcome
frequencies = []
max_result = die.num_sides + die_2.num_sides  # The maximum possible result (12 for two 6-sided dice)
for value in range(2, max_result + 1):  # Possible results range from 2 to 12
    frequency = results.count(value)  # Count how many times each result occurred
    frequencies.append(frequency)  # Append the frequency to the list
print(frequencies)  # Print frequencies of each possible result

# Visualize the results using a bar chart
x_values = list(range(2, max_result + 1))  # X-axis values (possible results)
data = [Bar(x=x_values, y=frequencies)]  # Bar chart data

# Configuration for the x-axis and y-axis
x_axis_config = {'title': 'Result', 'dtick': 1}  # X-axis: label and tick interval
y_axis_config = {'title': 'Frequency of Result'}  # Y-axis: label

# Layout configuration for the plot
my_layout = Layout(title='Results of Rolling Two D6 1000 Times', 
    xaxis=x_axis_config, yaxis=y_axis_config)

# Generate the plot and save it as an HTML file
offline.plot({'data': data, 'layout': my_layout}, filename='d6_d6.html')
