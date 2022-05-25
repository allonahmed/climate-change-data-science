#Application to compare and analyze weather patters from April of 1972 and April 2022
#import plotting functions to visually analyze our data
import matplotlib.pyplot as plt
import numpy as np

import math
from File import FileData
from calculations import correlation_coefficient, mean, standard_deviation

#create our two objects that contain the weather data of both years
weather1922 = FileData('average_april_1922_weather.csv');
weather1972 = FileData('average_april_1972_weather.csv');
weather2022 = FileData('average_april_2022_weather.csv');


#adjusts the font-size of the plot labels for UI purposes 
fig, ax = plt.subplots(3)
fig.suptitle('Max temperature for each day in April')

ax[0].xaxis.set_tick_params(labelsize=6)
ax[0].plot(weather1922.dates, weather1922.temperatures)
ax[0].set_title("1922")

ax[1].xaxis.set_tick_params(labelsize=6)
ax[1].plot(weather1972.dates, weather1972.temperatures)
ax[1].set_title("1972")
ax[1].set_ylabel("Temperature (F)")

ax[2].xaxis.set_tick_params(labelsize=6)
ax[2].plot(weather2022.dates, weather2022.temperatures)
ax[2].set_title("2022")
ax[2].set_xlabel("Dates")



print('\n         April Weather\n ------------------------------ \n  1922        1972        2022\n ------------------------------ ')
for i, j, k in zip(weather1922.temperatures, weather1972.temperatures, weather2022.temperatures):
    print('| ' + str(i) + '        ' + str(j) + '        ' + str(k) + ' |' )
print(' ------------------------------ \n')
print('------------------------------------------------------------------ ')
print("Average temperature for April 1922: ", str(mean(weather1922.temperatures)) + "°")
print('------------------------------------------------------------------ ')
print("Average temperature for April 1972: ", str(mean(weather1972.temperatures)) + "°")
print('------------------------------------------------------------------ ')
print("Average temperature for April 2022: ", str(mean(weather2022.temperatures)) + "°")
print('------------------------------------------------------------------ ')
print("Difference in average temperature for April 1922 and 2022: ", str(round((mean(weather2022.temperatures) - mean(weather1922.temperatures)),3)) + "°")
print('------------------------------------------------------------------ ')
print("Difference in average temperature for April 1972 and 2022: ", str(round((mean(weather2022.temperatures) - mean(weather1972.temperatures)),3)) + "°")
print('------------------------------------------------------------------ ')
print('Standard Deviation for temperature of April 1922: ', standard_deviation(weather1922.temperatures))
print('------------------------------------------------------------------ ')
print('Standard Deviation for temperature of April 1972: ', standard_deviation(weather1972.temperatures))
print('------------------------------------------------------------------ ')
print('Standard Deviation for temperature of April 2022: ', standard_deviation(weather2022.temperatures))
print('------------------------------------------------------------------ ')
print("Correlation Coefficient of April 1922 and 2022: ", correlation_coefficient(weather1922.temperatures, weather2022.temperatures))
print('------------------------------------------------------------------ ')
print("Correlation Coefficient of April 1972 and 2022: ", correlation_coefficient(weather1972.temperatures, weather2022.temperatures))
plt.show()







