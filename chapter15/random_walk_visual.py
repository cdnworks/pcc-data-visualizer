# TIY Problem pg. 246
# Modify this .py file by replacing the scatter() with plot()
# Pass in the same rw.x_values and y_values, but include a linewidth argument
# Use 5000 points

import matplotlib.pyplot as plotter

from random_walk import RandomWalk

# Make new walks as long as the program is active
while True:
    # make a new random walk and plot the points
    rw = RandomWalk(5000)
    rw.fill_walk()

    # Set the size of the plotting window
    plotter.figure(figsize=(10,6))

    point_numbers = list(range(rw.num_points))
    plotter.plot(rw.x_values, rw.y_values, color = 'yellow', linewidth = 1)

    # Emphasize the first and last points
    plotter.scatter(0,0, c='green', edgecolors = 'none', s = 100)
    plotter.scatter(rw.x_values[-1], rw.y_values[-1], c = 'red', 
        edgecolors = 'none', s = 100)

    # Remove axes
    plotter.axis('off')
    
    plotter.show()

    keep_running = input("Make a new walk? (y/n):")
    if keep_running == 'n':
        break