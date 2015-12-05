#coding:utf-8
import os
import re
import glob
import string
import math
import sys
import linecache


if len(sys.argv) != 4  :
	print "          Usage\n          python cell2poscar.py n  cellfile or all\n          n is the number of the nonmovale atom\n          all    --all the cellfile in current directory will be coverted"
	sys.exit()
else :
	cube1 = sys.argv[1]
	cube2 = sys.argv[2]
	cube3 = sys.argv[3]

if not os.path.isfile(cube1) :
	print cube1 + "doesn\'t exist"
	sys.exit()
elif not os.path.isfile(cube2) :
	print cube2 + "doesn\'t exist"
	sys.exit()
elif not os.path.isfile(cube3) :
	print cube3 + "doesn\'t exist"
	sys.exit()

cube4_name = cube1[:-5] + "---char_diff" + ".cube"


cube = open(cube1,"r")

cube4 = open(cube4_name,"a")

for i , line in enumerate(cube) :
	if len(line) < 10 and i > 6 :
		 x = i + 1
		 break
	else :
		cube4.write(line.rstrip() + "\n")


cube = open(cube2,"r")

for i , line in enumerate(cube) :
	if len(line) < 10 and i > 6 :
		 y = i + 1
		 break


cube = open(cube3,"r")

for i , line in enumerate(cube) :
	if len(line) < 10 and i > 6 :
		 z = i + 1
		 break



while (linecache.getline(cube1 , x)) :
	i = str(float(linecache.getline(cube1 , x).rstrip())-float(linecache.getline(cube2 , y).rstrip())-float(linecache.getline(cube3 , z).rstrip())) + "\n"
	cube4.write(i)
	x = x + 1
	y = y + 1
	z = z + 1

cube4.close()
linecache.clearcache()

