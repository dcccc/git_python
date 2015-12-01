#coding=utf-8
import re
import string
n = 16
z = 1
a=[]
f=open(r"C:\Users\dcc\Desktop\Pt(2).cif",'r')  #路径前面的r表示windows绝对路径，字符串不对\进行转移
for eachline in f:
	#b=re.match(r'(\w{1,2}\d{1,3}\s+)(\w{1,2}\s+\d.\d{4}\s+\d.\d{4}\s+\d.\d{4})(\s+)(.*)',eachline)
	b=re.split(r'\s+',eachline)
	if len(b) > 6 :
		#a=open(r"C:\Users\dcc\Desktop\tmp",'a')  #参数a表示追加写入
		c=b[1]+"	"+b[2]+"	"+b[3]+"	"+b[4]
		a.append(c)

a = sorted(a,key = lambda x : string.atoi(x[19])*100000+string.atoi(x[21:25]) )
h=open(r"C:\Users\dcc\Desktop\cif_to_pw.txt",'a')
for b in a:
	if z < n + 1 :
		i = b + '    0   0   0' + '\n'
		#h.write(i)
		#h.write("    0   0   0\n")
	else :
		#pass
		i = b + '\n'
		#h.write(i)
	z = z + 1
	print i
	h.write(i)