import numpy
import scipy.sparse

def detransform_image(imarrayTsparse):
    imarrayT = imarrayTsparse.toarray()
    length = imarrayT.shape[0]
    return imarrayT.reshape(length,length,3)