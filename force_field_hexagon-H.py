#coding=utf-8
import math
import random as random1
import sys
import time

def po_sele(seq,sel):
	'''随机选取原子位置'''
	sele_num=[]
	sele_po=[]
	sele_po_cen=[]
	while (len(sele_num) < sel):
		sele_num.append(random1.choice(seq))
		sele_num = list(set(sele_num))

	for i in sele_num:
		sele_po.extend([(i/n+n*ii)*3*n+i%n+n*jj for ii in [0,1,2] for jj in [0,1,2]])
		sele_po_cen.append((i/n+n)*3*n+i%n+n)
	return(sele_po,sele_num,sele_po_cen)



def hex_en(po,sele_po):
	'''用拟合关系计算一个原子的能量'''
	ii=3*n**2+n+po
	hexagon=[ii+1,ii-1,ii-3*n,ii+3*n,ii-3*n+1,ii+3*n-1]
	hex_po=[]
	dis_hex_po=[]
	hex_po=[i for i in hexagon if i in sele_po]
	len_hex_po = len(hex_po)
	#print len_hex_po

	if len_hex_po ==0 :
		return force_field[0]
	elif len_hex_po ==1 :
		return force_field[1]
	elif len_hex_po ==5 :
		return force_field[11]
	elif len_hex_po ==6 :
		return force_field[12]

	if len_hex_po == 2:
		return force_field[2]

	if len_hex_po == 3:
		return force_field[5]

	if len_hex_po == 4:
		return force_field[8]

def re_po_sele(sele_num):
	'''改变一个原子位置 计算能量'''
	b=sele_num[0]
	while (b in sele_num):
		b=random1.randint(0, n**2-1)
	sele_num.pop(random1.randint(0, sel-1))
	sele_num.append(b)

	sele_po,sele_po_cen=[],[]
	for i in sele_num:
		sele_po.extend([(i/n+n*ii)*3*n+i%n+n*jj for ii in [0,1,2] for jj in [0,1,2]])
	#print sorted(sele_po)
	energy=0
	for i in sele_num :
		energy=energy+hex_en(i,sele_po)
	return(energy,sele_num)

def  b_z(num,sele_num):
	(energy,sele_num)=re_po_sele(sele_num)
	(energy1,sele_num1)=re_po_sele(sele_num)
	prob=math.exp((energy-energy1)/kt)
	i=0
	while (i<num):
		#print prob
		if prob > random1.uniform(0,1) :
			txt.write(str(energy1)+"\n")
			#txt.write(str(energy1)+"   "+str(prob)+"   "+str(energy-energy1)+"\n")
			energy,sele_num=energy1,sele_num1
		else:
			#txt.write(str(energy)+"   "+str(prob)+"   "+str(energy-energy1)+"\n")
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


n=10
sel=50
kt=0.025875
force_field=[16.6281702163307,16.6380409802590,
16.6349199937773,16.6349199937773,16.6349199937773,
16.6423247724106,16.6423247724106,16.6423247724106,
16.6555505593623,16.6555505593623,16.6555505593623,
16.6521621547575,16.6583097332316]
txt=open(str(sel)+"_in_"+str(n)+"_2","a")
(sele_po2,sele_num2,sele_po_cen2)=po_sele(range(n**2),sel)


t0=time.time()
b_z(100000,sele_num2)
t1=time.time()
print t1-t0


