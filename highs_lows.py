import csv
from datetime import datetime
from multiprocessing.sharedctypes import Value

from matplotlib import pyplot as plotter

# Get high temperatures from the file
filename = 'death_valley_2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    dates, high_temps, low_temps = [], [], []
    for row in reader:
        try:
            current_date = datetime.strptime(row[0], '%Y-%m-%d')
            high = int(row[1])
            low = int(row[3])
        except ValueError:
            print(current_date, 'Missing data')
        else:
            dates.append(current_date)
            high_temps.append(high)
            low_temps.append(low)


# Plot data
fig = plotter.figure(dpi=128, figsize=(10,6))
plotter.plot(dates, high_temps, c='red', alpha=0.5)
plotter.plot(dates, low_temps, c='blue', alpha=0.5)
plotter.fill_between(dates, high_temps, low_temps, facecolor='blue', alpha=0.1)

# Format plot
plotter.title("Daily High and Low Temperatures, 2014\nDeath Valley", 
    fontsize = 20)
plotter.xlabel("", fontsize = 16)
fig.autofmt_xdate()
plotter.ylabel("Temperature (F)", fontsize = 16)
plotter.tick_params(axis='both', which='major', labelsize = 16)

plotter.show()