#!/usr/bin/python3

# https://www.mcleanit.ca/blog/synology-check-index-progress/


import sys, os, subprocess


valid_images = [".jpg",".jpeg",".gif",".png"]

args = ["exiftool"]
args.append("-GPSLatitude")

print(" ")
print("Image files with GPS tags:")
print(" ")

for file in os.listdir('.'):

    ext = os.path.splitext(file)[1]
    if ext.lower() not in valid_images:
        continue

    try:
        args2 = args.copy()
        args2.append(file)
        result = subprocess.run(args2, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)

    except subprocess.CalledProcessError as e:
        print("Process ended with an error:")
        print("-----[ args ]------------------")
        print("   ")
        for arg in args:
            print(' "' + arg.replace('"', '\\"') + '"', end='')
        print("")
        print("-----[ output ]------------------")
        print(e.output)
        print("-----[ returncode: " + str(e.returncode) + " ]------------------")
        sys.exit(1)

    stdout = str(result.stdout)

    # print(file + ": " + stdout)
    # print("length: " + str(len(stdout)))

    if len(stdout) > 3:
        print(', "' + file + '"')



print(" ")
print("Image files without GPS tags:")
print(" ")

for file in os.listdir('.'):

    ext = os.path.splitext(file)[1]
    if ext.lower() not in valid_images:
        continue

    try:
        args2 = args.copy()
        args2.append(file)
        result = subprocess.run(args2, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)

    except subprocess.CalledProcessError as e:
        print("Process ended with an error:")
        print("-----[ args ]------------------")
        print("   ")
        for arg in args:
            print(' "' + arg.replace('"', '\\"') + '"', end='')
        print("")
        print("-----[ output ]------------------")
        print(e.output)
        print("-----[ returncode: " + str(e.returncode) + " ]------------------")
        sys.exit(1)

    stdout = str(result.stdout)

    # print(file + ": " + stdout)
    # print("length: " + str(len(stdout)))

    if len(stdout) <= 3:
        print(', "' + file + '"')