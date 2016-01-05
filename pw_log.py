#coding:utf-8
import os
import re
import glob
import sys
import linecache
import time

pw=sorted(os.popen("top -b -n 1 | grep pw.x").readlines())
for line in pw:
	line_sp = re.split(r"\s+",line.rstrip().lstrip())
	print line_sp[1]

