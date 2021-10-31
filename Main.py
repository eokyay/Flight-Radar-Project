from mpl_toolkits.basemap import Basemap

import numpy as np
import matplotlib.pyplot as plt

m = Basemap(llcrnrlon=-80.3611,llcrnrlat=42.907,urcrnrlon=-78.5674,urcrnrlat=44.1373,
            resolution='f',projection='tmerc',lon_0=-79.347015,lat_0=43.651070)
#m.drawcoastlines()
m.fillcontinents(color='coral',lake_color='aqua')
m.drawcounties(linewidth=0.1, linestyle='solid', color='k', antialiased=1, facecolor='none', ax=None, zorder=None, drawbounds=True)
# draw parallels and meridians.
#m.drawparallels(np.arange(-90.,91.,30.))
#m.drawmeridians(np.arange(-180.,181.,60.))
#m.drawmapboundary(fill_color='aqua')
plt.title("Mercator Projection")
plt.show()

 #-80.3611	42.907	-78.5674	44.1373