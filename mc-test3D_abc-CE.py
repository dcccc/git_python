#coding=utf-8
import math
import random
import sys
import time
import numpy as np
import copy
#from PIL import Image
#import matplotlib.pyplot as plt

def po_sele(sel):
	'''随机选取原子位置'''
	all_po=[[i,j,k]for i in xrange(a) for j in xrange(b) for k in xrange(c)]
	sele_po=random.sample(all_po,sel)
	all_po_sigma=np.ones((a,b,c))
	for i in sele_po:
		all_po_sigma[tuple(i)] = -1
	unsele_po = filter(lambda x : x not in sele_po, all_po)
	all_po_sigma = -1*all_po_sigma
	return(all_po_sigma,sele_po,unsele_po)

def period(i,all_po_sigma,mode=1):
	'''周期性边界'''
	x,y,z=i[0],i[1],i[2]
	if x > a-1:
		x=x-a
	if x < 0:
		x=x+a
	if y > b-1:
		y=y-b
	if y < 0:
		y=y+b
	if z < 0:
		z=z+c
	if z > c-1:
		z=z-c
	if mode==1: 
		return([x,y,z])
	elif mode==2:
		return all_po_sigma[x,y,z]


def distan_forcefield(i,all_po_sigma):
	'''计算所选原子与周围的距离的分类个数，并计算能量'''
	x,y,z=i[0],i[1],i[2]
	i_sigma=all_po_sigma[tuple(i)]

	dis_9 =map(lambda x: period(x,all_po_sigma,2), [[x,y+1,z],[x,y+1,z+1],[x,y-1,z],[x,y-1,z+1]])
	dis_10=map(lambda x: period(x,all_po_sigma,2), [[x+1,y+1,z],[x+1,y+1,z+1],[x+1,y-1,z],[x+1,y-1,z+1],
													[x-1,y+1,z],[x-1,y+1,z+1],[x-1,y-1,z],[x-1,y-1,z+1]])
	dis_11=map(lambda x: period(x,all_po_sigma,2), [[x+2,y+1,z],[x+2,y+1,z+1],[x+2,y-1,z],[x+2,y-1,z+1],
													[x-2,y+1,z],[x-2,y+1,z+1],[x-2,y-1,z],[x-2,y-1,z+1]])
	dis_3 =map(lambda x: period(x,all_po_sigma,2), [[x+2,y,z],[x-2,y,z]])
	dis_2 =map(lambda x: period(x,all_po_sigma,2), [[x+1,y,z],[x-1,y,z]])
	dis_7 =map(lambda x: period(x,all_po_sigma,2), [[x+2,y,z+1],[x+2,y,z-1],[x-2,y,z+1],[x-2,y,z-1]])
	dis_6 =map(lambda x: period(x,all_po_sigma,2), [[x+1,y,z+1],[x+1,y,z-1],[x-1,y,z+1],[x-1,y,z-1]])
	dis_5 =map(lambda x: period(x,all_po_sigma,2), [[x,y,z+1],[x,y,z-1]])

	num1=[0,0,sum(dis_9),sum(dis_10),sum(dis_11),sum(dis_3),sum(dis_2),sum(dis_7),sum(dis_6),sum(dis_5)]


	#================================================================

	num=0
	for ii in xrange(2):
		num += dis_3[ii]*dis_2[ii]
	num1.append(num )     #三体2-3

	num=0
	for ii in xrange(2):
		num += dis_2[ii]*(dis_5[0]+dis_5[1])
	num1.append(num )     #三体2-5

	num=0
	for ii in xrange(2):
		num += dis_2[ii]*(dis_6[2*ii]+dis_6[2*ii+1])
	num1.append(num )     #三体2-6

	num=0
	for ii in xrange(2):
		num += dis_2[ii]*(dis_7[2*ii]+dis_7[2*ii+1])
	num1.append(num )     #三体2-7

	num=0
	for ii in xrange(2):
		num += dis_3[ii]*(dis_5[0]+dis_5[1])
	num1.append(num )     #三体3-5

	num=0
	for ii in xrange(2):
		num += dis_3[ii]*(dis_6[2*ii]+dis_6[2*ii+1])
	num1.append(num )     #三体3-6

	num=0
	for ii in xrange(2):
		num += dis_3[ii]*(dis_7[2*ii]+dis_7[2*ii+1])
	num1.append(num )     #三体3-7

	num=0
	for ii in xrange(2):
		num += dis_5[ii]*(dis_6[ii]+dis_6[ii+2])
	num1.append(num )     #三体5-6

	num=0
	for ii in xrange(2):
		num += dis_5[ii]*(dis_7[ii+2]+dis_7[ii])
	num1.append(num )     #三体5-7

	num=0
	for ii in xrange(4):
		num += dis_6[ii]*dis_7[ii]
	num1.append(num )     #三体6-7


	#----


	num=0
	for ii in xrange(4):
		num += dis_9[ii]*(dis_10[ii]+dis_10[2+ii])
	num1.append(num )     #三体9-10(13-14)

	num=0
	for ii in xrange(4):
		num += dis_9[ii]*(dis_11[ii]+dis_11[2+ii])
	num1.append(num )     #三体9-11(13-15)

	num=0
	for ii in xrange(2):
		num += dis_9[2*ii]*dis_9[2*ii+1]
	num1.append(num )     #三体9-13

	num=0
	for ii in xrange(2):
		num += dis_9[2*ii]*(dis_10[4*ii+3]+dis_10[4*ii+1])+dis_9[2*ii+1]*(dis_10[4*ii]+dis_10[4*ii+2])
	num1.append(num )     #三体9-14(10-13)

	num=0
	for ii in xrange(2):
		num += dis_9[2*ii+1]*(dis_11[4*ii+3]+dis_11[4*ii+1])+dis_9[2*ii]*(dis_11[4*ii]+dis_11[4*ii+2])
	num1.append(num )     #三体9-15(11-13)


	num=0
	for ii in xrange(8):
		num += dis_10[ii]*dis_11[ii]
	num1.append(num )     #三体10-11(14-15)

	num=0
	for ii in xrange(4):
		num += dis_10[2*ii]*dis_10[2*ii+1]
	num1.append(num )     #三体10-14

	num=0
	for ii in xrange(4):
		num += dis_10[2*ii]*dis_11[2*ii+1]+dis_11[2*ii]*dis_10[2*ii+1]
	num1.append(num )     #三体10-15(14-11)

	num=0
	for ii in xrange(4):
		num += dis_11[2*ii]*dis_11[2*ii+1]
	num1.append(num )     #三体11-15


	#----
 	num = sum(dis_9)*sum(dis_2)
	num1.append(num )     #三体2-9

 	num = sum(dis_9)*sum(dis_3)
	num1.append(num )     #三体3-9

	num = dis_5[0]*(dis_9[0]+dis_9[2])+dis_5[1]*(dis_9[1]+dis_9[3])
	num1.append(num )     #三体5-9

 	num += (dis_9[0]+dis_9[2])*(dis_6[0]+dis_6[2])+(dis_9[1]+dis_9[3])*(dis_6[1]+dis_6[3])
	num1.append(num )     #三体6-9	

 	num += (dis_9[0]+dis_9[2])*(dis_7[0]+dis_7[2])+(dis_9[1]+dis_9[3])*(dis_7[1]+dis_7[3])
	num1.append(num )     #三体7-9

