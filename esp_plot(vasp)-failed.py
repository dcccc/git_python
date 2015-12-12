#coding:utf-8
import os
import re
import glob
import string
import math
import sys

if len(sys.argv) > 2 or len(sys.argv)  < 2 :
	print "          usage\n          python  v_esp.py LOCPOT"
	sys.exit()
if len(sys.argv) == 2 :
	infile_name = sys.argv[1]

if os.path.isfile(infile_name) :
	pass
else:
	print "LOCPOT file doesn\'t exit!"
	sys.exit()

outfile_name = infile_name + ".csv"
espo = open(outfile_name,"a")

with open(infile_name) as LOCPOT :
	n = 0
	esp = 0
	for i , line in enumerate(LOCPOT) :
		line = line.lstrip().rstrip()
		line_sp = re.split(r'\s+' , line)
		if i == 1 :
			aa = float(line)
		elif i == 4 :
			c = math.sqrt(float(line_sp[0])*float(line_sp[0])+float(line_sp[1])*float(line_sp[1])+float(line_sp[2])*float(line_sp[2]))
		elif i == 10 :
			nx = int(line_sp[0])
			ny = int(line_sp[1])
			nz = int(line_sp[2])
		elif len(line) > 60 :
			if (i-11)*5//(nx*ny) == n :
				for j in range(len(line_sp)):
					esp = esp + float(line_sp[j])
			else :
				for j in range(len(line_sp)):
					esp = esp + float(line_sp[j])
				esp = esp/(nx*ny)
				z = c*n/nz
				espo.write(str(z)+","+str(esp)+"\n")
				esp = 0
				n = n + 1
espo.close()

linecache.clearcache()
