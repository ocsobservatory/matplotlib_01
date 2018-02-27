#http://matplotlib.org/1.3.1/users/image_tutorial.html


import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np


import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

img = mpimg.imread('01.tif')
imgplot = plt.imshow(img)
plt.show()


lum_img = img[:,:,0]
plt.hist(lum_img.flatten(), 256, range=(0.0,1.0), fc='black', ec='black')
plt.show()


lum_img = img[:,:,0]
plt.imshow(lum_img)
plt.show()

lum_img = img[:,:,0]
imgplot = plt.imshow(lum_img)
imgplot.set_cmap('hot')
plt.show()


lum_img = img[:,:,0]
imgplot = plt.imshow(lum_img)
#imgplot.set_cmap('spectral')
#imgplot.set_cmap('spectral_r')
#imgplot.set_cmap('nipy_spectral_r')
imgplot.set_cmap('nipy_spectral')
plt.show()


lum_img = img[:,:,0]
imgplot = plt.imshow(lum_img)
#imgplot.set_cmap('spectral')
#imgplot.set_cmap('spectral_r')
#imgplot.set_cmap('nipy_spectral_r')
imgplot.set_cmap('nipy_spectral')
plt.colorbar()
plt.show()


























