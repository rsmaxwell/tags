#!/usr/bin/python3

# https://www.mcleanit.ca/blog/synology-check-index-progress/


import sys, os, subprocess

class Location:
    def __init__(self, latitudeDeg, latitudeMin, latitudeSec, latitudeRef, longitudeDeg, longitudeMin, longitudeSec, longitudeRef):
        self.latitudeDeg = latitudeDeg
        self.latitudeMin = latitudeMin
        self.latitudeSec = latitudeSec
        self.latitudeRef = latitudeRef

        self.longitudeDeg = longitudeDeg
        self.longitudeMin = longitudeMin
        self.longitudeSec = longitudeSec
        self.longitudeRef = longitudeRef




class Image:
    def __init__(self, filenames):
        self.filenames = filenames
        self.args = ["exiftool"]
        self.args.append("-overwrite_original_in_place")

    def created(self, value):
        self.args.append("-CreateDate=" + value)
        self.args.append("-DateTimeOriginal=" + value)
        return self

    def rating(self, value):
        if (value == 'poor'):
            rating = 1
            ratingPercent = 1
        elif (value == 'fair'):
            rating = 2
            ratingPercent = 25
        elif (value == 'average'):
            rating = 3
            ratingPercent = 50
        elif (value == 'good'):
            rating = 4
            ratingPercent = 75
        elif (value == 'excellent'):
            rating = 5
            ratingPercent = 99
        else:
            printf('Unexpected Rating: ' + value)
            sys.exit(1)
            
        self.args.append("-Rating=" + str(rating))
        self.args.append("-xmp-microsoft:RatingPercent=" + str(ratingPercent))

        return self

    def gps(self, value):
        self.args.append("-GPSLatitudeRef=" + value.latitudeRef)
        self.args.append("-GPSLatitude=" + str(value.latitudeDeg) + ' deg ' + str(value.latitudeMin) + "' " + str(value.latitudeSec) + '"')
        self.args.append("-GPSLongitudeRef=" + value.longitudeRef)
        self.args.append("-GPSLongitude=" + str(value.longitudeDeg) + ' deg ' + str(value.longitudeMin) + "' " + str(value.longitudeSec) + '"')
        return self

    def gps_clear(self):
        self.args.append("-GPSLatitudeRef=")
        self.args.append("-GPSLatitude=")
        self.args.append("-GPSLongitudeRef=")
        self.args.append("-GPSLongitude=")
        return self

    def keywords(self, value):
        for tag in (value):
            self.args.append("-Keywords=" + tag)
        return self 

    def keywords_clear(self):
        self.args.append("-Keywords=")
        return self 

    def exiftool(self):
        for filename in (self.filenames):
            self.args.append("-ignoreMinorErrors")
            args = self.args.copy()
            args.append(filename)
            print("Updating " + filename)
            try:
                subprocess.run(args, stdout=None, stderr=None, check=True)
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


