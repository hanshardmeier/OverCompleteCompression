import scipy.sparse
import numpy

def transform_image(imarray):
    length = imarray.shape[0]
    imarray2D = imarray.reshape(length,
        imarray.shape[1]*imarray.shape[2])    
    return scipy.sparse.csr_matrix(imarray2D)