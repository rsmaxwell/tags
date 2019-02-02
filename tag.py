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

calais = Location(50, 57, 39.08, 'North', 1, 50, 53.57, 'East')
deanrow = Location(53, 19, 45.1, 'North', 2, 11, 23.9, 'East')
zermatt = Location(46, 1, 14.7, 'North', 7, 44, 57.0, 'East')
stanneylands_road = Location(53, 20, 22.0, 'North', 2, 13, 27.7, 'East')
criccieth = Location(52, 54, 55.6, 'North', 4, 14, 5.8, 'West')
meeting_house_wilmslow = Location(53, 19, 36.4, 'North', 2, 14, 30.2, 'West')
wastwater = Location(54, 26, 20.2, 'North', 3, 18, 20.5, 'West')
deanrow = Location(53, 19, 49.1, 'North', 2, 11, 38.5, 'West')
southampton_docks = Location(50, 53, 38.9, 'North', 1, 23, 58.7, 'West')
st_agnus_rustington = Location(50, 48, 50.2, 'North', 0, 30, 2.1, 'West')
north_shields = Location(50, 0, 37.2, 'North', 1, 26, 59.5, 'West')
north_shields_dock = Location(50, 0, 9.6, 'North', 1, 26, 46.6, 'West')
burnmoor_inn_eskdale = Location(54, 23, 54.0, 'North', 3, 16, 13.0, 'West')
seascale = Location(54, 23, 52.9, 'North', 3, 28, 38.4, 'West')
george_square_glasgow = Location(55, 51, 39.7, 'North', 4, 15, 0.1, 'West')
st_bees_beach = Location(54, 29, 22.8, 'North', 3, 36, 17.4, 'West')
newtown = Location(54, 20, 52.9, 'North', 3, 23, 48.1, 'West')
muncaster_bridge = Location(54, 21, 20.1, 'North', 3, 21, 59.0, 'West')
elms_road_leicester = Location(52, 36, 28.2, 'North', 1, 6, 23.9, 'West')
avenue_road_leicester = Location(52, 37, 0.8, 'North', 1, 6, 38.2, 'West')
coniston_water = Location(54, 18, 31.4, 'North', 3, 5, 7.0, 'West')
windermere = Location(54, 25, 9.8, 'North', 2, 57, 44.1, 'West')
seascale_beach = Location(54, 22, 47.9, 'North', 3, 28, 22.7, 'West')
wicksteed_park = Location(52, 23, 5.0, 'North', 0, 42, 26.5, 'West')
cockley_beck = Location(54, 24, 17.8, 'North', 3, 9, 42.8, 'West')
thornwaite_crag = Location(54, 21, 0.4, 'North', 3, 23, 19.8, 'West')
ravenglass = Location(54, 21, 13.3, 'North', 3, 24, 38.7, 'West')
ashness_bridge = Location(54, 34, 1.4, 'North', 3, 7, 47.0, 'West')
bradgate_park = Location(52, 41, 6.0, 'North', 1, 13, 25.9, 'West')
one_oak_lane_wilmslow = Location(53, 19, 37.6, 'North', 2, 12, 10.3, 'West')
gibraltar = Location(36, 7, 19.2, 'North', 5, 20, 35.3, 'West')
whitby = Location(54, 29, 12.3, 'North', 0, 36, 49.3, 'West')
cha_whitby = Location(54, 28, 17.6, 'North', 0, 36, 51.3, 'West')



class Image:
    def __init__(self, filenames):
        self.filenames = filenames
        self.args = ["exiftool"]
        self.args.append("-overwrite_original_in_place")

    def created(self, value):
        self.args.append("-CreateDate=" + value)
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

    def tag(self, value):
        for tag in (value):
            self.args.append("-Keywords=" + tag)
        return self 

    def exiftool(self):
        for filename in (self.filenames):
            args = self.args.copy()
            args.append(filename)
            print("Updating " + filename)
            try:
                subprocess.run(args, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
            except subprocess.CalledProcessError as e:
                print("Process ended with an error:")
                print("-----[ args ]------------------")
                for arg in args:
                    print("    " + arg)
                if (e.stdout != None):
                    print("-----[ stdout ]------------------")
                    print("stdout:" + e.stdout.decode('utf-8'))
                if (e.stderr != None):
                    print("-----[ stderr ]------------------")
                    print("stderr:" + e.stderr.decode('utf-8'))
                print("-----[ returncode: " + str(e.returncode) + " ]------------------")
                sys.exit(1)


