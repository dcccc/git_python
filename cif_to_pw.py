#coding=utf-8
import re
import string
import math
n = 24
z = 1
a=[]
f=open(r"C:\Users\dcc\Desktop\1111",'r')  #路径前面的r表示windows绝对路径，字符串不对\进行转移
h=open(r"C:\Users\dcc\Desktop\cif_to_pw.txt",'a')
for eachline in f:
	#b=re.match(r'(\w{1,2}\d{1,3}\s+)(\w{1,2}\s+\d.\d{4}\s+\d.\d{4}\s+\d.\d{4})(\s+)(.*)',eachline)
	b=re.split(r'[\s\-]+',eachline)
	if len(b) > 6 :
		#a=open(r"C:\Users\dcc\Desktop\tmp",'a')  #参数a表示追加写入
		c=b[1]+"	"+b[2]+"	"+b[3]+"	"+b[4]
		a.append(c)
	elif b[0]=="_cell_length_a" :
		A=float(b[1])
	elif b[0]=="_cell_length_b" :
		B=float(b[1])	
	elif b[0]=="_cell_length_c" :
		C=float(b[1])
	elif b[0]=="_cell_angle_alpha" :
		a_=float(b[1])
	elif b[0]=="_cell_angle_beta" :
		b_=float(b[1])
	elif b[0]=="_cell_angle_gamma" :
		c_=float(b[1])

B=float(B) / float(A)
C=float(C) / float(A)
A=float(A) / 0.5291772
a_=math.cos(float(a_)/180*math.pi)
b_=math.cos(float(b_)/180*math.pi)
c_=math.cos(float(c_)/180*math.pi)
	
i="                   celldm(1) = " + str(A) + '\n'
h.write(i)
i="                   celldm(2) = " + str(B) + '\n'
h.write(i)
i="                   celldm(3) = " + str(C) + '\n'
h.write(i)
i="                   celldm(4) = " + str(a_) + '\n'
h.write(i)
i="                   celldm(5) = " + str(b_) + '\n'
h.write(i)
i="                   celldm(6) = " + str(c_) + '\n'
h.write(i)

"""
x=re.split(r'\s+',a[1])
y=len(x[1])
c=5+2*y
d , e=c+2 , y+c-3
a = sorted(a,key = lambda x : string.atoi(x[d:e]) )
for b in a:
	if z < n + 1 :
		i = b + '    0   0   0' + '\n'
		# h.write(i)
		# h.write("    0   0   0\n")
	else :
		#pass
		i = b + '\n'
		#h.write(i)
	z = z + 1
	#print i
	h.write(i)
h.close()
"""


a = sorted(a,key = lambda x : re.split(r'\s+',x)[3] )
for b in a:
	if z < n + 1 :
		i = b + '    0   0   0' + '\n'
		# h.write(i)
		# h.write("    0   0   0\n")
	else :
		#pass
		i = b + '\n'
		#h.write(i)
	z = z + 1
	#print i
	h.write(i)
h.close()