#plot_geotiff.py
#note that georaster has gdal dependencies

# usage:
#plot_geotiff.py inputfile outputfile cmap title
# example:
#plot_geotiff.py inputfile outputfile 'hot_r' "My Greate Title"


import sys
import georaster
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
import numpy as np
from numpy.ma import masked_array
from matplotlib.ticker import FuncFormatter
import matplotlib.ticker as mtick

my_image = georaster.SingleBandRaster(sys.argv[1])
fig, ax = plt.subplots()
masked = np.ma.masked_equal(my_image.r, 0.)
ax.xaxis.set_major_formatter(mtick.FormatStrFormatter('%.1f'))
shw = ax.imshow(masked,extent=my_image.extent,cmap=sys.argv[3],vmin=-15,vmax=40)
plt.colorbar(shw,extend = 'both',format='%.1f',shrink=0.8).minorticks_on()
name=sys.argv[1].split('.')[0]
title_str =  sys.argv[4]#' '.join(elem.capitalize() for elem in name.split('_'))
plt.title(title_str)
plt.show()
fig.savefig(sys.argv[2],bbox_inches='tight',dpi=600)
