import csv
from datetime import datetime
from multiprocessing.sharedctypes import Value

from matplotlib import pyplot as plotter

def get_data_date(filename):
    with open(filename) as f:
        reader = csv.reader(f)
        header_row = next(reader)

        dates = []
        for row in reader:
            try:
                current_date = datetime.strptime(row[0], '%Y-%m-%d')
            except ValueError:
                print(current_date, 'Missing data')
            else:
                dates.append(current_date)
        return dates

def get_high_temp(filename):
    with open(filename) as f:
        reader = csv.reader(f)
        header_row = next(reader)

        high_temps = []
        for row in reader:
            try:
                current_date = datetime.strptime(row[0], '%Y-%m-%d')
                high = int(row[1])
            except ValueError:
                print(current_date, 'Missing data')
                # This is a terrible solution irl but this is to get
                # the example data into the same length
                high_temps.append(0)
            else:
                high_temps.append(high)
        return high_temps
        
def get_low_temp(filename):
    with open(filename) as f:
        reader = csv.reader(f)
        header_row = next(reader)

        low_temps = []
        for row in reader:
            try:
                current_date = datetime.strptime(row[0], '%Y-%m-%d')
                low = int(row[3])
            except ValueError:
                print(current_date, 'Missing data')
                # This is a terrible solution irl but this is to get
                # the example data into the same length
                low_temps.append(0)
            else:
                low_temps.append(low)
        return low_temps

# Get high temperatures from the file
deathvalley_data = 'death_valley_2014.csv'
sitkaalaska_data = 'sitka_weather_2014.csv'

dd_dates = get_data_date(deathvalley_data)
dd_highs = get_high_temp(deathvalley_data)
dd_lows = get_low_temp(deathvalley_data)

sd_dates = get_data_date(sitkaalaska_data)
sd_highs = get_high_temp(sitkaalaska_data)
sd_lows = get_low_temp(sitkaalaska_data)





# Plot data
fig = plotter.figure(dpi=128, figsize=(10,6))
plotter.plot(dd_dates, dd_highs, c='red')
plotter.plot(sd_dates, sd_highs, c='red', alpha = 0.25)

plotter.plot(dd_dates, dd_lows, c='blue')
plotter.plot(sd_dates, sd_lows, c='blue', alpha = 0.25)

# Format plot
plotter.title("Daily High and Low Temperatures, 2014\nDeath Valley and Sitka", 
    fontsize = 20)
plotter.xlabel("", fontsize = 16)
fig.autofmt_xdate()
plotter.ylabel("Temperature (F)", fontsize = 16)
plotter.tick_params(axis='both', which='major', labelsize = 16)

plotter.show()