#!/usr/bin/python3

import tag
import location as loc






# John and Ronald trip to london - before Cornwall holiday
timestamp = '1972:06:02 12:00:00'
location = loc.hms_belfast
tag.Image(['img1437.jpg']).created(timestamp).rating('good').gps(location).keywords(['1970s']).exiftool()


