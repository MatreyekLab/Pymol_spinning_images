## Import codecs to do some of the writing into files
import codecs

## Import re for doing the character replacement
import re

## Set up the file I want to write to
outfilename = "Rotate_PTEN.pml"
outfile = codecs.open(outfilename, "w", "utf-8", "replace")

## First set of images before it starts looping
outfile.write("set antialias,2\n")
outfile.write("ray 2000\n")
name_string = str(format(1 / 1000,'.6f'))
name_string2 = re.sub('\.', '', name_string, count=1)
outfile.write("png ~/Desktop/Rotating_PTEN/PTEN_rotating_"+name_string2+"\n")

## Loop through making pymol rotate the object, raytrace, then export
for x in range(1,360):
	outfile.write("turn y, 1\n")
	outfile.write("ray 2000\n")
	name_string = str(format((x+1) / 1000,'.6f'))
	name_string2 = re.sub('\.', '', name_string, count=1)
	outfile.write("png ~/Desktop/Rotating_PTEN/PTEN_rotating_"+name_string2+"\n")

## Close the file
outfile.close()