#coding:utf-8
import os
import re
import glob
import sys


os.chdir(os.getcwd())


infile_name = sys.argv[1]





t=0
with open(infile_name) as cube :

	for i , line in enumerate(cube) :

		if len(line) <= 10 and len(line) >= 6 and i > 6:
			
			line = re.split(r'[\n]+',line)[0]

			if line[0]=="-" :
				t=t-float(line[1:])



			else :
				t=t+float(line)






print t