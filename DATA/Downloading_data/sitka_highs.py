import csv
import matplotlib.pyplot as plt
from datetime import datetime

filename = 'data/sitka_weather_07-2021_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row=next(reader)
    
# Get high temperatures from this file
    dates, highs = [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%d/%m/%Y')
        high = int(row[5])
        dates.append(current_date)
        highs.append(high)
    print(highs)

#plot the high temperatures
plt.style.use('seaborn-v0_8-dark-palette')
fix, ax = plt.subplots()
ax.plot(dates, highs, c='red')

#format plot
ax.set_title("Daily high temperatures, July 2021", fontsize=24)
ax.set_xlabel('', fontsize = 16)
fix.autofmt_xdate()
ax.set_ylabel("Temperature (F)", fontsize = 16)
ax.tick_params(axis='both', which='major', labelsize=16)

plt.show()