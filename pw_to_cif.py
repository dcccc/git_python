#coding=utf-8
import re
f=open(r"C:\Users\dcc\Desktop\1111",'r')

n = 1
for eachline in f:
	#b=re.match(r'(\w{1,2}\d{1,3}\s+)(\w{1,2}\s+\d.\d{4}\s+\d.\d{4}\s+\d.\d{4})(\s+)(.*)',eachline)
	b=re.split(r'\s+',eachline)
	if len(b) > 4 and len(b[2]) > 6 and len(b[1]) > 6:
		a=open(r"C:\Users\dcc\Desktop\pw_to_cif.txt",'a')  #参数a表示追加写入
		d=str(n)
		c=b[0]+d+"    "+b[0]+"    "+b[1]+"    "+b[2]+"    "+b[3]+"   0.00000  Uiso   1.00"+"\n"
		n=n+1
		#print c
		a.write(c)
		#print c
		a.close()
