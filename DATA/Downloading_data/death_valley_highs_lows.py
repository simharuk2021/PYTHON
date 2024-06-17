import csv
import matplotlib.pyplot as plt
from datetime import datetime

filename = 'data/death_valley_2021_simple.csv'
with open (filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    for index, column_header in enumerate(header_row):
        print(index, column_header)
            
        dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        # The exception handling allows for the chart to still be prodiced but for any missing data to be logged 
        try:
            high = int(row[3])
            low = int(row[4])
        except ValueError:
            print(f"Missing data for {current_date}")
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)

#plot the high temperatures
plt.style.use('seaborn-v0_8-dark-palette')
fix, ax = plt.subplots()
#alpha shades the area between
ax.plot(dates, highs, c='red', alpha = 0.5)
ax.plot(dates, lows, c='blue', alpha = 0.5)
ax.fill_between(dates, highs, lows, facecolor = 'blue', alpha=0.1)

#format plot
ax.set_title("Daily high and low temperatures, 2021", fontsize=24)
ax.set_xlabel('', fontsize = 16)
fix.autofmt_xdate()
ax.set_ylabel("Temperature (F)", fontsize = 16)
ax.tick_params(axis='both', which='major', labelsize=16)

plt.show()