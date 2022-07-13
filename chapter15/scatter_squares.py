import matplotlib.pyplot as plotter

x_vals = list(range(1,1001))
y_vals = [x**2 for x in x_vals]


plotter.scatter(x_vals, y_vals, c = y_vals, cmap = plotter.cm.hot,
    edgecolor = 'none', s=40)

# Title, Axes and Tick labels
plotter.title("Square Numbers", fontsize = 24)
plotter.xlabel("Value", fontsize = 14)
plotter.ylabel("Square Value", fontsize = 14)
plotter.tick_params(axis='both', which='major', labelsize = 14)

#Axis range
plotter.axis([0, 1100, 0, 1100000])

plotter.show()