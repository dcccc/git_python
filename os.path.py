#coding:utf-8
import re
import os
import urllib
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

#os.chdir(r"E:\\")
b = "测试".decode("utf-8")
os.mkdir(b)
a = os.getcwd()
os.chdir(os.path.join(a,b))
print os.getcwd()
f = open(b+".txt","a")
f.write(b)
f.close()