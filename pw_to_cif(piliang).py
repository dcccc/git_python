#coding:utf-8
import os
import re
import glob
import pwtocif

os.chdir("C:\Users\dcc\Desktop")
a=glob.glob("*.in")

print a[0].replace("in","txt")

#pwtocif.pw_to_cif(a[0])
for i in a:
	pwtocif.pw_to_cif(i)