"""
Driver for loading and resizing images with the SimpleDatasetLoader and the SimplePreprocessor classes
Usage: python resize_images.py --dataset ../dat/img --output ../dat/output
"""
import os
import argparse
from imutils import paths
from cv2 import imwrite
from simpledatasetloader import SimpleDatasetLoader
from simplepreprocessor import SimplePreprocessor

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("-d", "--dataset", required=True, help="path to input dataset")
    ap.add_argument("-o", "--output", required=True, help="path to output directory")
    args = vars(ap.parse_args())

    # get filenames from all subdirectories
    imagePaths = list(paths.list_images(args["dataset"]))
    
    ## instantiate preprocessor and data loader
    print("[INFO] resizing images...\n")
    sp = SimplePreprocessor(64, 64)
    sdl = SimpleDatasetLoader(preprocessors=[sp])
    
    ## load and resize data
    (data, labels) = sdl.load(imagePaths, verbose=500)

    # write to output directory using the labal and order as filename
    for (i, (image, label)) in enumerate(zip(data, labels)):
        fname = os.path.join(args["output"], f"{label}_{i}.png" )
        print(f"[INFO] writing a resized {label[:-1]} to {os.path.basename(fname)}")
        imwrite(fname, image)

if __name__=="__main__":
    main()