import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap

# Create a map using Basemap
map = Basemap(projection='merc', llcrnrlat=-60, urcrnrlat=90, llcrnrlon=-180, urcrnrlon=180, resolution='c')

# Draw coastlines and countries
map.drawcoastlines()
map.drawcountries()

# Plot some example data (latitude and longitude)
lats = [37.7749, 51.5074, -33.8688]
lons = [-122.4194, -0.1278, 151.2093]
map.scatter(lons, lats, latlon=True, marker='o', color='r')

# Add title
plt.title('Geographic Data on a Map using Basemap')

# Show the plot
plt.show()
