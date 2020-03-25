
import metrics as mt
import dippykit as dip
import matplotlib.pyplot as plt
import skimage
import exposure
import matlab.engine



def restore_underexposure(img):
    return exposure.histogram_equalization(img)




if __name__ == "__main__":

    f_basename = ("brussels3","espresso_square","wiseonRocks_square")
    rang1 = (0,)
    rang2 = (1,2,3,4,5)
    histograms = True
    stats = True
    show = True

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
        plt.figure()
        plt.title(f_basename[j] + 'Original Image')
        plt.imshow(orig_img)
        plt.axis("off")
        if histograms:
            orig_hist = mt.histogram(orig_img)
            plt.figure()
            plt.title(f_basename[j] + ' Original Image. Histogram')
            plt.stem(orig_hist[1],orig_hist[0],use_line_collection=True)
            plt.savefig('underexposure_restored\\'+f_basename[j]+"_hist.png")
        

        for i in rang2:
            f = prev_path+"_03_"+str(i)+".jpg"
            img = dip.im_read(f)
            title = f_basename[j] + " underexposure level: "+str(i)
            titles.append(title)
            rec_img = restore_underexposure(img)
             
            if histograms:
                h_rec = mt.histogram(rec_img)
                h = mt.histogram(img)

                plt.figure()
                plt.suptitle(f_basename[j] + ' underexposure level: '+str(i))
                plt.subplot(1,2,1)
                plt.title( 'Image histogram')
                plt.stem(h[1],h[0],use_line_collection=True)
                plt.subplot(1,2,2)
                plt.title('Recovered image histogram')
                plt.stem(h_rec[1],h_rec[0],use_line_collection=True)
                fig_size = plt.gcf().get_size_inches() 
                plt.gcf().set_size_inches(2 * fig_size) 
                plt.savefig("underexposure_restored\\"+f_basename[j]+"level"+str(i)+"_hist.pdf")

            plt.figure()
            plt.imshow(img)
            plt.title(title+'. Image')
            plt.axis("off")

            plt.figure()
            plt.title(title+ '. Recovered image')
            plt.imshow(rec_img)
            plt.axis("off")
            path = "underexposure_restored\\"+f_basename[j]+"level"+str(i)
            dip.im_write(rec_img, path+"_restored.bmp")
            dip.im_write(img, path+".bmp")
            paths.append(path+'_restored.bmp')

        if stats:
            mt.compute_stats(paths,titles,orig_path)
    
    if show:
        plt.show()