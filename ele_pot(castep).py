#coding:utf-8
import os
import re
import glob
import sys

if len(sys.argv) < 2  :
	print "          Usage\n          ele_pot(castep).py  pot_fmtfiles or all\n          all    --all the xx.cif in current directory  will be converted\n          pot_fmtfiles     --the pot_fmtfiles will be converted"
	sys.exit()
elif len(sys.argv) == 2 and sys.argv[1] == "all":
	os.chdir(os.getcwd())
	a = glob.glob("*.pot_fmt")
elif len(sys.argv) >= 2 and sys.argv[1] != "all":
	a = sys.argv[1:]
else :
	sys.exit()


if len(a) == 0 :
	print "there is no file to be converted"

def pot_fmt_H(pot_fmt) :
	if not os.path.isfile(pot_fmt) :
		print pot_fmt + " doesn\'t exist"
	else :
		csv_name = pot_fmt.replace("pot_fmt","csv")
		out = open(csv_name,'a') 

		with open(pot_fmt) as pot_fmt :
			n = 1
			m = 1
			t = 0
			pot = []
			for i , line in enumerate(pot_fmt) :
				line = line.lstrip().rstrip()
				line_sp = re.split(r"\s+",line)
				if i == 8 :
					na = int(line_sp[0])
					nb = int(line_sp[1])
					nc = int(line_sp[2])
					x = 11+na*nb*nc
				elif i >= 11 and  i < x :
					if len(pot) >= int(line_sp[2]) :
						pot[int(line_sp[2])-1] = pot[int(line_sp[2])-1] + float(line_sp[3])
					else :
						pot.append(float(line_sp[3]))
				elif i >= 11 and i >= x :
					break

		for i in range(len(pot)) :
			out.write(str(i+1) + "," + str(pot[i]/(na*nb)) + "\n")

		out.close()

for i in a :
	pot_fmt_H(i)


