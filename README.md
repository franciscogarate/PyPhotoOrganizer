# pyexif (before: PyPhotoOrganizer)
Include geolocation info in your photos with Python and exiftool command (terminal)

I hope the scripts are clear enough to be understood and customized for beginners python users.

### Requirements:
For Linux:
- Python 3.11 or higher
- exiftool (sudo apt-get install exiftool)

For Mac OS:
- Python 3 (libraries: pandas and openxl)
- Imagemagick (brew install imagemagick)
- library exiftools (perl)

Instructions:
- Images must be in a local folder
- Fill info_exif.xlsx. May be used:
	- Windows: dir *.jpg /b > file.csv
 	-  Linux/Mac: find . -type f -iname "*.jpg" | sort -V > file.csv
- Following variables must be completed:
        - path

###Folder Organizer

Also, I include some useful scripts to organize them, depending on the size, camera maker or whatever you want if it's included in Exif info.

Instructions:
- Images must be in a local folder
- Following variables must be completed:
	- path_w
	- typefile_w
	- size_w

### Half-framed:
```
for f in *.jpg; do magick "$f" -crop 2x1@ +repage -scene 1 "${f%.jpg}_crop_%d.jpg"; done
```
