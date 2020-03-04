import dippykit as dip
import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
from skimage.metrics import structural_similarity as ssim
from PIL import Image
import PIL

f, ax = plt.subplots(1,2)
im_og = dip.im_read('/Users/omarwali/ece4271/project3/Data_students/wiseonRocks_square/wiseonRocks_square_01_0.png')
im_in = dip.im_read('/Users/omarwali/ece4271/project3/Data_students/wiseonRocks_square/wiseonRocks_square_02_5.jpg')

r = im_og.shape[0]
c = im_og.shape[1]

resized_image = cv.resize(im_in, (c,r), interpolation=cv.INTER_CUBIC)
dip.im_write(resized_image, 'wiseonRocks_square_02_5_rs.jpg', 95)

ax[0].imshow(im_og)
ax[0].set_title('Original Image')
ax[0].axis('off')

ax[1].imshow(resized_image)
ax[1].set_title('Resized Image')
ax[1].axis('off')

plt.show()

PSNR = dip.PSNR(im_og, resized_image, 255)

SSIM = ssim(resized_image, im_og, data_range=im_og.max() - im_og.min(), multichannel=True)

print('SSIM: ')
print(SSIM)
print('\n')

print('PSNR: ')
print(PSNR)


