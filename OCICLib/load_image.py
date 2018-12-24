import numpy
from PIL import Image

def read_TIF(imageString):
    im = Image.open(imageString)  
    a = numpy.array(im)
    return numpy.array(im) #uint8