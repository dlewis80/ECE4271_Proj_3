
import dippykit as dip
import numpy as np
from skimage.metrics import structural_similarity
import matlab.engine


def histogram(img1):
    im = img1.ravel()
    return (np.bincount(im,minlength = 256),np.arange(256))
    

def compute_stats(paths,titles,orig_path):
    eng = matlab.engine.start_matlab()
    eng.compute_stats(paths,titles,orig_path,nargout=0)
    eng.quit()