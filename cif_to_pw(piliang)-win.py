#coding:utf-8
import os
import re
import glob
import string
import math
import sys

if len(sys.argv) < 3  :
	print "          Usage\n          python cif_to_pw(piliang)-2.py n   ciffiles or all\n          n is the number of the nonmovale atom\n          all    --all the xx.cif in current directory  will be converted"
	sys.exit()
elif len(sys.argv) == 3 and sys.argv[2] == "all":
	os.chdir(os.getcwd())
	a = glob.glob("*.cif")
elif len(sys.argv) >= 3 and sys.argv[2] != "all":
	a = sys.argv[2:]
else :
	sys.exit()


n = int(sys.argv[1])

if len(a) == 0 :
	print "there is no file to be converted"



def cif_to_pw(cif):
	if not os.path.isfile(cif) :
		print cif + " doesn\'t exist"
	else :	
		z = 1
		a=[]
		f=open(cif,'r')
		txt = cif.replace("cif","txt")
		h=open(txt,'a')

		for eachline in f:
		#b=re.match(r'(\w{1,2}\d{1,3}\s+)(\w{1,2}\s+\d.\d{4}\s+\d.\d{4}\s+\d.\d{4})(\s+)(.*)',eachline)
			b=re.split(r'[\s]+',eachline)
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
		a_=round(a_,8)
		b_=math.cos(float(b_)/180*math.pi)
		b_=round(b_,8)
		c_=math.cos(float(c_)/180*math.pi)
		c_=round(c_,8)
	
		i="                   celldm(1) = " + str(A) + " ," + '\n'
		h.write(i)
		i="                   celldm(2) = " + str(B) + " ," + '\n'
		h.write(i)
		i="                   celldm(3) = " + str(C) + " ," + '\n'
		h.write(i)
		i="                   celldm(4) = " + str(a_) + " ," + '\n'
		h.write(i)
		i="                   celldm(5) = " + str(b_) + " ," + '\n'
		h.write(i)
		i="                   celldm(6) = " + str(c_) + " ," + '\n'
		h.write(i)

		a = sorted(a,key = lambda x : float(re.split(r'\s+',x)[3]) )
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



for i in a:
	cif_to_pw(i)