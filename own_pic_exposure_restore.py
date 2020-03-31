import dippykit as dip
import skimage
import exposure
import matplotlib.pyplot as plt
import numpy as np
import metrics as mt
from PIL import ImageEnhance,Image

name = 'ownPic_3'
addit = '_03_5'

under = True
over = False

o_img = dip.im_read('own_pics/'+name+'.jpg')

enhancer = ImageEnhance.Brightness(Image.fromarray(o_img))
paths =[]
titles=[]

if under:
    #Underexposing image
    u_img = np.array(enhancer.enhance(0.08))
    #u_img = dip.im_read('own_pics/ownPic_3_03_2.jpg')
    rec_1 = exposure.histogram_equalization(u_img)
    paths.append('underexposure_restored/'+name+addit+'_restored.bmp')
    titles.append('Underexposed Image')
    dip.im_write(u_img,'underexposure_restored/'+name+addit+'_underexposed.bmp')
    dip.im_write(rec_1,paths[0])
    h_under = mt.histogram(u_img)
    h_under_rec = mt.histogram(rec_1)

    plt.figure()
    plt.subplot(2,1,1)
    plt.stem(h_under[1],h_under[0],use_line_collection=True)
    plt.title('Underexposed Image')
    plt.subplot(2,1,2)
    plt.stem(h_under_rec[1],h_under_rec[0],use_line_collection=True)
    plt.title('Enhanced Image')
    fig_size = plt.gcf().get_size_inches() 
    plt.gcf().set_size_inches(2 * fig_size) 
    plt.savefig('underexposure_restored/'+name+addit+'_hist.pdf')

    plt.figure()
    plt.subplot(1,2,1)
    plt.imshow(u_img)
    plt.axis('off')
    plt.title('Underexposed Image')
    plt.subplot(1,2,2)
    plt.imshow(rec_1)
    plt.axis('off')
    plt.title('Enhanced Image')


if over:
    #Overexposing image
    o_img = np.array(enhancer.enhance(3.5))
    #o_img = dip.im_read('own_pics/ownPic_3_04_2.jpg')
    rec_2 = exposure.histogram_equalization(o_img)
    paths.append('overexposure_restored/'+name+addit+'_restored.bmp')
    titles.append('Overexposed Image')
    dip.im_write(o_img,'overexposure_restored/'+name+addit+'_overexposed.bmp')
    dip.im_write(rec_2,paths[0])
    h_over = mt.histogram(o_img)
    h_over_rec = mt.histogram(rec_2)
    plt.figure()
    plt.subplot(2,1,1)
    plt.stem(h_over[1],h_over[0],use_line_collection=True)
    plt.title('Overexposed Image')
    plt.subplot(2,1,2)
    plt.stem(h_over_rec[1],h_over_rec[0],use_line_collection=True)
    plt.title('Enhanced Image')
    fig_size = plt.gcf().get_size_inches() 
    plt.gcf().set_size_inches(2 * fig_size) 
    plt.savefig('overexposure_restored/'+name+addit+'_hist.pdf')

    plt.figure()
    plt.subplot(1,2,1)
    plt.imshow(o_img)
    plt.axis('off')
    plt.title('Overexposed Image')
    plt.subplot(1,2,2)
    plt.imshow(rec_2)
    plt.axis('off')
    plt.title('Enhanced Image')



mt.compute_stats(paths,titles,'own_pics/'+name+'.jpg',False)

plt.show()

