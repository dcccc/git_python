#coding:utf-8
#import sys
#reload(sys)
#sys.setdefaultencoding("utf-8")  #设置默认编码为utf-8
f=open(r"C:\Users\dcc\Desktop\yaogun\yiwcineis.lrc",'r')  #路径前面的r表示windows绝对路径，字符串不对\进行转移
for eachline in f:
	a=open(r"C:\Users\dcc\Desktop\12",'a')  #参数a表示追加写入
	a.write(eachline)
	a.close()