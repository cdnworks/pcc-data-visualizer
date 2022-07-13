import pygal

from die import Die

d_six = Die()

#Make some rolls, store results in a list
results = []
for roll in range(1000):
    result = d_six.roll()
    results.append(result)

# Collect frequencies of each roll result
frequencies = []
for value in range(1, d_six.num_sides + 1):
    frequency = results.count(value)
    frequencies.append(frequency)

# Visualize the results
hist = pygal.Bar()

hist.title = "1000 Rolls of a D6"
hist.x_labels = ['1', '2', '3', '4', '5', '6']
hist.x_title = "Result"
hist.y_title = "Frequency"

hist.add('D6', frequencies)
hist.render_to_file('die_visual.svg')