#=====fine

 	num = sum(dis_10[:4])*dis_2[0]+sum(dis_10[4:])*dis_2[1]
	num1.append(num )     #三体2-10

 	num = sum(dis_10[:4])*dis_3[0]+sum(dis_10[4:])*dis_3[1]
	num1.append(num )     #三体3-10

	num=0
	for ii in xrange(2):
		num+= dis_5[ii]*(dis_10[ii+1]+dis_10[ii+2]+dis_10[ii+4]+dis_10[ii+6])
	num1.append(num )     #三体5-10

	num = dis_6[0]*(dis_10[0]+dis_10[2])+dis_6[1]*(dis_10[1]+dis_10[3])+dis_6[2]*(dis_10[4]+dis_10[6])+dis_6[3]*(dis_10[5]+dis_10[7])
	num1.append(num )     #三体6-10

	num = dis_7[0]*(dis_10[0]+dis_10[2])+dis_7[1]*(dis_10[1]+dis_10[3])+dis_7[2]*(dis_10[4]+dis_10[6])+dis_7[3]*(dis_10[5]+dis_10[7])
	num1.append(num )     #三体7-10




 	num = sum(dis_11[:4])*dis_2[0]+sum(dis_11[4:])*dis_2[1]
	num1.append(num )     #三体2-11

 	num = sum(dis_11[:4])*dis_3[0]+sum(dis_11[4:])*dis_3[1]
	num1.append(num )     #三体3-11

	num=0
	for ii in xrange(2):
		num+= dis_5[ii]*(dis_11[ii+1]+dis_11[ii+2]+dis_11[ii+4]+dis_11[ii+6])
	num1.append(num )     #三体5-11

	num = dis_6[0]*(dis_11[0]+dis_11[2])+dis_6[1]*(dis_11[1]+dis_11[3])+dis_6[2]*(dis_11[4]+dis_11[6])+dis_6[3]*(dis_11[5]+dis_11[7])
	num1.append(num )     #三体6-11

	num = dis_7[0]*(dis_11[0]+dis_11[2])+dis_7[1]*(dis_11[1]+dis_11[3])+dis_7[2]*(dis_11[4]+dis_11[6])+dis_7[3]*(dis_11[5]+dis_11[7])
	num1.append(num )     #三体7-11




	num=dis_5[0]*(dis_9[1]+dis_9[3])+dis_5[1]*(dis_9[0]+dis_9[2])
	num1.append(num )     #三体5-13

	num=dis_5[0]*(dis_10[1]+dis_10[3]+dis_10[5]+dis_10[7])+dis_5[1]*(dis_10[0]+dis_10[2]+dis_10[4]+dis_10[6])
	num1.append(num )     #三体5-14

	num=dis_5[0]*(dis_11[1]+dis_11[3]+dis_11[5]+dis_11[7])+dis_5[1]*(dis_11[0]+dis_11[2]+dis_11[4]+dis_11[6])
	num1.append(num )     #三体5-15

	num=(dis_6[0]+dis_6[2])*(dis_9[1]+dis_9[3])+(dis_6[1]+dis_6[3])*(dis_9[0]+dis_9[2])
	num1.append(num )     #三体6-13

	num=0
	for ii in xrange(2):
		num=dis_6[ii*2]*(dis_10[ii*4+1]+dis_10[ii*4+3])+dis_6[ii*2+1]*(dis_10[ii*4]+dis_10[ii*4+2])
	num1.append(num )     #三体6-14

	num=0
	for ii in xrange(2):
		num=dis_6[ii*2]*(dis_11[ii*4+1]+dis_11[ii*4+3])+dis_6[ii*2+1]*(dis_11[ii*4]+dis_11[ii*4+2])
	num1.append(num )     #三体6-15


	num=(dis_7[0]+dis_7[2])*(dis_9[1]+dis_9[3])+(dis_7[1]+dis_7[3])*(dis_9[0]+dis_9[2])
	num1.append(num )     #三体7-13

	num=0
	for ii in xrange(2):
		num=dis_7[ii*2]*(dis_10[ii*4+1]+dis_10[ii*4+3])+dis_7[ii*2+1]*(dis_10[ii*4]+dis_10[ii*4+2])
	num1.append(num )     #三体7-14

	num=0
	for ii in xrange(2):
		num=dis_7[ii*2]*(dis_11[ii*4+1]+dis_11[ii*4+3])+dis_7[ii*2+1]*(dis_11[ii*4]+dis_11[ii*4+2])
	num1.append(num )     #三体7-15



	return np.array(num1)*i_sigma



