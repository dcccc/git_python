import os
import re
import glob
import string
import math
import sys
from PIL import Image


if len(sys.argv) < 1  :
	print "there is no picture to convert!"
else :
	pic = sys.argv[1:]

def pic2txt(pic) :
	if os.path.isfile(pic) :
		p = Image.open(pic)
		for_mat = os.path.splitext(pic)[1]
		txt = open(pic.replace(for_mat , ".txt"),"a")
		for i in range(p.size[1]):
			for j in range(p.size[0]) :
				pixel= map(str, list(p.getpixel((j,i))))
				txt.write("_".join(pixel) + " ")
			txt.write("\n")
		p.close()
	else:
		print pic + " doesn't exist!"

for l in pic :
	pic2txt(l)

