#coding:utf-8
import os
import re
import glob
import string
import math
import sys




if len(sys.argv) < 3  :
	print "          Usage\n          python cell2poscar.py n  cellfile or all\n          n is the number of the nonmovale atom\n          all    --all the cellfile in current directory will be coverted"
	sys.exit()
elif sys.argv[1] == "0" :
	non_mov = "!"
elif sys.argv[1] != "0" :
	non_mov = ""
if sys.argv[2] == "all" :
	os.chdir(os.getcwd())
	a = glob.glob("*.cell")
	n = int(sys.argv[1]) 
elif sys.argv[2] != "all" :
	a = sys.argv[2:]
	n = int(sys.argv[1])

if len(a) == 0 :
	print "there is no cellfile in the diretory"
	sys.exit()



def cell2vasp(cell_name) :
	cell = open(cell_name,'r')
	POS_name = cell_name[:-5] + "----POSCAR"
	POSCAR = open(POS_name,'a')

	POSCAR.write("title\n1" + "\n")

	a_p = []

	for i , line in enumerate(cell) :
		if line.rstrip() == "%ENDBLOCK POSITIONS_FRAC" :
			break
	
		if i == 1 or i == 2 or i == 3 :
			line = line.lstrip()
			POSCAR.write(line)
		elif len(line) > 60 and i > 3:
			line = line.lstrip()
			line_sp = re.split(r'\s+',line)
			a_p.append(line_sp[0:4])


	a_p = sorted(a_p , key = lambda x : x[3] )

	elem_num = []

	for i , eachline in enumerate(a_p) :
		elem_num.append(eachline[0])
		if i < n :
			eachline.append(non_mov + "F  F  F")
		else:
			eachline.append(non_mov + "T  T  T")

	elem = sorted(list(set(elem_num)))

	at_sp = ""
	at_num = ""


	for line in elem :
		at_num = at_num + str(elem_num.count(line)) + "   "
		at_sp = at_sp + line + "   "

	POSCAR.write("!" + at_sp + "\n")
	POSCAR.write(at_num + "\n")
	POSCAR.write("Selective dynamic\nDirect\n")

	a_v = sorted(a_p , key = lambda x : x[0] )

	for line in a_v :
		POSCAR.write(line[1] + "   " + line[2] + "   " + line[3] + "   " + line[4] + "\n")

	POSCAR.close()



for i in a :
	cell2vasp(i)



