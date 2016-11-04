#coding:utf-8
import numpy as np
import re ,os
import glob
import string
import math
import sys
import linecache

grd="Pt-I1_density.grd"
outmol="Pt-I1.outmol"

cube=open("111.cube","a")
cube.write("cube file generated from DMol3 density.grd \nby python script\n")

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

vecter=[]
for i in [41,42,43]:
	vecter.append(linecache.getline(outmol,i))
po=[]
i=45
line='     '
while (line.strip() !="$end"):
	line=linecache.getline(outmol,i)
	po.append(line)
	i+=1


cube.write("%d  0.000   0.000   0.000\n" %(len(po)-1))

line=linecache.getline(grd, 4)
fft=map(int, re.split(r'\s+',line.strip()))

for i in range(3):
	lien=vecter[i]
	ve=map(float, re.split(r'\s+',lien.strip()))
	cube.write("%d  %f  %f  %f\n" %(fft[i],ve[0]/fft[i],ve[1]/fft[i],ve[2]/fft[i]))

for i in xrange(len(po)-1):
	a_num=ele_num[po[i][:10].strip()]
	cube.write("%s   0.0000  %s"  %(a_num, po[i][10:]))

n=0
data=[]
while(n<(fft[0]+1)*(fft[1]+1)*(fft[2]+1)):
	line=linecache.getline(grd, n+6)
	data.append(float(line.strip()))
	n+=1

data=np.array(data).reshape(fft[2]+1,fft[1]+1,fft[0]+1)

for i in xrange(fft[0]):
	for j in xrange(fft[1]):
		for k in xrange(fft[2]):
			cube.write("%1.13f\n"  %(data[k,j,i]))
cube.close()
