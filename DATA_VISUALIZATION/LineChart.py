# Line Chart
# Importing matplotlib and elements
from matplotlib import pyplot as plt
# Providing Rough data
Years = [2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016]
EarthQuakes = [10, 13, 8, 16, 23, 22, 24, 7]
# Creating a Line Chart
# Years on x-axis and EarthQuakes on y
plt.plot(Years, EarthQuakes, color='red', marker='o', linestyle='solid')
# Title
plt.title('Earthquakes Per Year')
# Labels
plt.xlabel('Years')
plt.ylabel('Occurance / Year')
plt.show()
