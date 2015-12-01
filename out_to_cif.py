#coding=utf-8
import re
f=open(r"C:\Users\dcc\Desktop\1122.txt",'r')
n = -1
f=f.readlines()
while True :
	if  f[n][0:6] == "ATOMIC_" :
		brake
	#b=re.match(r'(\w{1,2}\d{1,3}\s+)(\w{1,2}\s+\d.\d{4}\s+\d.\d{4}\s+\d.\d{4})(\s+)(.*)',eachline)
	b=re.split(r'\s+',f[n])
	if len(b) > 6 and len(b[1]) > 10 and b[1][0] == "0":
		a=open(r"C:\Users\dcc\Desktop\out_to_cif.txt",'a')  #参数a表示追加写入
		d=str(n)
		c=b[0]+d+"    "+b[0]+"    "+b[1]+"    "+b[2]+"    "+b[3]+"   0.00000  Uiso   1.00"+"\n"
		n = n - 1
		a.write(c)
		print c
		a.close()