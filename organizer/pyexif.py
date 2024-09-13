#!/usr/bin/python
# -*- coding: utf-8 -*-
from PIL import Image
from PIL.ExifTags import TAGS

def testForExif(imgFileName):
    try:
        exifData = {}
        imgFile = Image.open(imgFileName)
        info = imgFile._getexif()
        if info:
            for (tag, value) in info.items():
                decoded = TAGS.get(tag, tag)
                exifData[decoded] = value
            exifGPS = exifData['Model'] #GSPInfo
            print exifGPS
            #exifData['Make'] = u'Coconut'
            #imgFile.save("nueva3.JPG")
            #if not exifGPS:
                #exifData['GPSLatitudeRef'] = 'N'
                #exifData['GPSLatitude'] = '40/1,24/1,55/1'
                #exifData['GPSLongitudeRef'] = 'W'
                #exifData['GPSLongitude'] = '3/1,42/1,26/1'
                #exifData['Make'] = 'Coconut'
                #Image.save(imgFileName)
    except:
        pass