def repo_sele(sel,sele_po,unsele_po,all_po_sigma):
	a_po=random.chioce(sele_po,1)
	b_po=random.chioce(unsele_po,1)

	sele_po.remove(a_po)
	unsele_po.remove(b_po)
	sele_po.append(b_po)
	unsele_po.append(a_po)

	all_po_sigma[tuple(b_po)]=1
	all_po_sigma[tuple(a_po)]=-1

	force_para=np.array([0.]*20)
	force_para[0]=a*b*c-sel
	force_para[1]=sel
	for i in [(i,j,k) for i in xrange(a) for j in xrange(b) for k in xrange(c)]:
		force_para +=distan_forcefield(i,all_po_sigma)
	energy = np.sum(force_para * force_field)
	return(energy,sele_po,unsele_po,all_po_sigma)


def  b_z_mp(num,sel,sele_po,unsele_po,all_po_sigma,txt):
	file_out=open(txt+"mp_ce","a")
	(energy,sele_po,unsele_po,all_po_sigma)=repo_sele(sel,sele_po,unsele_po,all_po_sigma)
	(energy1,sele_po1,unsele_po1,all_po_sigma1)=repo_sele(sel,sele_po,unsele_po,all_po_sigma)
	prob=math.exp((energy-energy1)/kt)
	i=0
	while (i<num):

		if prob > random.uniform(0,1) :
			file_out.write(str(energy1)+"\n")
			energy,sele_po,unsele_po,all_po_sigma=energy1,sele_po1,unsele_po1,all_po_sigma1
		else:
			file_out.write(str(energy)+"\n")		
		(energy1,sele_po1,unsele_po1,all_po_sigma1)=repo_sele(sel,sele_po,unsele_po,copy.deepcopy(all_po_sigma))
		#print energy-energy1
		prob=math.exp((energy-energy1)/kt)
		i=i+1
		#progress_bar(i,num)


