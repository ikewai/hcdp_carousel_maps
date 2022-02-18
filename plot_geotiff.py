import sys
import georaster
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
import numpy as np
from numpy.ma import masked_array


my_image = georaster.SingleBandRaster(sys.argv[1])
fig, ax = plt.subplots()
masked = np.ma.masked_equal(my_image.r, 0.)

shw = ax.imshow(masked,extent=my_image.extent,cmap='hot_r')
plt.colorbar(shw)
name=sys.argv[1].split('.')[0]
title_str =  ' '.join(elem.capitalize() for elem in name.split('_'))
plt.title(title_str)
plt.show()
fig.savefig(sys.argv[1].replace('tif','png'))
