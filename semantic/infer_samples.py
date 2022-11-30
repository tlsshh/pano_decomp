import os
import sys
from os import listdir
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + '/..')


import argparse
import cv2
from pathlib import Path


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--samples-path', type=str, default='../data/samples')
    parser.add_argument('--out-path', type=str, default='../data/out_samples')
    parser.add_argument('--height', type=int, default=256)
    opt = parser.parse_args()
    return opt


def list_files(directory, extension):
    """ List files with specified suffixes in the directory (exclude subdirectories)
    """
    file_list = listdir(directory)
    included_list = []
    for f in file_list:
        for ext in extension:
            if f.endswith('.' + ext):
                included_list.append((directory, f))
                break
    return included_list


if __name__ == '__main__':
    opt = parse_args()

    # list all samples
    input_image_file_list = list_files(opt.samples_path, ['jpg', 'jpeg', 'png', 'tif', 'JPG'])

    # process
    if not os.path.exists(opt.out_path):
        os.makedirs(opt.out_path)
    for d, img_name in input_image_file_list:
        img_path = os.path.join(d, img_name)
        im = cv2.imread(img_path)
        im = cv2.resize(im, (opt.height * 2, opt.height), interpolation=cv2.INTER_AREA)
        out_file_path = os.path.join(opt.out_path, f"resized_{img_name}")
        cv2.imwrite(out_file_path, im)
        print(f"Write image: {out_file_path}")
