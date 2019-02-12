#!/usr/bin/python3

import tag
import location as loc


tag.Image(['img1559.jpg']).gps(loc.stanneylands_road).exiftool()
