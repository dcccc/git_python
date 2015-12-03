#coding=utf-8
import re
import math

def pw_to_cif(pw):
	
	f=open(pw,'r')
	cif=pw.replace("inp","cif")
	a=open(cif,'a')
	i="data_O-TiO2-110-8\n_audit_creation_date              2015-08-28\n_audit_creation_method            'Materials Studio'\n_symmetry_space_group_name_H-M    'P1'\n_symmetry_Int_Tables_number       1\n_symmetry_cell_setting            triclinic\nloop_\n_symmetry_equiv_pos_as_xyz\n  x,y,z\n"
	a.write(i)

	n = 1
	a_,b_,c_,A,B,C =0,0,0,0,0,0
	for eachline in f:
		b=eachline.lstrip()
		b=re.split(r'\s+',b)
		#b=re.match(r'(\w{1,2}\d{1,3}\s+)(\w{1,2}\s+\d.\d{4}\s+\d.\d{4}\s+\d.\d{4})(\s+)(.*)',eachline)
		if b[0]=="celldm(1)" :
			b=b[2].rstrip(',')
			A=float(b)
		elif b[0]=="celldm(2)" :
			b=b[2].rstrip(',')
			B=float(b)	
		elif b[0]=="celldm(3)" :
			b=b[2].rstrip(',')
			C=float(b)
		elif b[0]=="celldm(4)" :
			b=b[2].rstrip(',')
			a_=float(b)
		elif b[0]=="celldm(5)" :
			b=b[2].rstrip(',')
			b_=float(b)
		elif b[0]=="celldm(6)" :
			b=b[2].rstrip(',')
			c_=float(b)


	A=float(A) * 0.5291772
	B=A * float(B)
	C=A * float(C)

	if a_:
		a_=math.acos(a_)*180/math.pi
	else:
		a_ = 90
	if b_:
		b_=math.acos(b_)*180/math.pi
	else:
		b_ = 90
	if c_:
		c_=math.acos(c_)*180/math.pi
	else:
		c_ = 90

	i="_cell_length_a                    " + str(A) + '\n'
	a.write(i)
	i="_cell_length_b                    " + str(B) + '\n'
	a.write(i)
	i="_cell_length_c                    " + str(C) + '\n'
	a.write(i)
	i="_cell_angle_alpha                 " + str(a_) + '\n'
	a.write(i)
	i="_cell_angle_beta                  " + str(b_) + '\n'
	a.write(i)
	i="_cell_angle_gamma                 " + str(c_) + '\n'
	a.write(i)

	i="loop_\n_atom_site_label\n_atom_site_type_symbol\n_atom_site_fract_x\n_atom_site_fract_y\n_atom_site_fract_z\n_atom_site_U_iso_or_equiv\n_atom_site_adp_type\n_atom_site_occupancy\n"
	a.write(i)

	f=open(pw,'r')
	for eachline in f:
		b=eachline.lstrip()
		b=re.split(r'\s+',b)
		#print b
		if len(b) >= 4 and len(b[2]) > 6 and len(b[1]) > 6 and "0" in b[2] :
			a=open(cif,'a')  #参数a表示追加写入
			d=str(n)
			c=b[0]+d+"    "+b[0]+"    "+b[1]+"    "+b[2]+"    "+b[3]+"   0.00000  Uiso   1.00"+"\n"
			n=n+1
			#print c
			a.write(c)
			#print c
			a.close()
