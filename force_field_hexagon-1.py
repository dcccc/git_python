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
		sele_num.append(random1.choice(list(a_cen)))
		sele_num = list(set(sele_num))

	for i in sele_num:
		sele_po.extend([i+3*n**2*ii+n*jj for ii in [-1,0,1] for jj in [-1,0,1]])
	unsele_num=a_cen - set(sele_num)
	return(set(sele_po),set(sele_num),set(unsele_num))

def distan(i,sele_po):
	'''计算所选原子与周围的距离的分类个数，并计算能量'''
	dis=set([i+1,i-1,i+3*n,i-3*n,i+3*n-1,i-3*n+1])
	len_hex_po=len(dis & sele_po)
	if len_hex_po ==0 :
		return force_field[0]
	elif len_hex_po ==1 :
		return force_field[1]
	elif len_hex_po ==5 :
		return force_field[11]
	elif len_hex_po ==6 :
		return force_field[12]

	elif len_hex_po == 2:
		return force_field[2]
	elif len_hex_po == 3:
		return force_field[5]
	elif len_hex_po == 4:
		return force_field[8]


def repo_sele(sele_po,sele_num,unsele_num):
	a=random1.choice(list(sele_num))
	b=random1.choice(list(unsele_num))
	sele_num.remove(a)
	unsele_num.remove(b)
	sele_num.add(b)
	unsele_num.add(a)
	for ii in [-1,0,1]:
		for jj in [-1,0,1]:
			sele_po.remove(a+3*n**2*ii+n*jj)
			sele_po.add(b+3*n**2*ii+n*jj)
	energy = 0
	for i in sele_num :
		energy=distan(i,sele_po)+energy
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
		(energy1,sele_po1,sele_num1,unsele_num1)=repo_sele(sele_po,sele_num,unsele_num)
		prob=math.exp((energy-energy1)/kt)
		i=i+1
		progress_bar(i,num)

def progress_bar(i,l):
	done = "#" * int((i+1)*25/l)
	undone = " " * int(25-len(done))
	percent = (i+1)*100/l
	sys.stdout.write("\r["+done+undone+"]   ("+str(percent)+"%"+')')
	sys.stdout.flush()


n=10
sel=50
kt=0.025875
force_field=[16.6281702163307,16.6380409802590,
16.6349199937773,16.6349199937773,16.6349199937773,
16.6423247724106,16.6423247724106,16.6423247724106,
16.6555505593623,16.6555505593623,16.6555505593623,
16.6521621547575,16.6583097332316]
#a={str(i*3*n+j):complex(i+j*0.5,(j*1.732058*0.5)) for j in range(3*n) for i in range(3*n)}
a_cen=set([3*n**2+n+3*n*i+j  for j in range(n) for i in range(n)])
txt=open(str(sel)+"_in_"+str(n)+"_lj","a")
(sele_po2,sele_num2,unsele_num2)=po_sele(sel)

t0=time.time()
b_z(1000000,sele_po2,sele_num2,unsele_num2)
t1=time.time()
print t1-t0
