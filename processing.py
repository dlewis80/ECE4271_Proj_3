import cv2 as cv
import skimage as ski

def bilateral_filter(img):
    return cv.bilateralFilter(img, 100, 100, 100) #25 75/150 25

def gaussian_filter(img):
    return cv.GaussianBlur(img, (25, 25), 0) # 5

def wt_bayes(img):
    return ski.restoration.denoise_wavelet(img, multichannel=True, convert2ycbcr=True, wavelet='db2', method='BayesShrink', mode='hard', rescale_sigma=True) # sigma=50