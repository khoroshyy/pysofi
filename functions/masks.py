import numpy as np

def gauss2D_mask(shape = (3,3), sigma = 0.5):
    """
    2D gaussian mask - should give the same result as MATLAB's
    fspecial('gaussian',[shape],[sigma])
    """
    mdim, ndim = [(pixel-1) / 2 for pixel in shape]
    y, x = np.ogrid[-mdim:(mdim + 1), -ndim:(ndim + 1)]
    h = np.exp( -(x*x + y*y) / (2*sigma*sigma) )
    h[h < np.finfo(h.dtype).eps * h.max()] = 0
    sumh = h.sum()
    if sumh != 0:
        h /= sumh
    return h

def gauss1D_mask(shape = (1,3), sigma = 0.5):
    return gauss2D_mask(shape, sigma)[0]