def  b_z_random(num,sel,sele_po,unsele_po,all_po_sigma,txt):
	file_out=open(txt+"random_ce","a")
	(energy,sele_po,unsele_po,all_po_sigma)=repo_sele(sel,sele_po,unsele_po,all_po_sigma)
	i=0
	while (i<num):
		file_out.write(str(energy)+"\n")	
		(energy, all_po_sigma)=repo_sele(sel,all_po_sigma)
		i=i+1
		#progress_bar(i,num)


def progress_bar(i,l):
	done = "#" * int((i+1)*25/l)
	undone = " " * int(25-len(done))
	percent = (i+1)*100/l
	sys.stdout.write("\r["+done+undone+"]   ("+str(percent)+"%"+')')
	sys.stdout.flush()



def mp(sel,num):
	#a={str(i*3*n+j):complex(i+j*0.5,(j*1.732058*0.5)) for j in range(3*n) for i in range(3*n)}
	txt=str(sel)+"_in_"+str(n)
	(all_po_sigma,sele_po,unsele_po)=po_sele(sel)
	b_z_random(num,sel,sele_po,unsele_po,all_po_sigma,txt)
	b_z_mp(num,sel,sele_po,unsele_po,all_po_sigma,txt)



def forcefield(pos):
	for ij in pos:
		all_po_sigma=np.ones((a,b,c))
		force_para=np.array([0.]*53)
		#sele_po =[]
		for i in ij:
			all_po_sigma[tuple(i)]=-1
		all_po_sigma = -all_po_sigma
		for j in [(i,j,k) for i in xrange(a) for j in xrange(b) for k in xrange(c)]:
			force_para += distan_forcefield(j,all_po_sigma)
		force_para[0]=a*b*c-len(ij)
		force_para[1]=len(ij)
		print force_para
	#return force_para_num
	



'''
n=10
sel=50
kt = 0.025875
for i in xrange(3,98):
	mp(i,100000)

'''

# n=10
# sel=50
# kt=0.025875
# force_field=np.array([9.06867490194993,-18.4296070148236,0.000508715828757346,0.00124968824221631,
# 0.000802320081522068,0.000126049459988894,0.000166323671886438,-0.000299337895779782,
# 4.83459657468065E-5,9.42118654267147E-5,-3.60455113084266E-5,-0.000209158433395017,
# -0.000100186555974229,-0.000167511992006336,0.000234475838043886,2.45377308699107E-5,
# -0.000108147090154928,-0.000209329823140104,0.000183262767845508,1.51447303822608])




#sele_po=po_sele(sel)
#to_pic(sele_po)
#forcefield(pos,3)

