#coding=utf-8
import math
import random as random1
import sys
import time

def po_sele(sel):
	'''随机选取原子位置'''
	sele_num=[]
	sele_po=[]
	while (len(sele_num) < sel):
		sele_num.append(random1.choice(a_cen))
		sele_num = list(set(sele_num))

	for i in sele_num:
		sele_po.extend([i+3*n**2*i+n*jj for ii in [-1,0,1] for jj in [-1,0,1]])
		sele_po_cen.append(i)
	unsele_num=a_cen - set(sele_num)
	return(set(sele_po),set(sele_num),unsele_num)

def distan(i,sele_po):
	'''计算所选原子与周围的距离的分类个数，并计算能量'''
	dis_1=set([i+1,i-1,i+3*n,i-3*n,i+3*n-1,i-3*n+1])
	dis_3=set([i+3*n+1,i+6*n-1,i+3*n-2,i-3*n-1,i-6*n+1,i-3*n+2])
	dis_4=set([i+2,i+6*n,i+6*n-2,i-2,i-6*n,i-6*n+2])
	dis_7=set([i-3*n+3,i+3*n+3,i+6*n+1,i+9*n-1,i+9*n-2,i+6*n-3,i+3*n-3,i-3*n-2,i-6*n-1,i-9*n+1,n-9*n+2,n-6*n+3])
	dis_9=set([i-9*n,i-9*n+3,i+3,i+9*n,i+9*n-3,i-3])
	num_1=len(dis_1 & sele_po)
	num_3=len(dis_3 & sele_po)
	num_4=len(dis_4 & sele_po)
	num_7=len(dis_7 & sele_po)
	num_9=len(dis_9 & sele_po)
	energy=num_1*for_fie[0] + num_3*for_fie[1] + num_4*for_fie[2] + num_7*for_fie[3] + num_9*for_fie[4]
	return energy/2.

def repo_sele(sele_po,sele_num,unsele_num):
	a=sele_num.pop()
	b=unsele_num.pop()
	sele_num.add(b)
	unsele_num.add(a)
	for ii in [-1,0,1]:
		for jj in [-1,0,1]:
			sele_po.remove(a+3*n**2*i+n*jj)
			sele_po.add(b+3*n**2*i+n*jj)
	energy = sum(map(distan,sele_num))
	return(energy,sele_po,sele_num,unsele_num)



def  b_z(num,sele_po,sele_num,unsele_num):
	(energy,sele_po,sele_num,unsele_num)=repo_sele(sele_po,sele_num,unsele_num)
	(energy1,sele_po1,sele_num1,unsele_num1)=repo_sele(sele_po,sele_num,unsele_num)
	prob=math.exp((energy-energy1)/kt)
	i=0
	while (i<num):

		if prob > random1.uniform(0,1) :
			txt.write(str(energy1)+"\n")
			energy,sele_po,sele_num,unsele_num=energy1,sele_po1,sele_num1,unsele_num1
		else:
			txt.write(str(energy)+"\n")
			#energy,sele_num=energy,sele_num
		energy1,sele_num1=re_po_sele(sele_num)
		prob=math.exp((energy-energy1)/kt)
		i=i+1
		progress_bar(i,num)

def progress_bar(i,l):
	done = "#" * int((i+1)*25/l)
	undone = " " * int(25-len(done))
	percent = (i+1)*100/l
	sys.stdout.write("\r["+done+undone+"]   ("+str(percent)+"%"+')')
	sys.stdout.flush()


n=4
sel=3
for_fie=range(5)
#a={str(i*3*n+j):complex(i+j*0.5,(j*1.732058*0.5)) for j in range(3*n) for i in range(3*n)}
a_cen=set([3*n**2+n+3*n*i+j  for j in range(n) for i in range(n)])
txt=open(str(sel)+"_in_"+str(n)+"_lj","a")
(sele_po2,sele_num2,unsele_num2)=po_sele(sel)

b_z(1000,sele_po2,sele_num2,unsele_num2)

#print a_cen
#print round(abs(a['6']-a['2']),3)