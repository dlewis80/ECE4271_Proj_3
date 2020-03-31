import processing as prc
import metrics as mt
#import anisotropic as ani
import dippykit as dip
import matplotlib.pyplot as plt
import skimage
import exposure
import matlab.engine
import numpy as np

orig_img_1 = dip.im_read('Data_students/ownpic1/ownpic1_01_0.jpg')

img1 = skimage.util.random_noise(orig_img_1,mode='s&p',amount=0.2)
dip.im_write(dip.image_io.float_to_im(img1),'Data_students/ownpic1/ownpic1_07_1.jpg')

img1 = skimage.util.random_noise(orig_img_1,mode='s&p',amount=0.375)
dip.im_write(dip.image_io.float_to_im(img1),'Data_students/ownpic1/ownpic1_07_2.jpg')

img1 = skimage.util.random_noise(orig_img_1,mode='s&p',amount=0.550)
dip.im_write(dip.image_io.float_to_im(img1),'Data_students/ownpic1/ownpic1_07_3.jpg')

img1 = skimage.util.random_noise(orig_img_1,mode='s&p',amount=0.725)
dip.im_write(dip.image_io.float_to_im(img1),'Data_students/ownpic1/ownpic1_07_4.jpg')

img1 = skimage.util.random_noise(orig_img_1,mode='s&p',amount=0.9)
dip.im_write(dip.image_io.float_to_im(img1),'Data_students/ownpic1/ownpic1_07_5.jpg')