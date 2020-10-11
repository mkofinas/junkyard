import os
import argparse

import exifread


def parse_arguments():
    parser = argparse.ArgumentParser(
        description='Group images by the devices that captured them')
    parser.add_argument('-d', '--dir', default='.', type=str)

    args = parser.parse_args()
    return args


def main(args):
    files_per_device = {}
    for filename in os.listdir(args.dir):
        if filename.split('.')[-1].lower() in ['jpg', 'jpeg']:
            with open(os.path.join(args.dir, filename), 'rb') as f:
                try:
                    tags = exifread.process_file(f)
                    device = str(tags["Image Make"]) + " " + str(tags["Image Model"])
                    if device not in files_per_device:
                        files_per_device[device] = []
                    files_per_device[device].append(filename)
                except:
                    print(f"{filename} has no tags")
        elif os.path.isdir(filename):
            print(f"{filename} if a directory")
        else:
            print(f"{filename} is not an image")
    print(f"Capturing devices: {files_per_device.keys()}")
    for k, v in files_per_device.items():
        print(k, v)


if __name__ == "__main__":
    arguments = parse_arguments()
    main(arguments)
