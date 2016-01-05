#coding:utf-8
import os
import re
import glob
import sys
import linecache
import time

def progress_bar(i,l):
	done = "#" * int((i+1)*25/l)
	undone = " " * int(25-len(done))
	percent = (i+1)*100/l
	sys.stdout.write("\r["+done+undone+"]   ("+str(x)+"%"+')')
	sys.stdout.flush()

for i in range(100):
	time.sleep(0.08)
	progress_bar(i,100)
