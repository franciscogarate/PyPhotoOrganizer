#!/usr/bin/python
# -*- coding: utf-8 -*-
#http://www.sno.phy.queensu.ca/~phil/exiftool/exiftool_pod.html

import commands
def extrae(file_w,tag):
	return commands.getstatusoutput(("exiftool -EXIF:%s -T '%s'") % (tag,file_w))[1].strip()
	#output = 'Make                            : Apple'
	#init = output.find(':')
	#return output[init+1:].strip()

def escribe(file_w,lat_w,lon_w):
	a = commands.getstatusoutput(('exiftool -EXIF:GPSLatitude=%s %s') % (lat_w,file_w))[1].strip()
	b = commands.getstatusoutput(('exiftool -EXIF:GPSLongitude=%s %s') % (lon_w,file_w))[1].strip()
	return a, b


'''
print extrae('_MISC/IMG_7093B.JPG','Make')
print extrae('GPSLatitude')
'''
#http://www.sno.phy.queensu.ca/~phil/exiftool/exiftool_pod.html#writing_examples
# -csv[=CSVFILE]                   Export/import tags in CSV format
# 40.401727, -3.720627
#http://www.sno.phy.queensu.ca/~phil/exiftool/TagNames/GPS.html

#print escribe('_MISC/IMG_7093B.JPG','42.401727','4.720627')


