#coding:utf-8
import sys
reload(sys)
sys.setdefaultencoding("utf-8")    #指明默认解码方式为utf-8
f = open("C:\Users\dcc\Desktop\yaogun\yiwcineis.lrc",'r')
for el in f:   #读取文件的每一行
	print el.strip()    # strip  去掉开头结尾处的空格