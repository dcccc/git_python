#!/usr/bin/python
#coding:utf-8
import os
import re
import glob
import sys
import linecache
import time

def task_detail():
	print "-"*120
	print  "%-10s%-10s%-60s%s"  %("software", "user", "task neme", "pid")
	print "-"*120
	task = os.popen("top -b -n 1 | grep -E 'pw.x|dmol3.exe|castep|vasp|neb.x'").readlines()

	core_num=[]
	for soft in ["pw.x","dmol3", "castep", "vasp","neb.x"]:
		pw = sorted(filter(lambda x: soft in x,task))
		core_num.append(len(pw))
		for i in range(0,len(pw),4):
			line = re.split(r'\s+',pw[i].strip())
			pid_of=os.popen("lsof -p "+line[0]+" | egrep 'cwd|tmp'").readlines()
			if soft in ["pw.x","neb.x"] :
				cwd = re.split(r'\s+',pid_of[0].strip())[-1]
				task_name= re.split(r'\/',pid_of[-1].strip())[-1]
				cwd = cwd + "/" + ".".join(re.split(r"\.",task_name)[:-1]) + ".in"
			else:
				cwd = "/"+"/".join(re.split(r'\/',pid_of[0].strip())[1:])	
			pid = int(line[0])
			if len(cwd)>55 :
				cwd = "..." + cwd[-50:]
			print "%-10s%-10s%-60s%-10d%-10d%-10d%-10d" %(soft, line[1], cwd, pid, pid+1, pid+2, pid+3)

	print "-"*120
	print  "processes in running     %s"  %(" + ".join(map(str,core_num)))
	print "-"*120
	
task_detail()