#!/usr/bin/python
# -*- coding: utf-8 -*-

import exiftool
import os
from os.path import join, getsize, exists

path_w = '/Users/user_name/Desktop/Camera_nexus5'

def test(path,filetype,destination='_MISC'):
	if not os.path.exists(join(path_w,destination)): os.makedirs(join(path_w,destination))
	for dirpath, dirnames, filenames in os.walk(path):
		if destination in dirpath:
			pass
		else:
			for i in range(0,len(filenames)):
				fichero = join(dirpath, filenames[i])
				if(filetype in filenames[i]):
					if exiftool.extrae(fichero,'Make') != 'LGE':
						print "moviendo"
						os.system("mv '%s' '%s'" % (fichero,join(path,destination)))
					else:
						#print fichero
						pass


test(path_w,'.JPG')