# for i in xrange(3,98):
# 	mp(i,500000)
# mp(50,100000)
#mp(50,100000)
pos=[[[0,0,0]],[[0,0,0],[1,0,0]],[[0,0,0],[2,0,0]],[[0,0,0],[0,0,1]],[[0,0,0],[1,0,1]],
[[0,0,0],[2,0,1]],[[0,0,0],[0,1,0]],[[0,0,0],[1,1,0]],[[0,0,0],[2,1,0]],
[[0,0,1],[2,1,0]],[[0,0,0],[1,0,0],[2,0,0]],[[0,1,0],[1,1,0],[0,1,1]],
[[0,1,0],[2,1,0],[0,1,1]],[[0,1,0],[2,1,0],[1,1,1]],[[0,0,0],[0,1,0],[1,1,0]],[[3,0,0],[0,1,0],[2,1,0]],
[[0,0,1],[0,1,0],[2,1,0]],[[0,1,0],[3,1,0],[2,0,1]],[[0,0,0],[0,1,0],[0,1,1]],[[1,0,0],[0,1,0],[0,1,1]],
[[0,0,0],[0,1,0],[1,1,1]],[[0,0,0],[0,1,0],[2,1,1]],[[2,0,0],[0,1,0],[3,1,1]],[[0,0,1],[0,1,0],[0,1,1]],
[[0,0,1],[0,1,0],[1,1,1]],[[2,0,1],[0,1,0],[1,1,1]],[[0,0,1],[0,1,0],[2,1,1]],[[1,0,1],[0,1,0],[3,1,1]],
[[0,1,0],[1,1,0],[2,1,0],[3,1,0]],[[0,1,0],[0,1,1],[2,1,0],[3,1,0]],
[[0,1,0],[1,1,0],[2,1,0],[3,0,0]],[[0,1,0],[1,1,0],[0,1,1],[1,1,1]],
[[1,0,0],[3,0,0],[0,1,0],[2,1,0]],[[0,1,0],[1,1,0],[1,0,1],[2,0,1]],
[[0,0,0],[0,1,0],[2,0,0],[2,1,1]],[[0,0,0],[2,1,0],[0,1,1],[3,1,1]],
[[0,0,0],[1,1,0],[0,1,1],[1,0,1]],[[0,0,0],[2,1,0],[0,1,1],[1,0,1]],
[[1,0,0],[1,1,0],[0,1,1],[1,1,1],[2,1,1]],[[0,0,0],[0,0,1],[0,1,0],[0,1,1],[1,1,0]],
[[0,0,0],[0,0,1],[0,1,0],[0,1,1],[2,1,0]],[[0,0,0],[1,0,1],[0,1,1],[1,1,0],[2,1,1]],
[[0,0,0],[1,0,1],[2,0,1],[0,1,1],[2,1,0]],[[0,0,1],[2,0,0],[3,0,1],[0,1,0],[2,1,1]],
[[0,0,0],[1,0,0],[0,1,0],[1,1,0],[0,1,1],[1,1,1]],
[[0,0,0],[0,0,1],[1,0,0],[0,1,0],[0,1,1],[1,1,1]],
[[0,0,1],[1,0,0],[2,0,1],[0,1,0],[1,1,1],[2,1,0]],
[[0,0,0],[0,0,1],[2,0,0],[1,1,1],[3,1,1],[3,1,0]],
[[0,0,0],[1,0,0],[2,0,0],[1,0,1],[1,1,1],[1,1,0]],
[[0,0,1],[2,0,0],[0,1,0],[1,1,1],[2,1,0],[3,1,0]],
[[0,0,0],[1,0,0],[2,0,0],[0,1,0],[1,1,0],[1,1,1],[2,1,1]],
[[0,0,0],[1,0,0],[0,0,1],[0,1,0],[1,1,0],[0,1,1],[1,1,1]],
[[0,0,1],[1,0,0],[2,0,0],[2,0,1],[0,1,0],[1,1,1],[2,1,0]],
[[0,0,0],[1,0,0],[2,0,0],[3,0,0],[0,0,1],[0,1,0],[1,1,1]],
[[0,0,0],[1,0,0],[2,0,0],[3,0,0],[1,0,1],[0,1,0],[2,1,1]],
[[0,0,0],[1,0,1],[2,0,0],[0,1,0],[1,1,1],[2,1,0],[3,1,0]],
[[1,0,0],[1,0,1],[2,0,0],[1,1,0],[0,1,1],[1,1,1],[2,1,1]],
[[0,0,0],[1,0,1],[2,0,0],[3,0,1],[0,1,1],[1,1,0],[2,1,1],[3,1,0]],
[[0,0,0],[1,0,0],[2,0,0],[3,0,0],[0,0,1],[1,0,1],[2,0,1],[3,0,1],[0,1,0],[1,1,0],[2,1,0],[3,1,0],[0,1,1],[1,1,1],[2,1,1]],
[[0,0,0],[1,0,0],[2,0,0],[3,0,0],[0,0,1],[1,0,1],[2,0,1],[3,0,1],[0,1,0],[1,1,0],[2,1,0],[3,1,0],[0,1,1],[1,1,1],[2,1,1],[3,1,1]]]



a,b,c=4,2,2
forcefield(pos)
