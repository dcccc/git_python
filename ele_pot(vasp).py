#coding:utf-8
import os
import re
import glob
import string
import math
import sys

if len(sys.argv)  < 2 :
	print "          usage\n          python  v_esp.py LOCPOT"
	sys.exit()
elif len(sys.argv) >= 2 and sys.argv[1] != "all" :
	infile = sys.argv[1:]	
	

def loc_plot(infile_name):
	if not os.path.isfile(infile_name) :
		print "LOCPOT file doesn\'t exit!"
	else :
		outfile_name = infile_name + ".csv"
		espo = open(outfile_name,"a")

		with open(infile_name) as LOCPOT :
			for i , line in enumerate(LOCPOT) :
				line = line.lstrip().rstrip()
				line_sp = re.split(r'\s+' , line)
				if i == 1 :
					aa = float(line)
				elif i == 4 :
					c = math.sqrt(float(line_sp[0])*float(line_sp[0])+float(line_sp[1])*float(line_sp[1])+float(line_sp[2])*float(line_sp[2]))
				elif len(line) >= 11 and len(line) <= 15 and i > 8 :
					nx = int(line_sp[0])
					ny = int(line_sp[1])
					nz = int(line_sp[2])
					nn = i
					break

		with open(infile_name) as LOCPOT :
			n = 0
			m = 0
			esp = 0
			mm = nx*ny
			for i , line in enumerate(LOCPOT) :
				line = line.lstrip().rstrip()
				line_sp = re.split(r'\s+' , line)
				if i > nn:
					for j in range(len(line_sp)):
						if (m+1) < mm :				
							esp = esp + float(line_sp[j])
							m = m + 1
						else :
							esp = esp + float(line_sp[j])
							esp = esp/mm
							z = c*n*aa/nz
							espo.write(str(z)+","+str(esp)+"\n")
							esp = 0
							n = n + 1
							m = 0
		espo.close()

for i in infile :
	loc_plot(i)

