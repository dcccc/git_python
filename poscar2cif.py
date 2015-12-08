#coding:utf-8
import os
import re
import glob
import string
import math
import sys


if len(sys.argv) < 2  :
	print "          Usage\n          python poscar2cif.py [poscarfile]\n          pascarfile     --the pascarfile will be converted"
	sys.exit()
elif len(sys.argv) >= 1 :
	a = sys.argv[1:]
else :
	sys.exit()




def pos2cif(addr) :
	if not os.path.isfile(addr) :
		print addr + " doesn\'t exist"
	else :
		poscar = open(addr,"r")
		cif_addr = addr + ".cif"

		a1 = open(cif_addr,"a")

		at_pos = []

		for i , line in enumerate(poscar) :
			line = line.lstrip().rstrip()
			line_sp = re.split(r'\s+' , line)
			if i == 1 :
				a = float(line)
				continue
			elif i == 2 :
				x = line_sp
				continue
			elif i == 3 :
				y = line_sp
				continue
			elif i == 4 :
				z = line_sp
				continue
			elif i == 5:
				elem = re.split(r"\s+",line.replace("!" , ""))
				continue
			elif i == 6 :
				elem_num = line_sp
				continue
			elif line == "" :
				break
			elif len(line_sp) >= 3 :
				at_pos.append(line_sp[0:3])



		A = math.sqrt(float(x[0])*float(x[0]) + float(x[1])*float(x[1]) + float(x[2])*float(x[2]))
		B = math.sqrt(float(y[0])*float(y[0]) + float(y[1])*float(y[1]) + float(y[2])*float(y[2]))
		C = math.sqrt(float(z[0])*float(z[0]) + float(z[1])*float(z[1]) + float(z[2])*float(z[2]))

		a_ = (float(x[0])*float(y[0]) + float(x[1])*float(y[1]) + float(y[2])*float(y[2])) / A / B
		b_ = (float(x[0])*float(z[0]) + float(x[1])*float(z[1]) + float(x[2])*float(z[2])) / A / C
		c_ = (float(z[0])*float(y[0]) + float(z[1])*float(y[1]) + float(z[2])*float(y[2])) / C / B


		a_=math.acos(a_)*180/math.pi
		b_=math.acos(b_)*180/math.pi
		c_=math.acos(c_)*180/math.pi


		a1.write("data_O-TiO2-110-8\n_audit_creation_date              2015-08-28\n_audit_creation_method            'Materials Studio'\n_symmetry_space_group_name_H-M    'P1'\n_symmetry_Int_Tables_number       1\n_symmetry_cell_setting            triclinic\nloop_\n_symmetry_equiv_pos_as_xyz\n  x,y,z\n")


		i="_cell_length_a                    " + str(A*a) + '\n'
		a1.write(i)
		i="_cell_length_b                    " + str(B*a) + '\n'
		a1.write(i)
		i="_cell_length_c                    " + str(C*a) + '\n'
		a1.write(i)
		i="_cell_angle_alpha                 " + str(c_) + '\n'
		a1.write(i)
		i="_cell_angle_beta                  " + str(b_) + '\n'
		a1.write(i)
		i="_cell_angle_gamma                 " + str(a_) + '\n'
		a1.write(i)
		i="loop_\n_atom_site_label\n_atom_site_type_symbol\n_atom_site_fract_x\n_atom_site_fract_y\n_atom_site_fract_z\n_atom_site_U_iso_or_equiv\n_atom_site_adp_type\n_atom_site_occupancy\n"
		a1.write(i)



		a = int(elem_num[0])
		b = a + int(elem_num[1])
		c = b + int(elem_num[2])

		for i , line in enumerate(at_pos) :
			if i < a :
				a1.write(elem[0]+str(i+1)+"    "+elem[0]+"    "+line[0]+"    "+line[1]+"    "+line[2]+"   0.00000  Uiso   1.00"+"\n")
			elif i < b :
				a1.write(elem[1]+str(i+1)+"    "+elem[1]+"    "+line[0]+"    "+line[1]+"    "+line[2]+"   0.00000  Uiso   1.00"+"\n")
			elif i <= c :
				a1.write(elem[2]+str(i+1)+"    "+elem[2]+"    "+line[0]+"    "+line[1]+"    "+line[2]+"   0.00000  Uiso   1.00"+"\n")

for i in a :
	pos2cif(i)
