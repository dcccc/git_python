#coding:utf-8
import os
import re
import glob
import string
import math
import sys

if len(sys.argv) < 3  :
	print "          Usage\n          python cif2poscar.py n  cciffile or all\n          n is the number of the nonmovale atom\n          all    --all the cellfile in current directory will be coverted"
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


def cif_to_poscar(cif):
	if not os.path.isfile(cif) :
		print cif + " doesn\'t exist"
	else :	
		z = 1
		a_p=[]
		f=open(cif,"r")
		txt = cif.replace("cif","POSCAR")
		POSCAR = open(txt,'a')

		for eachline in f:
			b=re.split(r'[\s]+',eachline)
			if len(b) > 6 :
				a_p.append(b[1:5])
			elif b[0]=="_cell_length_a" :
				A=float(b[1])
			elif b[0]=="_cell_length_b" :
				B=float(b[1])	
			elif b[0]=="_cell_length_c" :
				C=float(b[1])
			elif b[0]=="_cell_angle_alpha" :
				a_=float(b[1])
			elif b[0]=="_cell_angle_beta" :
				b_=float(b[1])
			elif b[0]=="_cell_angle_gamma" :
				c_=float(b[1])

		cx , cy , cz = 0 , 0 , 1
		bx , by , bz = 0 , math.sin(a_/180*math.pi) , math.cos(a_/180*math.pi)
		az = math.cos(b_/180*math.pi)
		ay = (math.cos(c_/180*math.pi)-math.cos(b_/180*math.pi)*math.cos(a_/180*math.pi))/math.sin(a_/180*math.pi)
		ax = 1+2*math.cos(c_/180*math.pi)*math.cos(b_/180*math.pi)*math.cos(a_/180*math.pi) - math.cos(a_/180*math.pi)*math.cos(a_/180*math.pi)-math.cos(b_/180*math.pi)*math.cos(b_/180*math.pi)-math.cos(c_/180*math.pi)*math.cos(c_/180*math.pi)
		ax = math.sqrt(ax)/math.sin(a_/180*math.pi)
		#print  ax*A , ay*A , az*A
		#print  bx*B , by*B , bz*B
		#print  cx*C , cy*C , cz*C
		POSCAR.write("title" + "\n" + "1" + "\n")
		POSCAR.write(str(round(ax*A,5)) + "   " + str(round(ay*A,5))  + "   " + str(round(az*A,5)) + "\n")
		POSCAR.write(str(round(bx*B,5)) + "   " + str(round(by*B,5))  + "   " + str(round(bz*B,5)) + "\n")
		POSCAR.write(str(round(cx*C,5)) + "   " + str(round(cy*C,5))  + "   " + str(round(cz*C,5)) + "\n")



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
	cif_to_poscar(i)
		





