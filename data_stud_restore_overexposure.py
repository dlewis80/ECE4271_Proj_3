
import metrics as mt
import dippykit as dip
import matplotlib.pyplot as plt
import skfuzzy as fuzz
import skimage
import exposure
import matlab.engine
import numpy as np


'''
def mu1(x,fh2):
    return np.exp(-((255-x)**2)/(2*fh2))

def mu2(x,a,ex):
    gamma = (10*(ex-0.5))**1.1
    return 0.99*((x-a)/(255-a))**gamma

def restore_overexposure(img):
    img2 = np.copy(img)
    img2 = skimage.img_as_ubyte(skimage.color.rgb2hsv(img2))
    h = skimage.exposure.histogram(img2[:,:,2],normalize=True)
    img2 = img2.astype(np.double)
    ex = (1/h[0].size)*(np.sum(h[0]*h[1])/np.sum(h[0]))
    a =np.floor( h[0].size *(1-ex))

    fh2 = 0.5 * (np.sum(((255-h[1])**4) * h[0]))/(np.sum(((255-h[1])**2) * h[0]))
    for i in range(img2[:,:,2].shape[0]):
        for j in range(img2[:,:,2].shape[1]):
            if (img2[i,j,2] >= a):
                img2[i,j,2] = mu2(img2[i,j,2],a,ex)
            else:
                img2[i,j,2] = mu1(img2[i,j,2],fh2)

    for i in range(img2[:,:,1].shape[0]):
        for j in range(img2[:,:,1].shape[1]):
            img2[i,j,1] = (1/(1+np.exp(-12*(mu1(img2[i,j,1],fh2)-0.5))))* 0.7

    img2[:,:,2] = np.floor(255*img2[:,:,2])
    img2[:,:,1] = np.floor(255*img2[:,:,1])
    img2 = img2.astype(np.uint8)

    return skimage.color.hsv2rgb(img2)
'''
def restore_overexposure(img):
    return exposure.histogram_equalization(img)

if __name__ == "__main__":

    f_basename = ("brussels3","espresso_square","wiseonRocks_square")
    rang1 = (0,1,2)
    rang2 = (1,)
    histograms = True
    stats = True
    show = False

    paths =[]
    titles = []
    for j in rang1:
        paths.clear()
        titles.clear()
        prev_path = "Data_students\\"+f_basename[j]+"\\"+f_basename[j]
        if j == 2:
            orig_path = prev_path + "_01_0.png"
        else:
            orig_path = prev_path + "_01_0.jpg"

        orig_img = dip.im_read(orig_path)
        #orig_img = skimage.img_as_ubyte(skimage.color.rgb2gray(orig_img))
        plt.figure()
        plt.title(f_basename[j] + 'Original Image')
        plt.imshow(orig_img)
        plt.axis("off")
        if histograms:
            orig_hist = mt.histogram(orig_img)
            plt.figure()
            plt.title(f_basename[j] + ' Original Image. Histogram')
            plt.stem(orig_hist[1],orig_hist[0],use_line_collection=True)
            plt.savefig('overexposure_restored\\'+f_basename[j]+"_hist.png")
        

        for i in rang2:
            f = prev_path+"_04_"+str(i)+".jpg"
            img = dip.im_read(f)
            #img = skimage.img_as_ubyte(skimage.color.rgb2gray(img))
            title = f_basename[j] + " overexposure level: "+str(i)
            titles.append(title)
            rec_img = restore_overexposure(img)
             
            if histograms:
                h_rec = mt.histogram(rec_img)
                h = mt.histogram(img)

                plt.figure()
                plt.suptitle(f_basename[j] + ' overexposure level: '+str(i))
                plt.subplot(1,2,1)
                plt.title( 'Image histogram')
                plt.stem(h[1],h[0],use_line_collection=True)
                plt.subplot(1,2,2)
                plt.title('Recovered image histogram')
                plt.stem(h_rec[1],h_rec[0],use_line_collection=True)
                fig_size = plt.gcf().get_size_inches() 
                plt.gcf().set_size_inches(2 * fig_size) 
                plt.savefig("overexposure_restored\\"+f_basename[j]+"level"+str(i)+"_hist.pdf")

            plt.figure()
            plt.imshow(img)
            plt.title(title+'. Image')
            plt.axis("off")

            plt.figure()
            plt.title(title+ '. Recovered image')
            plt.imshow(rec_img)
            plt.axis("off")
            path = "overexposure_restored\\"+f_basename[j]+"level"+str(i)
            dip.im_write(rec_img, path+"_restored.bmp")
            dip.im_write(img, path+".bmp")
            paths.append(path+'_restored.bmp')

        if stats:
            mt.compute_stats(paths,titles,orig_path,False)
    
    if show:
        plt.show()