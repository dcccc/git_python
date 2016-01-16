#coding=utf-8
import math
import random
import sys
import numpy as np
from scipy import *

def to_po(num):
	m=int(round(n/2.0,0))
	po=[]
	for i in range(m+1):
		for j in range(m+1):
			po.append([num/n+n*i,num%n+n*j])
	return po

def po_sele(seq,n):
	sele_num=[]
	sele_po=[]
	while (len(sele_num) < n):
		sele_num.append(random.choice(seq))
		sele_num = list(set(sele_num))
	for i in sele_num:
		sele_po.extend(to_po(i))
	return(sele_po,sele_num)

def distan(aa,bb,po_all):
	de_po = [[i,j] for i in range(aa,aa+n) for j in range(bb,bb+n)]
	pp=[]
	for i in po_all :
		if i in de_po:
			pp.append(i)
	dis=[]
	for i in pp :
		for j in pp:
			dis.append(round((a[i[0],i[1],0]-a[j[0],j[1],0])**2+(a[i[0],i[1],1]-a[j[0],j[1],1])**2,2))
	return sorted(dis)

def all_distan(po_all):
	all_dis = []
	m=int(round(n/2.0,0))
	for i in range(m,m+n):
		for j in range(m,m+n):
			all_dis.append(distan(i,j,po_all))
	return all_dis

def progress_bar(i,l):
	done = "#" * int((i+1)*25/l)
	undone = " " * int(25-len(done))
	percent = (i+1)*100/l
	sys.stdout.write("\r["+done+undone+"]   ("+str(percent)+"%"+')')
	sys.stdout.flush()



def num_cir(sel,cir_num):
	po_sin = []
	dis_sin = []
	num_sin =[]
	mm=0
	while (mm<cir_num):
		(po_all,sele_num)=po_sele(range(n**2),sel)
		all_dis = all_distan(po_all)
		mm=mm+1
		nn=0
		if dis_sin == []:
			all_dis = sorted(all_dis,key = lambda x : x[-1])
			dis_sin.append(all_dis[0])
			po_sin.append(sele_num)
			num_sin.append(0)
		for i,line in enumerate(dis_sin) :
			if line in all_dis :
				 num_sin[i] = num_sin[i]+1
			else :
				nn=nn+1
		if nn==len(po_sin) :
			po_sin.append(sele_num)
			all_dis = sorted(all_dis,key = lambda x : x[-1])
			dis_sin.append(all_dis[0])
			num_sin.append(1)
			
		progress_bar(mm,cir_num)
	return(po_sin,dis_sin,num_sin)



def sortall(po_sin,dis_sin,num_sin):
	m=len(po_sin)
	for i in range(m-1):
		for j in range(m-i-1):
			if dis_sin[j][-1] > dis_sin[j+1][-1] :
				a=dis_sin[j+1]
				dis_sin[j+1] = dis_sin[j]
				dis_sin[j] = a

				a=po_sin[j+1]
				po_sin[j+1] = po_sin[j]
				po_sin[j] = a

				a=num_sin[j+1]
				num_sin[j+1] = num_sin[j]
				num_sin[j] = a
	return(po_sin,dis_sin,num_sin)

#print len(po_sin)
n=4
a = np.linspace(0,0,2*(n*3)**2).reshape(n*3,n*3,2)
a.dtype=float64
#print a.shape
for i in range(n*3):
	for j in range(n*3):
		a[i,j,0] = float(i)+0.50*float(j)
		a[i,j,1] = float(j)*math.sqrt(3.0)*0.5


(po_sin,dis_sin,num_sin)=num_cir(2,1000)
(po_sin,dis_sin,num_sin)=sortall(po_sin,dis_sin,num_sin)
print len(dis_sin)
print num_sin




