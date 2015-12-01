#coding:utf-8
import os
import re
import glob
import ciftopw

os.chdir("C:\Users\dcc\Desktop")
a=glob.glob("*.cif")

print a[0].replace("cif","txt")

for i in a:
	ciftopw.cif_to_pw(i)