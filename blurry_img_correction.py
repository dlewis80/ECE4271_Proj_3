import processing as prc
import dippykit as dip
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image, ImageEnhance

orig_img = dip.im_read('Data_students/blurryImage.png')
rec_img = prc.bilateral_filter(orig_img) # dip.image_io.float_to_im()
dip.im_write(rec_img,'Data_students/blurryImageCorrection.png')

fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(8, 5), sharex=True, sharey=True)

ax[0].imshow(orig_img)
ax[0].axis('off')
ax[0].set_title('Data')

ax[1].imshow(rec_img)
ax[1].axis('off')
ax[1].set_title('Self tuned restoration')

fig.tight_layout()

plt.show()