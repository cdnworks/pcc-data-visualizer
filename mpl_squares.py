import matplotlib.pyplot as plotter

squares = []
for i in range(1,11):
    squares.append(i ** 2)


plotter.plot((range(1,11)),squares, linewidth = 5)

# Title and label axes
plotter.title("Square Numbers", fontsize = 24)
plotter.xlabel("Value", fontsize = 14)
plotter.ylabel("Squared Value", fontsize = 14)

# Tick label size
plotter.tick_params(axis='both', labelsize = 14)


plotter.show()
