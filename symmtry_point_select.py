#coding=utf-8
import math
import random
import sys
import numpy as np
from scipy import *
a = np.linspace(0,0,288).reshape(12,12,2)
a.dtype=float64
#print a.shape
for i in range(12):
	for j in range(12):
		a[i,j,0] = float(i)-0.50+0.50*(float(j)-5.50)
		a[i,j,1] = (float(j)-5.50)*math.sqrt(3.0)*0.5

b=np.linspace(0,0,32).reshape(4,4,2)
for i in range(4):
	for j in range(4):
		b[i,j]=[i+4,j+4]


def to_po(num):
	return [[num/4,num%4],[num/4+4,num%4+0],[num/4+0,num%4+4],[num/4+4,num%4+4],[num/4+4,num%4+8],[num/4+8,num%4+4],[num/4+8,num%4+8],[num/4+0,num%4+8],[num/4+8,num%4+0]]

def po_sele(seq,n):
	sele_num=[]
	sele_po=[]
	while (len(sele_num) < n):
		sele_num.append(random.choice(seq))
		sele_num = list(set(sele_num))
	for i in sele_num:
		sele_po.extend(to_po(i))
	return(sele_po,sele_num)


#po = [[i,j] for i in range(12) for j in range(12)]

def distan(aa,bb,po_all):
	de_po = [[i,j] for i in range(aa,aa+4) for j in range(bb,bb+4)]
	pp=[]
	for i in po_all :
		if i in de_po:
			pp.append(i)
	dis=[]
	for i in pp :
		for j in pp:
			dis.append(round((a[i[0],i[1],0]-a[j[0],j[1],0])**2+(a[i[0],i[1],1]-a[j[0],j[1],1])**2,2))
	return sorted(dis)
	#return pp

def all_distan(po_all):
	all_dis = []
	for i in range(2,6):
		for j in range(2,6):
			all_dis.append(distan(i,j,po_all))
	return all_dis

#(po_all,sele_num)=po_sele(range(16),4)

#print len(all_distan(po_all))
def progress_bar(i,l):
	done = "#" * int((i+1)*25/l)
	undone = " " * int(25-len(done))
	percent = (i+1)*100/l
	sys.stdout.write("\r["+done+undone+"]   ("+str(percent)+"%"+')')
	sys.stdout.flush()


po_sin = []
dis_sin = []
m=0
while (m<10000):
	(po_all,sele_num)=po_sele(range(16),3)
	all_dis = all_distan(po_all)
	m=m+1
	n=0
	for i in all_dis :
		if i in dis_sin :
			pass 
		else :
			n=n+1
	if n==16 :
		po_sin.append(sele_num)
		all_dis = sorted(all_dis,key = lambda x : x[-1])
		dis_sin.append(all_dis[0])
	progress_bar(m,10000)

print len(po_sin)
#print dis_sin

