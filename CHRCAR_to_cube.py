#coding:utf-8
import numpy as np
import re ,os
import glob
import string
import math
import sys
import linecache

if len(sys.argv) < 2 :
	print '''Usage      python  CHRCAR_to_cube.py   CHRCAR file
	      '''
	sys.exit()

ele_num={"H":"1","He":"2","Li":"3","Be":"4","B":"5","C":"6","N":"7",
"O":"8","F":"9","Ne":"10","Na":"11","Mg":"12","Al":"13","Si":"14",
"P":"15","S":"16","Cl":"17","Ar":"18","K":"19","Ca":"20","Sc":"21",
"Ti":"22","V":"23","Cr":"24","Mn":"25","Fe":"26","Co":"27","Ni":"28",
"Cu":"29","Zn":"30","Ga":"31","Ge":"32","As":"33","Se":"34","Br":"35",
"Kr":"36","Rb":"37","Sr":"38","Y":"39","Zr":"40","Nb":"41","Mo":"42",
"Tc":"43","Ru":"44","Rh":"45","Pd":"46","Ag":"47","Cd":"48","In":"49",
"Sn":"50","Sb":"51","Te":"52","I":"53","Xe":"54","Cs":"55","Ba":"56",
"La":"57","Ce":"58","Pr":"59","Nd":"60","Pm":"61","Sm":"62","Eu":"63",
"Gd":"64","Tb":"65","Dy":"66","Ho":"67","Er":"68","Tm":"69","Yb":"70",
"Lu":"71","Hf":"72","Ta":"73","W":"74","Re":"75","Ir":"77","Pt":"78",
"Au":"79","Hg":"80","Tl":"81","Pb":"82","Bi":"83","Po":"84","At":"85",
"Rn":"86","Fr":"87","Ra":"88","Ac":"89","Th":"90","Pa":"91","U":"92",
"Np":"93","Pu":"94","Am":"95","Cm":"96","Bk":"97","Cf":"98","Es":"99"}

def chgcar2cube(chgcar):
	if not os.path.isfile(chgcar) :
		print "CHGCAR files doesn\'t exist!"
		sys.exit()
	CHGCAR_file=open(chgcar)
	axis_vector=[]
	atom_pos=[]
	for i , line in enumerate(CHGCAR_file) :		
		if  i in [2,3,4] :
			 axis_vector.append(map(float,re.split(r'\s+',line.strip())))
		if i==5 :
			atom_spe=re.split(r'\s',line.strip())
		if i==6 :
			atom_num=map(int,re.split(r'\s',line.strip()))

		if i>=8 and len(line)>24 :
			atom_pos.append(map(float,re.split(r'\s+',line.strip())))
		if i>9 and len(line)<24 and len(line)>8 :
			fft_grid=map(int, re.split(r'\s+',line.strip()))
			ben_num=i
			break
	atom_pos1=[]	
	for i in range(len(atom_pos)):
		x=(axis_vector[0][0]+axis_vector[1][0]+axis_vector[2][0])*atom_pos[i][0]/0.529177
		y=(axis_vector[0][1]+axis_vector[1][1]+axis_vector[2][1])*atom_pos[i][1]/0.529177
		z=(axis_vector[0][2]+axis_vector[1][2]+axis_vector[2][2])*atom_pos[i][2]/0.529177
		atom_pos1.append("%f %f %f\n"  %(x,y,z))




	cube_file=open(chgcar+".cube","a")
	cube_file.write("cube file generated from CHGCAR \nby python script\n")
	cube_file.write("%d 0.0 0.0 0.0\n"  %(sum(atom_num)))
	for i in xrange(3):
		cube_file.write("%d %f %f %f\n"  %(fft_grid[i],axis_vector[i][0]/fft_grid[i]/0.529177,axis_vector[i][1]/fft_grid[i]/0.529177,axis_vector[i][2]/fft_grid[i]/0.529177))
	atom_l=0
	for i in range(len(atom_num)):
		for j in range(atom_num[i]):
			cube_file.write("%s 0.0 %s"  %(ele_num[atom_spe[i]],atom_pos1[j+atom_l]))
		atom_l+=atom_num[i]

	density=[]
	ben_num+=2
	for i in xrange(int(math.ceil(fft_grid[0]*fft_grid[1]*fft_grid[2]/5))):
		line=linecache.getline(chgcar , ben_num+i)
		density.extend(map(float,re.split(r'\s',line.strip())))
	density=np.array(density).reshape(fft_grid[2],fft_grid[1],fft_grid[0])


	for i in xrange(fft_grid[0]):
		for j in xrange(fft_grid[1]):
			for k in xrange(fft_grid[2]):
				cube_file.write("%1.13f\n"  %(density[k,j,i]))
	cube_file.close()
	CHGCAR_file.close()



	# print axis_vector,atom_pos,atom_num,atom_spe,fft_grid
for i in sys.argv[1:]
	chgcar2cube(i)

