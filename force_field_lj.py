#coding=utf-8
import math
import random as random1
import sys
import numpy as np
#from scipy import *
import matplotlib.pyplot as plt
#from matplotlib.figure import savefig

def to_po(num):
	'''将随机选取的序数变为坐标'''
	po=[]
	for i in range(3):
		for j in range(3):
			po.append([num/n+n*i,num%n+n*j])
	return po

def po_sele(seq,sel):
	'''随机选取原子位置'''
	sele_num=[]
	sele_po=[]
	while (len(sele_num) < sel):
		sele_num.append(random1.choice(seq))
		sele_num = list(set(sele_num))
	for i in sele_num:
		sele_po.extend(to_po(i))
	return(sele_po,sele_num)



def distan(sel,sele_po=[]):
	'''计算所选原子间的距离'''
	if sele_po==[]:
		(sele_po,sele_num)=po_sele(range(n**2),sel)
	prim=[[i,j] for i in range(n,n*2) for j in range(n,n*2)]
	suro=[[i,j] for i in range(n-3,n*2+3) for j in range(n-3,n*2+3)]
	sel_suro=[]
	sel_prim=[]
	for i in sele_po :
		if i in prim :
			sel_prim.append(i)
		elif i in suro :
			sel_suro.append(i)
	#print len(sel_prim)
	#print len(sel_suro)

	dis_suro , dis_prim =[],[]
	for i in sel_prim :
		for j in sel_prim :
			dis1=np.sum((a[i[0],i[1],]-a[j[0],j[1],])**2)
			dis1=round(dis1,0)
			if dis1<=12:
				dis_prim.append(dis1)
		for k in sel_suro:
			dis2=np.sum((a[i[0],i[1],]-a[k[0],k[1],])**2)
			dis2=round(dis2,0)
			if dis2 <=12:
				dis_suro.append(dis2)
	#print len(dis_suro)
	#print len(dis_prim)
	return(dis_prim,dis_suro)

def dis_num(dis_prim,dis_suro):
	'''计算所选原子间的距离的数目'''
	dis_list=[1,3,4,7,9,12]
	dis_num=[]
	for i in dis_list :
		dis_num.append(dis_prim.count(i)/2.+dis_suro.count(i)/2.)
	return dis_num

def energy(sele_point):
	'''根据原子间的距离的数目  用拟合关系计算能量'''
	sele_po=[]
	for i in sele_point :
		sele_po.extend(to_po(i))
	(dis_prim,dis_suro)=distan(sel,sele_po=sele_po)
	energy=np.sum(np.array(dis_num(dis_prim,dis_suro))*force_field)
	return energy


n=3
sel=4
force_field=np.array([1,1,1,1,1,1])
a = np.linspace(0,0,2*(n*3)**2).reshape(n*3,n*3,2)
a.dtype=np.float64
#print a.shape
for i in range(n*3):
	for j in range(n*3):
		a[i,j,0] = float(i)+0.50*float(j)
		a[i,j,1] = float(j)*math.sqrt(3.0)*0.5

#(dis_prim,dis_suro)=distan(sel)
#dis_num=dis_num(dis_prim,dis_suro)

#print dis_num


print energy([0,1,2])

#print len(dis_suro)
#print len(dis_prim)





