import pygal

from die import Die

# Create two dice
die_1 = Die()
die_2 = Die(10)

#Make some rolls, store results in a list
results = []
for roll in range(50000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

# Collect frequencies of each roll result
frequencies = []
max_result = die_1.num_sides + die_2.num_sides

for value in range(2, max_result + 1):
    frequency = results.count(value)
    frequencies.append(frequency)

# Visualize the results
hist = pygal.Bar()

hist.title = "50000 Rolls of 1D6 + 1D10"
hist.x_labels = [x for x in range(2, 17)]
hist.x_title = "Result"
hist.y_title = "Frequency"

hist.add('D6 + D10', frequencies)
hist.render_to_file('dice_visual.svg')