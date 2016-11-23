import numpy as np
import matplotlib.pyplot as plt
import math
import linecache
import re ,os,sys,glob

if len(sys.argv) < 2  :
	print "python cube_to_cif.py   cubefiles"
	sys.exit()
if sys.argv[1]=="all" :
	cube_list=glob.glob("*.cube")
else:
	cube_list=sys.argv[1:]

ele_list={"1":"H","2":"He","3":"Li","4":"Be","5":"B","6":"C","7":"N","8":"O","9":"F","10":"Ne",
"11":"Na","12":"Mg","13":"Al","14":"Si","15":"P","16":"S","17":"Cl","18":"Ar","19":"K",
"20":"Ca","21":"Sc","22":"Ti","23":"V","24":"Cr","25":"Mn","26":"Fe","27":"Co",
"28":"Ni","29":"Cu","30":"Zn","31":"Ga","32":"Ge","33":"As","34":"Se","35":"Br",
"36":"Kr","37":"Rb","38":"Sr","39":"Y","40":"Zr","41":"Nb","42":"Mo","43":"Tc",
"44":"Ru","45":"Rh","46":"Pd","47":"Ag","48":"Cd","49":"In","50":"Sn","51":"Sb",
"52":"Te","53":"I","54":"Xe","55":"Cs","56":"Ba","57":"La","58":"Ce","59":"Pr",
"60":"Nd","61":"Pm","62":"Sm","63":"Eu","64":"Gd","65":"Tb","66":"Dy","67":"Ho",
"68":"Er","69":"Tm","70":"Yb","71":"Lu","72":"Hf","73":"Ta","74":"W","75":"Re",
"77":"Ir","78":"Pt","79":"Au","80":"Hg","81":"Tl","82":"Pb","83":"Bi","84":"Po",
"85":"At","86":"Rn","87":"Fr","88":"Ra","89":"Ac","90":"Th","91":"Pa","92":"U",
"93":"Np","94":"Pu","95":"Am","96":"Cm","97":"Bk","98":"Cf","99":"Es"}


def cube_to_cif(cubefile):
	
	fft=[]
	for i in [3,4,5,6]:
		line=linecache.getline(cubefile, i)
		line=re.split(r'\s+',line.strip())
		fft.append([int(line[0]),float(line[1]),float(line[2]),float(line[3])])
	
	x_v=fft[1][0]*fft[1][1]+fft[2][0]*fft[2][1]+fft[3][0]*fft[3][1]
	y_v=fft[1][0]*fft[1][2]+fft[2][0]*fft[2][2]+fft[3][0]*fft[3][2]
	z_v=fft[1][0]*fft[1][3]+fft[2][0]*fft[2][3]+fft[3][0]*fft[3][3]
	
	x_sh=fft[0][1]/x_v
	y_sh=fft[0][2]/y_v
	z_sh=fft[0][3]/z_v
	
	po=[]
	for i in xrange(7,7+fft[0][0]):
		line=linecache.getline(cubefile, i)
		line=re.split(r'\s+',line.strip())
		po.append([ele_list[line[0]],float(line[-3])/x_v-x_sh,float(line[-2])/y_v-y_sh,float(line[-1])/z_v-z_sh])
	
	
	x=fft[1][1:]
	y=fft[2][1:]
	z=fft[3][1:]
	
	A = math.sqrt(float(x[0])*float(x[0]) + float(x[1])*float(x[1]) + float(x[2])*float(x[2]))*fft[1][0]*0.5291772
	B = math.sqrt(float(y[0])*float(y[0]) + float(y[1])*float(y[1]) + float(y[2])*float(y[2]))*fft[2][0]*0.5291772
	C = math.sqrt(float(z[0])*float(z[0]) + float(z[1])*float(z[1]) + float(z[2])*float(z[2]))*fft[3][0]*0.5291772
	
	a_ = (float(x[0])*float(y[0]) + float(x[1])*float(y[1]) + float(y[2])*float(y[2])) / A / B
	b_ = (float(x[0])*float(z[0]) + float(x[1])*float(z[1]) + float(x[2])*float(z[2])) / A / C
	c_ = (float(z[0])*float(y[0]) + float(z[1])*float(y[1]) + float(z[2])*float(y[2])) / C / B
	
	
	a_=math.acos(a_)*180/math.pi
	b_=math.acos(b_)*180/math.pi
	c_=math.acos(c_)*180/math.pi
	
	
	head='''data_FePO41.pw
	_audit_creation_date              2016-11-21
	_audit_creation_method            'Materials Studio'
	_symmetry_space_group_name_H-M    'P1'
	_symmetry_Int_Tables_number       1
	_symmetry_cell_setting            triclinic
	loop_
	_symmetry_equiv_pos_as_xyz
	  x,y,z
	_cell_length_a                    %f
	_cell_length_b                    %f
	_cell_length_c                    %f
	_cell_angle_alpha                 %f
	_cell_angle_beta                  %f
	_cell_angle_gamma                 %f
	loop_
	_atom_site_label
	_atom_site_type_symbol
	_atom_site_fract_x
	_atom_site_fract_y
	_atom_site_fract_z
	_atom_site_U_iso_or_equiv
	_atom_site_adp_type
	_atom_site_occupancy\n'''  %(A,B,C,a_,b_,c_)
	
	
	cif_file=open(cubefile[:-4]+".cif","a")
	
	cif_file.write(head)
	
	for i,line in enumerate(po):
		cif_file.write("%s%d   %s   %f  %f   %f    0.00000  Uiso   1.00\n" \
		%(line[0],i+1,line[0],line[1],line[2],line[3]))

for i in cube_list:
	if not os.path.isfile(i) :
		print i + " doesn\'t exist"
	else:
		cube_to_cif(i)