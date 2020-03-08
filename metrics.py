
import dippykit as dip
import cv2 as cv
from skimage.metrics import structural_similarity


def mse(img1, img2):
    return dip.MSE(img1,img2)

def psnr(img1, img2):
    return dip.PSNR(img1, img2)

def ssim(img1, img2):
    return structural_similarity(img2, img1, data_range=img1.max()- img1.min(), multichannel=True)

def csv(img1, img2):
    return 0.5
    

def unique(img1,img2):
    return 0.5

    

def full_metrics (img1,img2):
    r_mse = mse(img1, img2)
    r_psnr = psnr(img1, img2)
    r_ssim = ssim(img1, img2)
    r_csv = csv(img1,img2)
    r_unique = unique(img1,img2)
    return (r_mse, r_psnr, r_ssim, r_csv, r_unique)


def print_metrics(title,f_metrics):
    print('\n'+title +'\n')
    print('MSE: '+str(f_metrics[0])+'\n')
    print('PSNR: '+str(f_metrics[1])+'\n')
    print('SSIM: '+str(f_metrics[2])+'\n')
    print('CSV: '+str(f_metrics[3])+'\n')
    print('UNIQUE: '+str(f_metrics[4])+'\n')
