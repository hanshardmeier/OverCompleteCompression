import argparse
import numpy
import OCICLib
from PIL import Image

def parse_arguments():
    parser = argparse.ArgumentParser(
        description='Compress Images with OCIC Format - © Hans Hardmeier.')
    parser.add_argument('-i',
    '--input',required=True,type=str,help='Compressed HD5 image')
    return parser.parse_args()

def main():
    args = parse_arguments()
    imarrayT = OCICLib.load_sparse_mat("a",args.input)
    imarray = OCICLib.detransform_image(imarrayT)
    img = Image.fromarray(imarray,'RGB')
#    img.save('test.tif')
    img.show()
    print("Image has been successfully compressed!")
main()