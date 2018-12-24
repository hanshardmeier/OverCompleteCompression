import argparse
import numpy
import OCICLib
from PIL import Image

def parse_arguments():
    parser = argparse.ArgumentParser(
        description='Compress Images with OCIC Format - © Hans Hardmeier.')
    parser.add_argument('-i',
    '--input1',help='Image')
    return parser.parse_args()

def main():
    args = parse_arguments()
    imarray1 = OCICLib.read_TIF(args.input1)
    imarrayT = OCICLib.transform_image(imarray1)
    imarray2 = OCICLib.detransform_image(imarrayT)

    imageFull=numpy.concatenate((imarray1,imarray2),axis=1)
    img = Image.fromarray(imageFull,'RGB')
    img.save('compare.tif')
    img.show()
    ssq = numpy.sum((imarray1-imarray2)**2)
    print("Sum of square difference: "+str(ssq))

main()