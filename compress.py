import argparse
import numpy
import OCICLib

def parse_arguments():
    parser = argparse.ArgumentParser(
        description='Compress Images with OCIC Format - © Hans Hardmeier.')
    parser.add_argument('-i','--input',required=True,type=str,help='Image to be compressed')
    parser.add_argument('-o','--output',type=str,help='Image output path')
    return parser.parse_args()

def main():
    args = parse_arguments()
    imarray = OCICLib.read_TIF(args.input)
    imarrayT = OCICLib.transform_image(imarray)
    OCICLib.store_sparse_mat(imarrayT,"a",args.output)
    print("Image has been successfully compressed!")
main()