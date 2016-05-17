
# Importing matplotlib and elements
from matplotlib import pyplot as plt
# Providing Rough data
Years = [2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016]
EarthQuakes = [10, 13, 8, 16, 23, 22, 24, 7]
plt.scatter(Years, EarthQuakes, color='Red')
# Title
plt.title('Earthquakes Per Year')
# Labels
plt.xlabel('Years')
plt.ylabel('Occurrence / Year')
# Ticks @ x-axis (Years)
plt.xticks([i for i in Years], Years)
plt.show()
