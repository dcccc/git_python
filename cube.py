#coding:utf-8
import os
import re
import glob
import sys


os.chdir(os.getcwd())

if len(sys.argv) > 3 or len(sys.argv) == 1 or len(sys.argv) == 2 :
	print "Input parameter error\npython(.exe) inputfile outputfile"
	sys.exit()
if len(sys.argv) == 0 :
	print "          Usage\n          python(\.exe) cube.py inputfile outputfile"
	sys.exit()
if len(sys.argv) == 3 :
	infile_name = sys.argv[1]
	outfile_name = sys.argv[2]

if os.path.isfile(infile_name) :
	pass
else:
	print "input file doesn\'t exit!"
	sys.exit()




out = open(outfile_name,'a') 

with open(infile_name) as cube :
	n = 1
	m = 1
	t = 0
	for i , line in enumerate(cube) :
		if len(line) > 10 or i <= 1 :
			out.write(line)

		if i == 3 :
			a = int(re.split(r'[\s\-]+',line)[0])
		if i == 4 :
			b = int(re.split(r'[\s\-]+',line)[0])
		if i == 5 :
			c = int(re.split(r'[\s\-]+',line)[0])
		if len(line) <= 10 and len(line) >= 6 and i > 6:
			t=t+1
			line = re.split(r'[\n]+',line)[0]

			if m == b :
				if n < c:
					out.write(line)
					out.write(" ")
				if n == c:
					n = 0
					m = 1
					out.write(line)
					out.write("\n\n\n")
				n = n + 1

			else :
				if n < c:
					out.write(line)
					out.write(" ")
				if n == c:
					n = 0
					m = m + 1
					out.write(line)
					out.write("\n")
				n = n + 1	



out.close()
print t