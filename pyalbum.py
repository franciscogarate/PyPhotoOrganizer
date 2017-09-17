#!/usr/bin/python
# -*- coding: utf-8 -*-
#import pyexif
import os
from os.path import join, getsize, exists
#dirpath is a string, the path to the directory
#dirnames is a list of the names of the subdirectories in dirpath
#filenames is a list of the names of the non-directory files in dirpath

'''
if not os.path.exists(directory):
    os.makedirs(directory)
'''

def deletefolderempty():
	for dirpath, dirnames, filenames in os.walk(path_w):
		if '_MISC' in dirpath:
			pass
		elif '_MOV' in dirpath:
			pass
		elif len(filenames) == 0:# and not '_MISC' in dirpath and not '_MOV' in dirpath:
			print dirpath
			#rmdir don't delete directory that are not empty
			os.system("rmdir '%s'" % (dirpath))

def cleanfiles():
	files_to_delete = (".DS_Store","Thumbs.db")
	for dirpath, dirnames, filenames in os.walk(path_w):
		for i in range(0,len(filenames)):
			# delete files
			if filenames[i] in files_to_delete:
				#pass
				print "deleting %s" % (join(dirpath, filenames[i]))
				os.system("rm '%s'" % (join(dirpath, filenames[i])))
			
def mvsmallfiles(path,filetype,size_mb,destination='_MISC'):
	if not os.path.exists(join(path_w,destination)): os.makedirs(join(path_w,destination))
	for dirpath, dirnames, filenames in os.walk(path):
		if destination in dirpath:
			pass
		else:
			for i in range(0,len(filenames)):
				if(filetype in filenames[i]) and getsize(join(dirpath, filenames[i])) < size_mb * 1000000:
					pass
					#print "moving %s to _MISC" % (join(dirpath, filenames[i]))	
					os.system("mv '%s' '%s'" % (join(dirpath, filenames[i]),join(path_w,destination)))

def movetype(path,filetype,destination='_MOV'):
	if not os.path.exists(join(path_w,destination)): os.makedirs(join(path_w,destination))
	for dirpath, dirnames, filenames in os.walk(path):
		if destination in dirpath:
			pass
		else:
			for i in range(0,len(filenames)):
				# move or delete by extension: .MOV
				ficheros = []
				if(filetype in filenames[i]):
					ficheros.append(filenames[i])
					print "moving %s to _MOV" % (join(dirpath, filenames[i]))
					os.system("mv '%s' '%s'" % (join(dirpath, filenames[i]),join(path,destination)))
					#pyexif.testForExif(os.path.join(dirpath, filenames[i]))
					#print len(ficheros)
					#print len(set(ficheros))

def remayusc(path,filetype):
	for dirpath, dirnames, filenames in os.walk(path):
		for i in range(0,len(filenames)):
			if(filetype in filenames[i]):
				os.system("mv '%s' '%s'" % (join(dirpath, filenames[i]),join(dirpath, filenames[i].upper())))
				#pyexif.testForExif(os.path.join(dirpath, filenames[i]))

def renamimg(path,filetype):
	for dirpath, dirnames, filenames in os.walk(path):
		for i in range(0,len(filenames)):
			if(filetype in filenames[i]):
				nuevo_w = 'IMG_' + str(i+1).zfill(4) + '.JPG'
				os.system("mv '%s' '%s'" % (join(dirpath, filenames[i]),join(dirpath, nuevo_w)))

path_w = '/Volumes/Lightroom'
cleanfiles()
#remayusc(path_w,'.jpg')
#mvsmallfiles(path_w,'.JPG',1)
#movetype(path_w,'.mp4','_MOV')
#renamimg(path_w,'.JPG')

print "Finish %s" % ('--')
