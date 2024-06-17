import csv
import matplotlib.pyplot as plt
from datetime import datetime

filename = 'data/sitka_weather_07-2021_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row=next(reader)
    # This code extracts the index number for each column so that the columns with the data can be
    # for index, column_header in enumerate(header_row):
    #     print(index, column_header)
    
# Get high temperatures from this file
    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%d/%m/%Y')
        high = int(row[5])
        low = int(row[6])
        dates.append(current_date)
        highs.append(high)
        lows.append(low)
    print(highs)

#plot the high temperatures
plt.style.use('seaborn-v0_8-dark-palette')
fix, ax = plt.subplots()
#alpha shades the area between
ax.plot(dates, highs, c='red', alpha = 0.5)
ax.plot(dates, lows, c='blue', alpha = 0.5)
ax.fill_between(dates, highs, lows, facecolor = 'blue', alpha=0.1)

#format plot
ax.set_title("Daily high and low temperatures, July 2021", fontsize=24)
ax.set_xlabel('', fontsize = 16)
fix.autofmt_xdate()
ax.set_ylabel("Temperature (F)", fontsize = 16)
ax.tick_params(axis='both', which='major', labelsize=16)

plt.show()