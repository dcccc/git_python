#coding=utf-8
import math
import random as random1
import sys
import numpy as np

def to_po(num):
	'''将随机选取的序数变为坐标'''
	po=[]
	po_cen=[]
	for i in range(3):
		for j in range(3):
			po.append([num/n+n*i,num%n+n*j])
	po_cen.append([num/n+n*1,num%n+n*1])
	return(po,po_cen)

def po_sele(seq,sel):
	'''随机选取原子位置'''
	sele_num=[]
	sele_po=[]
	sel_po_cen=[]
	while (len(sele_num) < sel):
		sele_num.append(random1.choice(seq))
		sele_num = list(set(sele_num))

	for i in sele_num:
		(po,po_cen)=to_po(i)
		sele_po.extend(po)
		sel_po_cen.extend(po_cen)
	return(sele_po,sele_num,sel_po_cen)





def hex_en(po,sele_po):
	'''用拟合关系计算一个原子的能量'''
	x,y=po[0],po[1]
	hexagon=[[x,y-1],[x+1,y-1],[x+1,y],[x,y+1],[x-1,y+1],[x-1,y]]
	hex_po=[]
	dis_hex_po=[]
	for i in hexagon :
		if i in sele_po :
			hex_po.append(i)
	len_hex_po = len(hex_po)

	if len_hex_po ==0 :
		return force_field[0]
	elif len_hex_po ==1 :
		return force_field[1]
	elif len_hex_po ==5 :
		return force_field[11]
	elif len_hex_po ==6 :
		return force_field[12]
	else :
		for i in hex_po :
			for j in hex_po :
				dis=np.sum((a[i[0],i[1],]-a[j[0],j[1],])**2)
				dis_hex_po.append(round(dis,0))
	diff_13 = dis_hex_po.count(1)-dis_hex_po.count(3)
	dis_hex_po = sorted(set(dis_hex_po))
	if len_hex_po == 2:
		if dis_hex_po == [0.0, 1.0] :
			return force_field[2]
		elif dis_hex_po == [0.0, 3.0] :
			return force_field[3]
		elif dis_hex_po == [0.0, 4.0] :
			return force_field[4]

	if len_hex_po == 3:
		if dis_hex_po == [0.0, 1.0, 3.0] :  #连
			return force_field[5]
		elif dis_hex_po == [0.0, 1.0, 3.0, 4.0]: #偏
			return force_field[6]
		elif dis_hex_po == [0.0, 3.0] : #均
			return force_field[7]

	if len_hex_po == 4:
		if diff_13 == 2 :
			return force_field[8]
		elif diff_13 == -2:
			return force_field[9]
		elif diff_13 == 0:
			return force_field[10]

def re_po_sele(sele_num):
	'''改变一个原子位置 计算能量'''
	b=sele_num[0]
	while (b in sele_num):
		b=random1.choice(range(n**2))
	sele_num.pop(random1.choice(range(sel)))
	sele_num.append(b)

	sel_po,sel_po_cen=[],[]
	for i in sele_num:
		(po,po_cen)=to_po(i)
		sele_po.extend(po)
		sel_po_cen.extend(po_cen)
	#return(sele_po,sele_num,sel_po_cen)
	energy=0
	for i in sele_po_cen :
		energy=energy+hex_en(i,sele_po)
	return(energy,sele_num)




n=3
sel=5
force_field=range(13)
a = np.linspace(0,0,2*(n*3)**2).reshape(n*3,n*3,2)
a.dtype=np.float64
#print a.shape
for i in range(n*3):
	for j in range(n*3):
		a[i,j,0] = i+0.50*j
		a[i,j,1] = j*math.sqrt(3.0)*0.5

#(dis_prim,dis_suro)=distan(sel)
#dis_num=dis_num(dis_prim,dis_suro)

#print dis_num


#print energy([0,1,2])

#print len(dis_suro)
#print len(dis_prim)



#b=[[i,j] for i in range(n-1,2*n+1) for j in range(n-1,2*n+1)]

#(sele_po,sele_num,sel_po_cen)=po_sele(range(n**2),sel)

#print sel_po_cen



(sele_po,sele_num,sele_po_cen)=po_sele(range(n**2),sel)
print  hex_en([3,3],sele_po)
print  sele_num

(energy,sele_num)=re_po_sele(sele_num)

print  sele_num

(energy,sele_num)=re_po_sele(sele_num)

print  sele_num






