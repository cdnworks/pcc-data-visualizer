# TIY Problem pg. 240
# Plot the first 5000 cubic integers, and apply a color map to the plot

import matplotlib.pyplot as plotter

x_vals = list(range(1, 5001))
y_vals = [x**3 for x in x_vals]

plotter.scatter(x_vals, y_vals, c = y_vals, cmap = plotter.cm.spring)

plotter.title("Cubic Numbers", fontsize = 24)
plotter.xlabel("Value", fontsize = 14)
plotter.ylabel("Cubed Value", fontsize = 14)

plotter.show()

