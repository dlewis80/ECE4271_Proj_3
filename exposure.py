import numpy as np
import metrics as mt
import skimage

def histogram_equalization(img):
    im = img.flatten()
    (h,_) = mt.histogram(im)
    T = np.around((255/im.size)*np.cumsum(h))
    for i in range(im.size):
        im[i] = T[im[i]]

    return np.reshape(im,(img.shape))

def intensity_rescalation(img):
    return skimage.exposure.rescale_intensity(img)

    
